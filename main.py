# coding: utf-8
from PIL import Image, ImageFont
import os
import re

from handright import Template, handwrite

txt_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(txt_file_path, "r", encoding="utf-8") as file:
    raw_text = file.read()

text = re.sub(r"<img.*?>", "", raw_text)

text = re.sub(r"\$(.*?)\$", lambda match: " " * len(match.group(0)), text)

text = re.sub(r"-", "•", text, flags=re.MULTILINE)

text = re.sub(r"<h[1-6]>.*?</h[1-6]>", "", raw_text)

template = Template(
    background=Image.new(mode="1", size=(1485, 2100), color=1),
    font=ImageFont.truetype("/Users/legendstane/Desktop/handwritingGenerator/font2.ttf", size=40),
    line_spacing=50,  # 设置行间距
    fill=0,  # 设置字体颜色为黑色
)
images = handwrite(text, template)
for im in images:
    assert isinstance(im, Image.Image)
    im.show()