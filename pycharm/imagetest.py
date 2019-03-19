import Image


border_color = "#FF0000" #red
square_color = "#0000FF" #blue
width, height = 240, 60
midx, midy = width // 2, height // 2
image = Image.Image(width, height, "square_eye.img")
for x in range(width):
    for y in range(height):
        if x < 5 or x >= width - 5 or y < 5 or y >= height - 5:
            image[x, y] = border_color
        elif midx - 20 < x < midx + 20 and midy - 20 and midy - 20 < midy + 20:
            image[x, y] = square_color
    image.save()
    image.export("square_eye.xpm")