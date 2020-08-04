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
        images(dict)
    """
    parent_path = os.path.join(parent_path, "images")
    images = os.listdir(parent_path)
    # Gets the path of each image
    images = {
        image.split(".")[0]: pygame.image.load(os.path.join(parent_path, image))
        for image in images
    }
    # Gets the pygame surface object of each image
    images = {
        name: pygame.transform.scale(path, (i_width, i_height,),)
        for name, path in images.items()
    }
    return images

