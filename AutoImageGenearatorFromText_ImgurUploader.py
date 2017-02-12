#! python 3
# This is a simple Python script that creates an image from your clipboard
# or from your input. Gives it a nice background and uploads to imgur. It
# also copies the imgur direct link to your clipboard. Have fun using it!

'''
Version 1.0
Made by Saif Hassan
Twitter: twitter.com/saiftheboss7

Read on Github to know how to use it: https://github.com/saiftheboss7/AutoImageGenearatorFromText_ImgurUploader
'''

from PIL import Image, ImageDraw, ImageFont, ImageColor
import textwrap
import pyimgur
import pyperclip


def imageProcessor():
    text = input()
    # or use 'text = pyperclip.paste()' to paste anything that you have on
    # clipboard.
    paragraph = textwrap.wrap(text, width=30)
    # this breaks multiple lines into single lines. Play with width to have
    # your perfect separation
    MAX_W, MAX_H = 750, 350  # this defines the max width and height of the image
    color = ImageColor.getrgb('#007FFF')
    # Replace the hex code as per your need.
    im = Image.new('RGB', (MAX_W, MAX_H), color)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("seguisb.ttf", 42)
    # It is written on Windows so this is loading SegoeUISemibold font with 42
    # size by default.

    current_h, pad = 50, 10
    for line in paragraph:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + pad

    im.save('test.png')
    print('Image generated successfully in the current folder!')
    '''CLIENT_ID = Here Goes your Imgur Client ID
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image('test.png', title=text)
    print(uploaded_image.link)
    pyperclip.copy(uploaded_image.link)
    print('Direct image link has already been copied to clipboard. Have fun!')'''

imageProcessor()
