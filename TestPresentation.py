# Kamil Lesiak

import unittest
from python_presentation import *


class TestMethods(unittest.TestCase):

    def test_wrong_image_path(self):
        with self.assertRaises(FileNotFoundError):
            Slide(image=Image("wrong_path"))

    def test_wrong_text_path(self):
        with self.assertRaises(FileNotFoundError):
            Slide(text=SlideText("wrong_path", from_file=True))

    def test_too_high_color_value(self):
        with self.assertRaises(ValueError):
            RGBColor(r=2, g=3, b=280)

    def test_too_low_color_value(self):
        with self.assertRaises(ValueError):
            RGBColor(r=2, g=-3, b=28)

    def test_default_title_position(self):
        title = Title("ex title", vertical="wrong")
        self.assertEqual(title.vertical, "C")

    def test_default_subtitle_position(self):
        subtitle = Subtitle("ex subtitle", vertical="wrong")
        self.assertEqual(subtitle.vertical, "C")

    def test_footer_proposition_from_botton_subtitle(self):
        with self.assertRaises(AttributeError):
            Subtitle("ex subtitle", vertical="B")


if __name__ == '__main__':
    unittest.main()
