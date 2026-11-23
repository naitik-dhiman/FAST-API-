from fastapi import FastAPI , HTTPException
from app.schemas import PostCreate, PostResponse 

app = FastAPI()



# # ! returning a python dictionary that is returned , same kind of JSON 
# @app.get("/hello-world")
# def hello_world ():
#     return {"message" : "hello World"}



# * now moving to actual file GET * fetching post 
text_posts = {
    1: {"title": "My First Post", "content": "Learning FastAPI is exciting!"},
    2: {"title": "Python Tips", "content": "Use dictionary comprehensions to write cleaner code."},
    3: {"title": "Daily Motivation", "content": "Small progress every day leads to big results."},
    4: {"title": "Programming", "content": "Practice coding consistently to improve problem-solving."},
    5: {"title": "Project Update", "content": "I am building my first REST API using FastAPI."},
    6: {"title": "Tech Insight", "content": "APIs allow different applications to communicate."},
    7: {"title": "Learning DSA", "content": "Arrays and strings are important DSA fundamentals."},
    8: {"title": "Weekend Goals", "content": "Complete two coding problems and revise Python."},
    9: {"title": "Question", "content": "What is your favourite Python framework?"},
    10: {"title": "Mini Announcement", "content": "My new backend development journey starts today!"}
}


# * query parameters 
@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
        return list(text_posts.values())[:limit]

    return text_posts


# * dynamic path parameter 
@app.get("/posts/{id}")
def get_post (id : int ):

     if id not in text_posts :
          raise HTTPException(status_code=404 , detail= "Post Not found")
     return text_posts.get(id) 

 

# * creating a post for uploading data after creating a schema using pydantic which include title and content as data fields 

# * no return type 
# @app.post("/posts")
# def create_post (post: PostCreate):
#      new_post = {"title"  : post.title , "content" : post.content}
#      text_posts[max(text_posts.keys()) + 1 ] =  new_post 
#      return new_post 


# * with return type of data schema created 
@app.post("/posts")
def create_post (post: PostCreate)-> PostResponse: 
     new_post = {"title"  : post.title , "content" : post.content}
     text_posts[max(text_posts.keys()) + 1 ] =  new_post 
     return new_post 

# ! after defining this there may be error if we return something else 