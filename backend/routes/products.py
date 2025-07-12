from fastapi import APIRouter
from models import Product
from services import load_products,delete_product, save_product, update_product

router = APIRouter()



@router.get("/products")
def get_products():
    return load_products()

@router.post("/products")
def add_product(product: Product):
    save_product(product)
    return {"maseg": "product added seccessfully"}


@router.put("/products")
def edit_product(product: Product):
    update_product(product)
    return {"maseg": "product updated seccessfully"}



@router.delete("/products/{product_id}")
def remoce_product(product_id: int):
    delete_product(product_id)
    return {"maseg": "product updated seccessfully"}
