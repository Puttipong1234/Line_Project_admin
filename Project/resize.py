from PIL import Image

from resizeimage import resizeimage


with open('Project\static\\richimg\\action.JPG', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [2500, 1686])
        cover.save('action.jpeg', image.format)