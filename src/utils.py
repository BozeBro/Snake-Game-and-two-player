import os
import pygame

def load_images(parent_path, i_width, i_height):
    """
    loads images in a different directory
    :param
        parent_path(str) - PATH to the dir folder of the working file
        i_width(int) - width of each image
        i_height(int) - height of each image
    :return
        images(dict(str: pygame surface object))
    """
    parent_path = os.path.join(parent_path, "images")
    images = iter(os.listdir(parent_path))
    # Gets the path of each image
    # and gets pygame surface object from the path
    images = {
        image.split(".")[0]: pygame.transform.scale(
            pygame.image.load(os.path.join(parent_path, image)), 
            (i_width, i_height)
        )
        for image in images
    }
    return images

