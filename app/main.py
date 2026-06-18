
from fastapi import FastAPI

from pydantic import BaseModel
from sqlalchemy.orm import Session
from .import models,schemas,utils
from .database import engine,get_db
from fastapi import Depends
from .routers import post,user,auth,vote
from pydantic_settings import BaseSettings, SettingsConfigDict
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)

#dependency 

app=FastAPI()

#origins=["https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/")
async def root():
    return {"message":"Hello World my name is PRIYANSHU !!!!! "}

from sqlalchemy import text






#my_posts=[{"title":"title of post1","content":"content of post 1","id":1},{"title":"fav food","content":"i like pizza","id":2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id']==id:
#             return p
        
#request comes with GET method url :"/"
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#          return i







# @app.get("/check")
# def check(db: Session = Depends(get_db)):

#     result = db.execute(text("SELECT * FROM posts"))

#     rows = [dict(row._mapping) for row in result]

#     return {"data": rows}

# from sqlalchemy import text

# @app.get("/dbinfo")
# def dbinfo(db: Session = Depends(get_db)):

#     result = db.execute(
#         text("SELECT current_database(), current_schema(), current_user")
#     )

#     return {
#         "data": [dict(row._mapping) for row in result]
#     }

# @app.get("/sqlalchemy")
# def test_posts(db:Session=Depends(get_db)):
#     print(db.bind.url)
#     posts=db.query(models.Post).all()
    
#     return{"data":posts}



 


