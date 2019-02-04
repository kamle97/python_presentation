# Kamil Lesiak


class Footer:
    """
    Class represents the footer of a slide
    """

    def __init__(self, content, text_size=14, text_color=None, font="Arial", horizontal="R", bold=False,
                 underline=False, italics=False):
        """
        construction that sets the content of a footer and style properties
        :param content: what is displayed inside of a footer
        :param text_size:
        :param text_color:
        :param font:
        :param horizontal:
        :param bold:
        :param underline:
        :param italics:
        """
        self.content = content
        self.text_size = text_size
        self.text_color = text_color
        self.font = font
        self.vertical_value = 150
        self.horizontal = horizontal
        self.bold = bold
        self.underline = underline
        self.italics = italics
