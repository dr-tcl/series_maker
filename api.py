from typing import Union

from fastapi import FastAPI
from main import series_maker

app = FastAPI()


@app.get("/series_maker/")
def read_root(q: Union[int, None] = None):
    number = series_maker(q)
    return {"answer": number}
