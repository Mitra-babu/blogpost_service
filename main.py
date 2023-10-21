from fastapi import FastAPI
from database import models
from database.database import engine
from router import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(post.router)


@app.get("/")
def hello_world() -> str:
    return "hello world"


models.Base.metadata.create_all(engine)
app.mount('/images', StaticFiles(directory='images'), name='images')
origins = ["http://locahost:3000"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['*'],
                   allow_headers=['*'])
