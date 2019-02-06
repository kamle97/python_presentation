# Kamil Lesiak


class Subtitle(object):
    """
    Class that represents the subtitle of a slide
    """
    def __init__(self, content, text_size=24, text_color=None, font="Arial", vertical="C", horizontal="C", bold=False,
                 underline=False, italics=False):
        """
        constructor that receive subtitle content and style
        :param content: text that will be shown inside the subtitle section
        :param text_size:
        :param text_color:
        :param font:
        :param vertical:
        :param horizontal:
        :param bold:
        :param underline:
        :param italics:
        """
        self.content = content
        self.text_size = text_size
        self.text_color = text_color
        self.font = font
        self.vertical = vertical
        self.vertical_value = 90
        self.horizontal = horizontal
        self.bold = bold
        self.underline = underline
        self.italics = italics
        self.subtitle_vertical()

    def subtitle_vertical(self):
        """
        function that determines the position of a subtitle inside of a pdf file
        :return:
        """
        if self.vertical == "T":
            self.vertical_value = 30
        elif self.vertical == "B":
            raise AttributeError("Cannot set \"B\" (Bottom) position of a subtitle, use footer instead")
        else:
            self.vertical = "C"
