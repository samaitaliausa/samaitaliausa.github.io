import os

s = """<article class="thumb">
    <a href="images/actual/{filename}" class="image"><img src="images/actual/{filename}" alt="" /></a>
</article>"""


image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

articleshtml = ""

def list_images(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith(tuple(image_extensions)):
            articleshtml += 

list_images("images/actual")