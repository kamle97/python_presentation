# Kamil Lesiak


class Title(object):
    """
        Class that represents the subtitle of a slide
    """

    def __init__(self, content, text_size=24, text_color=None, font="Arial", vertical="C", horizontal="C", bold=True,
                 underline=False, italics=False):
        """
        constructor that receive title content and style
        :param content: text that will be shown inside the title section
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
        self.vertical_value = 75
        self.horizontal = horizontal
        self.bold = bold
        self.underline = underline
        self.italics = italics
        self.title_vertical()

    def title_vertical(self):
        """
        function that determines the position of a title inside of a pdf file
        :return:
        """
        if self.vertical == "T":
            self.vertical_value = 15
        elif self.vertical == "B":
            self.vertical_value = 130
        else:
            self.vertical = "C"
