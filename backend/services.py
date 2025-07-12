from models import Movies
from database import get_connection

def load_Movies():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM movies")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Movies(**Movies) for movies in Movies]


def save_product(product: Movies):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO products (name, price, image_url) VALUES (%s, %s, %s)"
    val = (product.name, product.price, product.image_url)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    
    
def update_movie(product: Movies):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE movies SET name=%s, price=%s, image_url=%s WHERE id=%s"
    val = (Movies.name, Movies.price, Movies.image_url, Movies.id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

def delete_movie(Movies_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM products WHERE id=%s"
    cursor.execute(sql, (Movies_id,))
    conn.commit()
    conn.close()