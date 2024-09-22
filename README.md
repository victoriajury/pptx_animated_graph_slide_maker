## Get images from Notebook into an animated powerpoint slide

### Problem
I need to display images from a Jupyter notebook in a presentation. The images should
be on one slide and revealed one after the other, by clicking or shown automatically
after a specified delay.

Copying, stacking and animating the images is cumbersome and time-consuming if there
are many of them.

### Solution
Theses scripts export images from a Jupyter notebook and saves them to a folder. These
images are then inserted into Powerpoint presentation slide and animated to appear
one after the other.

The images are stacked in the order that they appear in the Jupyter notebook.

### Notes

- The `pptx` library does not support animations. I had to manipulate the presentation
xml to apply the effects. 

- Adding more than one set of images to a slide might break the presentation, since
the image IDs might be shared across sets and wont be unique within the slide.

### Usage

#### Dependencies
- Python 3
- pipenv
- pptx


**To export the images from notebook to your specified directory:**
```
if __name__ == "__main__":
    export_images("test_notebook.ipynb", output_dir="nb_images", prefix=None)
```
```
python nb_exporter.py
```

**To insert images into a new presentation:**

Effect options: `on_click` and `after_click`

```
if __name__ == "__main__":
    create_presentation("test.pptx", "nb_images", effect="after_click", delay=200)
```
```
python slide_maker.py
```
