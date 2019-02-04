# Kamil Lesiak

from PIL import Image as PILImage


class Image(object):
    """
    Class represents image inside of a slide, and solve the scaling and the positioning problems
    """

    def __init__(self, filename=""):
        """
        constructor that gets the image from the filename
        :param filename: source of the image
        """
        self.filename = filename
        self.width = -1
        self.height = -1
        self.x = -1
        self.y = -1
        self.scale_and_position_image(filename)

    def scale_and_position_image(self, filename):
        """
        function responsible for image scaling and positioning
        :param filename: filename of an image
        :return:
        """
        im = PILImage.open(filename)
        w, h = im.size
        if w > 800:
            self.width = 800
        else:
            self.width = w

        if h > 500:
            self.height = 500
        else:
            self.height = h

        self.width /= 4
        self.height /= 4

        self.x = 150 - self.width / 2
        self.y = 100 - self.height / 2
