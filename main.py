import sqlite3
import json

def film_by_title(name):
    """return dictionary with inf about film by name"""
    connection = sqlite3.connect('netflix.db')
    sql = """
    SELECT title, country, release_year, listed_in, description
    FROM netflix
    WHERE title = ? 
    ORDER BY date_added DESC 
    """
    cursor = connection.cursor()
    data = cursor.execute(sql, (name,)).fetchall()[0]
    connection.close()
    return {
        "title": data[0],
        "country": data[1],
        "release_year": data[2],
        "genre": data[3],
        "description": data[4]
    }


def movie_by_year(year1, year2):
    """return title and release year of film by year"""
    connection = sqlite3.connect('netflix.db')
    sss = """
    SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN ? AND ?
    LIMIT 100
    """
    cursor = connection.cursor()
    data = cursor.execute(sss, (year1, year2,)).fetchall()
    sm = []
    for element in data:
        sm.append({
            "title": element[0],
            'release_year' : element[1]
        })
    return sm



def rating_family(dop):
    """ return films that have have rating 'family' """
    connection = sqlite3.connect('netflix.db')
    dop = tuple(dop)
    qqq = f"""
    SELECT title, rating, description
    FROM netflix
    WHERE rating in {dop}
    """
    cursor = connection.cursor()
    data = cursor.execute(qqq).fetchall()
    sm = []
    for element in data:
        sm.append({
            "title": element[0],
            'rating': element[1],
            'description': element[2]
        })
    return sm



def rating_adult(dop):
    """ return films that have have rating 'for adults' """
    connection = sqlite3.connect('netflix.db')
    dop = tuple(dop)
    lll = f"""
    select title, rating, description
    FROM netflix
    WHERE rating in {dop}
    """
    cursor = connection.cursor()
    data = cursor.execute(lll).fetchall()
    sm = []
    for element in data:
        sm.append({
            "title": element[0],
            'rating': element[1],
            'description': element[2]
        })
    return sm



def rating_children(dop):
    """ return films that have have rating 'for children' """
    connection = sqlite3.connect('netflix.db')
    dop = tuple(dop)
    rrr = """
    SELECT title, rating, description
    FROM netflix
    WHERE rating = 'G'
    """
    cursor = connection.cursor()
    data = cursor.execute(rrr).fetchall()
    sm = []
    for element in data:
        sm.append({
            "title": element[0],
            'rating': element[1],
            'description': element[2]
        })
    return sm



def film_by_genre(genre):
    """ return film by genre"""
    connection = sqlite3.connect('netflix.db')
    sql = f"""
    SELECT title, description
    FROM netflix
    WHERE listed_in = '{genre}' 
    ORDER BY release_year DESC
    LIMIT 10
    """
    cursor = connection.cursor()
    data = cursor.execute(sql).fetchall()
    sm = []
    for i in data:
        sm.append({"title": i[0], "description": i[1]})
    return sm



def get_actors(act1, act2):
    """ return names of actors who were colleges  more that 2 times with both,who are in arguments"""
    connection = sqlite3.connect('netflix.db')
    sql = f"""
    SELECT `cast`
    FROM netflix
    WHERE `cast` LIKE '%{act1}%{act2}%'
    """
    cursor = connection.cursor()
    data = cursor.execute(sql).fetchall()
    sm = {}
    for el in data:
        for i in el[0].split(', '):
            if i in sm.keys():
                sm[i] += 1
            else:
                sm[i] = 1
    result = []
    for k, v in sm.items():
        if v >= 2:
            result.append(k)
    result.pop(0)
    result.pop(0)
    return result



def get_films(typp, year, genree):
    """ get name and description of film by tipe, release_year and genre of film """
    connection = sqlite3.connect('netflix.db')
    sql = f"""
        SELECT title, description
        FROM netflix
        WHERE type = '{typp}'
        AND release_year = {year}
        AND listed_in LIKE  '%{genree}%'
        """
    cursor = connection.cursor()
    data = cursor.execute(sql).fetchall()
    sm = []
    for i in data:
        sm.append({'title': i[0], 'description': i[1]})
    return sm

