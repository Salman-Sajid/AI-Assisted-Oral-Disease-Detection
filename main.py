from fastapi import FastAPI , File, UploadFile 
from fastapi.staticfiles import StaticFiles
import random
import string
import shutil
import os
import uvicorn
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
from pydantic import BaseModel
import subprocess
from detect import run
app = FastAPI()

host = 'http://192.168.43.30:8000'

class ImageInput(BaseModel):
    image: bytes
    name: str

# Path to the YOLOv5 model and output directory
model_path = 'C://Users//User//Desktop//Dataset//Modelv2//last.pt'
output_dir = 'C://Users//User//Desktop//Dataset//Modelv2//integration//runs//detect//exp'

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ping")
async def ping():
    return "Hello, I am alive"


@app.post("/predict")
async def detect_image(image: UploadFile = File(...)):
    # Save the image file to disk
    image_path = 'C://Users/User/Desktop/Dataset/f1.jpg'
    with open(image_path, 'wb') as f:
        f.write(await image.read())
    # C:\Users\User\Desktop\Dataset\Modelv2\integration\yolov5\runs\detect\exp
    # Run the detect.py script using subprocess
    save_dir = run(weights='C://Users/User/Desktop/Dataset/Modelv2/last.pt', source=image_path)
    print(save_dir)
    
    # Read the output image file and return it as a response
    output_path = 'C://Users/User/Desktop/Dataset/Modelv2/integration/yolov5/runs/detect/exp/f1.jpg'

    file_name = f'{random_filename(6)}.jpg'

    shutil.copy2(output_path, f'static/{file_name}')

    return {"url": f'{host}/static/{file_name}'}

def random_filename(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)