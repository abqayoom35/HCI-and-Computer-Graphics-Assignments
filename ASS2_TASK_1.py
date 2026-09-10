import math
W = int(input("Enter horizontal resolution (pixels): "))
H = int(input("Enter vertical resolution (pixels): "))
D = float(input("Enter physical diagonal size (inches): "))

# Total pixels
total_pixels = W * H

# Aspect ratio
gcd = math.gcd(W, H)
aspect_w = W // gcd
aspect_h = H // gcd

# DPI/PPI
diagonal_pixels = math.sqrt(W**2 + H**2)
dpi = diagonal_pixels / D

# Density classification
if dpi < 100:
    category = "Low Density (Standard Monitor)"
elif dpi <= 200:
    category = "Medium Density (HD Display)"
else:
    category = "High Density (Retina / Mobile)"

print("\n--- DISPLAY METRICS ANALYSIS ---")
print("Total Pixel Count :", total_pixels, "pixels")
print("Aspect Ratio      :", aspect_w, ":", aspect_h)
print("Calculated DPI    :", round(dpi, 2), "DPI")
print("Density Category  :", category)