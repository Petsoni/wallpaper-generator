import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Set the size of the wallpaper
width, height = 3840, 2160

# Create a new image with a dark background

# Draw the mountains
# mountain_colors = ["#8FBCBB", "#88C0D0", "#81A1C1", "#5E81AC", "#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#B48EAD",
#                    "#5E81AC", "#88C0D0", "#EBCB8B", "#D08770", "#BF616A", "#A3BE8C", "#B48EAD"]


mountain_colors = ["#282a2e", "#373b41", "#c5c8c6", "#4C566A", "#434C5E", "#3B4252", "#2E3440"]


# "#4C566A", "#434C5E", "#3B4252", "#2E3440",

# Function to generate random mountain points
def generate_mountain_points(base_y, peak_x, peak_y, width_range):
    left_base_x = peak_x - width_range
    right_base_x = peak_x + width_range
    return [(left_base_x, base_y), (peak_x, peak_y), (right_base_x, base_y)]


# Generate 10 wallpapers
for n in range(10):
    wallpaper = Image.new("RGB", (width, height), "#1d1f21")
    draw = ImageDraw.Draw(wallpaper)
    base_y = height
    num_mountains = 3

    # Add some stars to the sky
    num_stars = 150
    for _ in range(num_stars):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        draw.ellipse((x, y, x + 3, y + 3), fill="#c5c8c6")

    for i in range(num_mountains):
        peak_x = np.random.randint(200, width - 200)
        peak_y = np.random.randint(height // 3, 2 * height // 3)
        width_range = np.random.randint(1000, 1200)
        random_color_in_list = random.randint(0, len(mountain_colors) - 1)
        color = mountain_colors[random_color_in_list]
        points = generate_mountain_points(base_y, peak_x, peak_y, width_range)
        draw.polygon(points, fill=color)

    # Blur the image slightly to create a dreamy effect
    wallpaper = wallpaper.filter(ImageFilter.GaussianBlur(1))

    # Save the wallpaper
    wallpaper_path = f"generated/ngi_{n}.jpg"
    wallpaper.save(wallpaper_path)
