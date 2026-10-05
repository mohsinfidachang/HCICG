import os
from PIL import Image
import numpy as np
import cv2
# import matplotlib.pyplot as plt

def inspect_image(image_path: str) -> dict:
    """Load the image and return its measured image-data properties."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    img = Image.open(image_path)
    width, height = img.size
    img_array = np.array(img)

    if img_array.ndim == 2:
        channels = 1
        shape = [height, width]
    else:
        channels = img_array.shape[2] if img_array.ndim == 3 else 3
        shape = [height, width, channels]

    if img.mode == 'L': channels = 1
    if img.mode == 'RGB': channels = 3
    if img.mode == 'RGBA': channels = 4

    pixel_count = width * height
    estimated_bytes = pixel_count * channels

    result = {
        "width": width,
        "height": height,
        "channels": channels,
        "shape": shape,
        "pixel_count": pixel_count,
        "estimated_bytes": estimated_bytes,
        "color_order": "RGB"
    }
    print(f"[Task1] {result}")
    return result
