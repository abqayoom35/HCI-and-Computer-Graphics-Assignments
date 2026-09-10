import numpy as np

# Create a black image
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Top-left = Red
img[:150, :200] = [255, 0, 0]

# Top-right = Green
img[:150, 200:] = [0, 255, 0]

# Bottom-left = Blue
img[150:, :200] = [0, 0, 255]

# Bottom-right = White
img[150:, 200:] = [255, 255, 255]

print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape:", img.shape)
print("Data Type:", img.dtype)
print("Total Elements:", img.size)
print("Memory Footprint:", img.nbytes, "bytes")