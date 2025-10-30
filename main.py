from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from uuid import uuid4
import os

app = FastAPI()
UPLOAD_DIR = "static"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

items = []  # In-memory storage


@app.post("/api/product")
async def create_item(
    request: Request,
    name: str = Form(...),
    price: float = Form(...),
    qty: int = Form(...),
    image: UploadFile = File(None)
):
    item_id = str(uuid4())
    amount = price * qty
    full_image_url = None

    if image and image.filename:
        ext = os.path.splitext(image.filename)[1]
        filename = f"{uuid4()}{ext}"
        path = os.path.join(UPLOAD_DIR, filename)
        with open(path, "wb") as f:
            f.write(await image.read())
        full_image_url = f"{str(request.base_url).rstrip('/')}/static/{filename}"

    item = {"id": item_id, "name": name, "price": price, "qty": qty, "amount": amount, "fullImageUrl": full_image_url}
    items.append(item)
    return item


@app.get("/api/product")
def get_items():
    return items


@app.get("/api/product/{item_id}")
def get_item(item_id: str):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Not found"}


@app.put("/api/product/{item_id}")
async def update_item(
    item_id: str,
    request: Request,
    name: str = Form(...),
    price: float = Form(...),
    qty: int = Form(...),
    image: UploadFile = File(None)
):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            amount = price * qty
            full_image_url = item["fullImageUrl"]

            if image and image.filename:
                ext = os.path.splitext(image.filename)[1]
                filename = f"{uuid4()}{ext}"
                path = os.path.join(UPLOAD_DIR, filename)
                with open(path, "wb") as f:
                    f.write(await image.read())
                full_image_url = f"{str(request.base_url).rstrip('/')}/static/{filename}"

            items[i] = {"id": item_id, "name": name, "price": price, "qty": qty, "amount": amount, "fullImageUrl": full_image_url}
            return items[i]
    return {"error": "Not found"}


@app.delete("/api/product/{item_id}")
def delete_item(item_id: str):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(i)
            return {"message": "Deleted"}
    return {"error": "Not found"}