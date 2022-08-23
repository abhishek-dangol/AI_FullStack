from typing import Union

from fastapi import FastAPI
from copycat import generate_branding_snippet, generate_keywords


app = FastAPI()


@app.get("/generate_snippet")
def generate_snippet_api(prompt: str):
    # snippet = generate_branding_snippet()
    return {"message": f"Hello CopyCat prompt: {prompt}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# python3 -m uvicorn copycat_api:app --reload
