from flask import Flask, jsonify
from main import *

app = Flask(__name__)


@app.route("/movie/<title>")
def title(title):
    """ page with film by name """
    film = film_by_title(title)
    return jsonify(film)


@app.route("/movie/<int:year1>/to/<int:year2>")
def by_year(year1, year2):
    """page with films between 2 years """
    film = movie_by_year(year1, year2)
    return jsonify(film)


@app.route('/rating/family')
def family_rating():
    """ page of films with rating 'family' """
    films = rating_family(['G', 'PG', 'PG-13'])
    return jsonify(films)


@app.route('/rating/adult')
def adult_rating():
    """ page of films with rating 'adult' """
    films = rating_adult(['R', 'NC-17'])
    return jsonify(films)


@app.route('/rating/children')
def children_rating():
    """ page of films with rating 'children' """
    films = rating_children(['G'])
    return jsonify(films)

@app.route('/genre/<genre>')
def film_genre(genre):
    """ films by genre """
    films = film_by_genre(genre)
    return jsonify(films)


if __name__ == '__main__':
    app.run()

