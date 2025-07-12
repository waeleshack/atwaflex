from fastapi import APIRouter
from models import Movies
from services import load_movies,delete_movies, save_movies, update_movie

router = APIRouter()



@router.get("/movies")
def get_movies():
    return load_movies()

@router.post("/movies")
def add_movies(product: Movies):
    save_movies(product)
    return {"maseg": "product added seccessfully"}


@router.put("/products")
def edit_Movies(movies: Movies):
    update_movie(movies)
    return {"maseg": "movies updated seccessfully"}



@router.delete("/products/{product_id}")
def remoce_movies(movies_id: int):
    delete_movies(movies_id)
    return {"maseg": "movie updated seccessfully"}
