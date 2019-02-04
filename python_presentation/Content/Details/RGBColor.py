# Kamil Lesiak


class RGBColor:
    """
    Class that represents color of a text in RGB format
    """
    def __init__(self, r=0, g=0, b=0):
        """
        constructor that receive RGB color values
        :param r:
        :param g:
        :param b:
        """
        self.r = r
        self.g = g
        self.b = b
        self.check_correctness()

    def check_correctness(self):
        """
        checking the correctness of the given RGB values
        :return:
        """
        if self.r < 0 or self.r > 255 or self.g < 0 or self.g > 255 or self.b < 0 or self.b > 255:
            raise ValueError("RGB arguments should be between 0 and 255")
