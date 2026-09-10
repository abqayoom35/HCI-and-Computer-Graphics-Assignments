"""
Task 3: Channel Slicing & Isolation
-------------------------------------
Loads sample.jpg, extracts R/G/B 2D intensity grids (Axis 2 slicing),
builds single-channel color views, and displays a 2x3 subplot grid.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1. Load image into a NumPy array
img = np.array(Image.open("sample.jpg").convert("RGB"))
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape : {img.shape}")

# 2. Extract 2D intensity grids (Axis 2 slicing: [:, :, channel_index])
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]

print(f"Red Channel 2D Shape  : {red_channel.shape}  | Mean Intensity: {red_channel.mean():.2f}")
print(f"Green Channel 2D Shape: {green_channel.shape} | Mean Intensity: {green_channel.mean():.2f}")
print(f"Blue Channel 2D Shape : {blue_channel.shape}  | Mean Intensity: {blue_channel.mean():.2f}")

# 3. Build 3D color-isolated arrays (other two channels zeroed out)
red_only = np.zeros_like(img)
red_only[:, :, 0] = red_channel

green_only = np.zeros_like(img)
green_only[:, :, 1] = green_channel

blue_only = np.zeros_like(img)
blue_only[:, :, 2] = blue_channel

# 4. Display in a 2x3 subplot grid
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Top row: color-isolated versions
axes[0, 0].imshow(red_only);   axes[0, 0].set_title("Red Only");   axes[0, 0].axis("off")
axes[0, 1].imshow(green_only); axes[0, 1].set_title("Green Only"); axes[0, 1].axis("off")
axes[0, 2].imshow(blue_only);  axes[0, 2].set_title("Blue Only");  axes[0, 2].axis("off")

# Bottom row: grayscale intensity maps
axes[1, 0].imshow(red_channel, cmap="gray");   axes[1, 0].set_title("Red Intensity");   axes[1, 0].axis("off")
axes[1, 1].imshow(green_channel, cmap="gray"); axes[1, 1].set_title("Green Intensity"); axes[1, 1].axis("off")
axes[1, 2].imshow(blue_channel, cmap="gray");  axes[1, 2].set_title("Blue Intensity");  axes[1, 2].axis("off")

plt.tight_layout()
plt.savefig("task3_channels_output.png", dpi=150)
print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")
plt.show()