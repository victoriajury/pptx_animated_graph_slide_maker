from pptx import Presentation
from pptx.util import Inches

from effects import images_appear_on_click_effect

images = [
    "images/tomato_blue.png",
    "images/tomato_red.png",
    "images/tomato_green.png",
    "images/tomato_yellow.png",
]

top = Inches(1)
left = Inches(5)
height = Inches(5.5)

prs = Presentation()
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

for img in images:
    pic = slide.shapes.add_picture(img, left, top, height=height)

images_appear_on_click_effect(images, slide)

prs.save("test3.pptx")
