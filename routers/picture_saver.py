"""this file create name for picture and save picture in 'static/photos'."""

import os
import secrets

from PIL import Image

from app import app


def save_picture(form_picture):
    """Create name and size for picture and save picture."""
    # create default name for picture if picture not selected
    if form_picture is None:
        picture_file_name = 'default.jpg'
        return picture_file_name
    # create random numbers name for picture if picture selected
    else:
        random_hex = secrets.token_hex(8)
        _, file_extension = os.path.splitext(form_picture.filename)
        picture_file_name = random_hex + file_extension
        picture_path = os.path.join(app.root_path, 'static/photos', picture_file_name)
        output_size = (125, 125)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)
        return picture_file_name
