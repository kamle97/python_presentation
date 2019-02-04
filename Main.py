# Kamil Lesiak

from python_presentation import *

presentation = None


def slides_creation():
    slide1 = Slide(title=Title("Example title", text_size=52, text_color=RGBColor(r=255), vertical="B"),
                   subtitle=Subtitle("My Subtitle", text_color=RGBColor(b=255), vertical="T", italics=True))
    presentation.add_slides(slide1)
    slide2 = Slide(title=Title("Example 2nd title", text_size=52, text_color=RGBColor(r=255), vertical="T"),
                   subtitle=Subtitle("My Subtitle", text_color=RGBColor(b=255), vertical="T", italics=True,
                                     underline=True),
                   footer=Footer("Kamil Lesiak", italics=True))
    slide3 = Slide(title=Title("Example 3rd title", text_size=42, text_color=RGBColor(r=255), vertical="C"),
                   subtitle=Subtitle("My Subtitle", text_color=RGBColor(b=255), vertical="C", italics=True))
    presentation.add_slides(slide2, slide3)
    slide1.subtitle.vertical = "T"
    slide1.text = SlideText("example_text.txt", from_file=True, horizontal="R")
    slidelist = [slide1, slide2, slide3]
    presentation.add_slides_from_list(slidelist)
    slide_with_image = Slide(title=Title("Na tym slajdzie jest obrazek", text_color=RGBColor(g=255), vertical="T"),
                             image=Image("pict1.jpg"))
    slide_with_image2 = Slide(
        title=Title("Na tym slajdzie jest drugi obrazek", text_color=RGBColor(g=255), vertical="T"),
        image=Image("laa_liga.png"))
    slide_with_image3 = Slide(
        title=Title("Na tym slajdzie jest trzeci obrazek", text_color=RGBColor(g=255), vertical="T"),
        image=Image("pictt.jpg"))
    presentation.add_slides(slide_with_image, slide_with_image2, slide_with_image3)


def main():
    global presentation
    presentation = PythonPresentation()
    slides_creation()
    presentation.export_presentation_to_pdf("test.pdf", slides=[1, 1, 0, 1, 0, 1, 1, 1, 1])
    presentation.export_presentation_to_pptx("pres.pptx")
    return


if __name__ == "__main__":
    main()
