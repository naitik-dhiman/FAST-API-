from fastapi import FastAPI

app = FastAPI()



# ! returning a python dictionary that is returned same kind of JSON 
@app.get("/hello-world")
def hello_world ():
    return {"message" : "hello World"}