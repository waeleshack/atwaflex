from fastapi import APIRouter
from models import movies
from services import load_movies,delete_movies, save_movies, update_movies

router = APIRouter()



@router.get("/movies")
def get_products():
    return load_movies()

@router.post("/products")
def add_movies(product: movies):
    save_movies(product)
    return {"maseg": "product added seccessfully"}


@router.put("/products")
def edit_Movies(Movies: movies):
    update_movies(Movies)
    return {"maseg": "movies updated seccessfully"}



@router.delete("/products/{product_id}")
def remoce_movies(movies_id: int):
    delete_movies(movies_id)
    return {"maseg": "movie updated seccessfully"}
