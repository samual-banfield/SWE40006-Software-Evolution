import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    {"quote": "May the Force be with you.", "movie": "Star Wars", "year": 1977},
    {"quote": "I'll be back.", "movie": "The Terminator", "year": 1984},
    {"quote": "Here's looking at you, kid.", "movie": "Casablanca", "year": 1942},
    {"quote": "You're gonna need a bigger boat.", "movie": "Jaws", "year": 1975},
    {"quote": "There's no place like home.", "movie": "The Wizard of Oz", "year": 1939},
    {"quote": "I see dead people.", "movie": "The Sixth Sense", "year": 1999},
    {"quote": "Houston, we have a problem.", "movie": "Apollo 13", "year": 1995},
    {"quote": "To infinity and beyond!", "movie": "Toy Story", "year": 1995},
]

@app.route("/")
def index():
    return jsonify({"message": "Random Quote API", "endpoints": ["/quote", "/quotes"]})

@app.route("/quote")
def random_quote():
    return jsonify(random.choice(QUOTES))

@app.route("/quotes")
def all_quotes():
    return jsonify(QUOTES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    