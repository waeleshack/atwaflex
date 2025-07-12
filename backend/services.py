from models import Movies
from database import get_connection

def load_movies():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Movies(**Movies) for movies in Movies]


def save_movies(movies: Movies):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO movies (name, descreption, image_url) VALUES (%s, %s, %s)"
    val = (movies.name, movies.descreption, movies.image_url)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    
    
def update_movie(product: Movies):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE movies SET name=%s, descreption=%s, image_url=%s WHERE id=%s"
    val = (Movies.name, Movies.price, Movies.image_url, Movies.id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

def delete_movies(movies_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM movies WHERE id=%s"
    cursor.execute(sql, (movies_id))
    conn.commit()
    conn.close()