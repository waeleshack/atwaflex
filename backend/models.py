from pydantic import BaseModel

class Movies(BaseModel):
    id : int
    name : str
    Descreption : float
    image_url : str
    tag : str
    