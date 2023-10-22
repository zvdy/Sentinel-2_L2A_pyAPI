import io
from typing import Optional
import matplotlib.pyplot as plt
from fastapi import FastAPI, File, UploadFile
import rasterio
from PIL import Image
import uvicorn


app = FastAPI()


@app.post("/attributes")
async def get_image_attributes(image_file: UploadFile = File(...)):
    # Read the image file with Rasterio
    with rasterio.open(image_file.file) as dataset:
        # Extract the required attributes
        width = dataset.width
        height = dataset.height
        bands = dataset.count
        crs = dataset.crs.to_dict()
        bbox = dataset.bounds
        driver = dataset.driver
        dtype = dataset.dtypes[0]
        transform = dataset.transform


    # Return the attributes as a JSON object
    return {
        "width": width,
        "height": height,
        "bands": bands,
        "crs": crs,
        "bbox": bbox,
        "driver": driver,
        "dtype": dtype,
        "transform": transform
    }


@app.post("/thumbnail", response_model=bytes)
async def thumbnail(image: UploadFile, resolution: Optional[int] = None):
    # Read the image as a PIL Image object.
    image = Image.open(io.BytesIO(await image.read()))

    # Resize the image.
    if resolution is not None:
        image = image.resize((resolution, resolution))

    # Convert the image to RGB mode.
    image = image.convert("RGB")

    # Save the image as a PNG.
    png = io.BytesIO()
    image.save(png, format="PNG")

    # Return the PNG as bytes.
    return png.getvalue()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)