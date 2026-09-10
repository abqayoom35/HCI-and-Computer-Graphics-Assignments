# Task 4: Spatial Downsampling & Pixelation via Striding
# ---------------------------------------------------------
# Downsamples an image using NumPy step-slicing (img[::N, ::N, :]),
# re-expands it with np.repeat() to visualize pixelation, and reports
# the reduction in dimensions and memory.

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

N = 8  # step factor

# Load original image
img = np.array(Image.open("sample.jpg").convert("RGB"))
orig_shape = img.shape
orig_mem = img.nbytes

# 1. Downsample: take every N-th pixel along rows and columns
downsampled = img[::N, ::N, :]
down_shape = downsampled.shape
down_mem = downsampled.nbytes

# 2. Re-expand back to original size for a blocky/pixelated look
#    np.repeat along axis 0 (rows) then axis 1 (columns)
re_expanded = np.repeat(downsampled, N, axis=0)
re_expanded = np.repeat(re_expanded, N, axis=1)
# Trim/pad in case of rounding so it matches the original exactly
re_expanded = re_expanded[: orig_shape[0], : orig_shape[1], :]

# 3. Calculate reduction percentages
dim_reduction_pct = (1 - (down_shape[0] * down_shape[1]) ** 0.5 /
                      (orig_shape[0] * orig_shape[1]) ** 0.5) * 100
# Simpler equivalent, matching sample output: reduction per axis = (1 - 1/N) * 100
dim_reduction_per_axis = (1 - 1 / N) * 100
mem_reduction_pct = (1 - down_mem / orig_mem) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape     : {orig_shape} | Memory: {orig_mem:,} bytes")
print(f"Downsampled Shape  : {down_shape} | Memory: {down_mem:,} bytes")
print(f"Re-expanded Shape  : {re_expanded.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction_per_axis:.2f}% reduction per axis")
print(f"Memory Savings     : {mem_reduction_pct:.2f}% data reduction")

# Optional visualization
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img); axes[0].set_title("Original"); axes[0].axis("off")
axes[1].imshow(re_expanded); axes[1].set_title(f"Pixelated (N={N})"); axes[1].axis("off")
plt.tight_layout()
plt.savefig("task4_downsampling_output.png", dpi=150)
plt.show()