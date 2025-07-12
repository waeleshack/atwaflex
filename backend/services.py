from models import Product
from database import get_connection

def load_products():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Product(**product) for product in products]


def save_product(product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO products (name, price, image_url) VALUES (%s, %s, %s)"
    val = (product.name, product.price, product.image_url)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    
    
def update_product(product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE products SET name=%s, price=%s, image_url=%s WHERE id=%s"
    val = (product.name, product.price, product.image_url, product.id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

def delete_product(product_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM products WHERE id=%s"
    cursor.execute(sql, (product_id,))
    conn.commit()
    conn.close()