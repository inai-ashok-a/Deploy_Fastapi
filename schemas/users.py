from pydantic import BaseModel
import re   #importing regular matching from the inbuild class


class User(BaseModel):
    name:str
    age:int
    email:str


