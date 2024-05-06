#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:03:42 2024

@author: mac
"""
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt  # Make sure to import pyplot


image_path = "/Users/mac/Downloads/original.png"
original_image = Image.open(image_path)  # Reading the image from the provided path

# Applying a box blur filter
filtered_image = original_image.filter(ImageFilter.BoxBlur(3))
plt.imshow(filtered_image)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

filtered_image_path = "mean_filtered_image.png"
filtered_image.save(filtered_image_path)  # Saving the filtered image

