from .. import models,schemas,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import APIRouter
from typing import List,Optional
from sqlalchemy import func

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user),Limit:int=10,skip:int=0,search:Optional[str]=" "):
   # cursor.execute("""SELECT * FROM posts""")  #sql query
   # posts=cursor.fetchall()
    #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    posts=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()  #by default left inner join 
    #print(results)
  
    #return {"data":posts}
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_posts(post:schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s)RETURNING * """,(post.title,post.content,post.published ))
    # new_post=cursor.fetchone()
    #conn.commit()
    #print(**post.dict())
    #new_post=models.Post(title=post.title,content=post.content,published=post.published)
    #or
    print(current_user.id)
    new_post=models.Post(User_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  #same for returning
   

    #return{"data":new_post}
    return new_post


#title str, content str, category, bool published 


#retive one individual post
@router.get("/{id}",response_model=schemas.PostOut,)
def get_post(id: int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id),))
    #post=db.query(models.Post).filter(models.Post.id==id).first()
    # post=cursor.fetchone()
    #print(Test_post)
    #post=find_post(int(id))  # int(id)because its bydefault return as string we need to convert to int
    post=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
        #response.status_code=status.HTTP_404_NOT_FOUND
       # return {"message":f"post with id: {id} was not found"}
    #return{"post_details":post}
    # if post.User_id!=current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="not authorized to perform requested action")
    
    return post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #delete post
    # find the index in the array that has required id 
    # my_posts.pop(index)
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""",(str(id),))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    #index=find_index_post(id)
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post =post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} does not exist")
    if post.User_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized to perform request at action")
    post_query.delete(synchronize_session=False)
    db.commit()
    #my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id:int,post:schemas.PostCreate,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title=%s,content=%s,published=%s  WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post=cursor.fetchone()
    # #index=find_index_post(id)
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    updated_post=post_query.first()
    if updated_post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} does not exist")
    if updated_post.User_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized to perform request at action")
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    #post_dict=post.dict()
    #post_dict['id']=id
    #my_posts[index]=post_dict
    #return{"data": post_query.first()}
    return updated_post
