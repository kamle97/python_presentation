# Kamil Lesiak


class Slide:
    """
    Class represents slide content
    """

    def __init__(self, *, title=None, subtitle=None, text=None, footer=None, image=None):
        """
        constructor with all optional arguments, that created slides with expected content
        :param title: slide title
        :param subtitle: slide subtitle
        :param text: slide normal text
        :param footer: slide footer
        :param image: image shows on the slide
        """
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.footer = footer
        self.image = image
