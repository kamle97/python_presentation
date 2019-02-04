# Kamil Lesiak


class SlideText(object):
    """
    Function represents the normal text inside the slide
    """

    def __init__(self, content, from_file=False, text_size=12, text_color=None, font="Arial", horizontal="C",
                 bold=False, underline=False, italics=False):
        """
        constructor that receive text and text style
        the text could be imported from the file, then the second argument have to be set to True
        :param content: text that will be displayed
        :param from_file: flag that have to be set to true if the content argument is the filename
        :param text_size:
        :param text_color:
        :param font:
        :param horizontal:
        :param bold:
        :param underline:
        :param italics:
        """
        if from_file:
            with open(content, 'r') as file:
                self.content = file.read()
        else:
            self.content = content
        self.text_size = text_size
        self.text_color = text_color
        self.font = font
        self.vertical_value = 50
        self.horizontal = horizontal
        self.bold = bold
        self.underline = underline
        self.italics = italics
