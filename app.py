import os

import openai
from flask import Flask, redirect, render_template, request, url_for

import prompts

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        days = request.form["days"]
        response_rooms = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompts.generate_rooms(animal),
            temperature=0.6,
        )
        response_amenities = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompts.generate_amenities(animal),
            temperature=0.6,
        )
        response_prices = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompts.generate_prices(days),
            temperature=0.6,
        )
        return redirect(url_for("index", 
            rooms=response_rooms.choices[0].text, 
            amenities=response_amenities.choices[0].text, 
            prices=response_prices.choices[0].text))

    rooms = request.args.get("rooms")
    amenities = request.args.get("amenities")
    prices = request.args.get("prices")
    return render_template("index.html", rooms=rooms, amenities=amenities, prices=prices)

