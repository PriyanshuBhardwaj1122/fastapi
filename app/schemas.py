from pydantic import BaseModel,Field
from datetime import datetime
from pydantic import EmailStr
from typing import Optional,Annotated
from pydantic import ConfigDict
#from pydantic.types import conint
#schema

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class userOut(BaseModel):
    id:int
    email:str
    created_at:datetime

    model_config = ConfigDict(from_attributes=True) 

        
class PostCreate(PostBase):
    pass    

class PostResponse(PostBase):
    id:int
    created_at:datetime
    User_id:int
    owner:userOut


    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post: PostResponse
    votes:int

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email:EmailStr
    password:str
  



class Userlogin(BaseModel):
      email:str
      password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class Token_data(BaseModel):
    id:Optional[int] = None  



class Vote(BaseModel):
    post_id:int
    dir: Annotated[int,Field(ge=0,le=1)]