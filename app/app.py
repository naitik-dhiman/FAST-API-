from fastapi import FastAPI , HTTPException

app = FastAPI()



# # ! returning a python dictionary that is returned , same kind of JSON 
# @app.get("/hello-world")
# def hello_world ():
#     return {"message" : "hello World"}



# * now moving to actual file GET * fetching post 
text_posts = {1 : {"title": "New post " , "content" : "cool test post"}}


@app.get("/posts")
def get_all_posts(): 
     return text_posts 

# * dynamic path parameter 
@app.get("/posts/{id}")
def get_post (id : int ):

     if id not in text_posts :
          raise HTTPException(status_code=404 , details = "Post Not found")
     return text_posts.get(id) 