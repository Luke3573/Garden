# First import wget python module.
import wget

# Set up the image URL
image_url = "https://readm.org/uploads/chapter_files/16594/279/1.jpg"

# Use wget download method to download specified image url.
image_filename = wget.download(image_url)

print('Image Successfully Downloaded: ', image_filename)