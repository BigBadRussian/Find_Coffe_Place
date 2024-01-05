import json
import os

from geopy import distance
import requests
import folium
from flask import Flask
from dotenv import load_dotenv


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def calc_distance(your_coordinates, coffee_place_coordinates):
    distance_to_coffee = distance.distance(your_coordinates[::-1], coffee_place_coordinates).kilometers
    return distance_to_coffee


def define_your_coordinate():
    load_dotenv()
    address = input("Где вы находитесь? \n")
    your_coordinates = fetch_coordinates(apikey=os.getenv('TOKEN'), address=address)
    return your_coordinates


def open_coffees_data():
    with open("coffee.json", "r", encoding="CP1251") as file:
        coffee_places = json.load(file)
    return coffee_places


def show_closest_coffees(location):
    coffee_places_distance_to_you = []
    for coffee_place in open_coffees_data():
        coffe_place_coordinates = (coffee_place["Latitude_WGS84"], coffee_place["Longitude_WGS84"])
        coffee_places_distance_to_you.append({"title": coffee_place["Name"],
                                              "latitude": coffee_place["Latitude_WGS84"],
                                              "longitude": coffee_place["Longitude_WGS84"],
                                              "distance": calc_distance(
                                                  coffee_place_coordinates=coffe_place_coordinates,
                                                  your_coordinates=location)})
    coffee_places_distance_to_you.sort(key=lambda coffee: coffee['distance'])
    top_coffee_points = coffee_places_distance_to_you[:5]
    return top_coffee_points


def create_coffe_map_html(location):
    location_float = (float(location[1]), float(location[0]))
    coffee_map = folium.Map(location=location_float, zoom_start=16)
    for coffee_point in show_closest_coffees(location=location):
        folium.Marker(
            location=[coffee_point["latitude"], coffee_point["longitude"]],
            tooltip="Click me!",
            popup=coffee_point["title"],
            icon=folium.Icon(icon="cloud"),
        ).add_to(coffee_map)
    coffee_map.save("coffee_map.html")


def create_site():
    with open('coffee_map.html') as file:
        return file.read()


def main():
    create_coffe_map_html(define_your_coordinate())
    app = Flask(__name__)
    app.add_url_rule('/', 'hello', create_site)
    app.run('0.0.0.0')


if __name__ == "__main__":
    main()
