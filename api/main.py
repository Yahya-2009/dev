#importing fastapi
from fastapi import FastApi 
from fastapi.middleware.cors import CORSMiddleware
# Initialize the FastAPI application 
app = FastApi(
    title="FastApi Example",
    description="This is an example of using FastApi"
)

# define endpoints or routes
@app.get('/')
def default_route():
    """
    This is the defualt endpoint for this back-end.
    """
    return "you have just reached the default route. Back-end server is listening..


@app.get("/example")
def get_example():
    """
    This endpoint returns a JSON object consisting of a simple message.
    """
    return {"message": "Hello World!", "year":2025}


@app.get("/example2")
def get_example2(name):  #can also pass in paremeters
    """
    This endpoint takes in a parameter called "name"
    """
    return {"message": f"Hello World {name}!"}