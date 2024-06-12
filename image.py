from PIL import Image, ImageDraw

# Open the image file
img = Image.open('Capture.PNG').convert("RGBA")

# Create a mask
mask = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(mask)
width, height = img.size
draw.ellipse((0, 0, width, height), fill=255)

# Apply the mask to the image
result = Image.new('RGBA', img.size)
result.paste(img, (0, 0), mask)

# Crop the result to the circle bounds (optional)
bbox = mask.getbbox()
result = result.crop(bbox)

# Save the output
result.save('circular_image.png')