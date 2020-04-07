import tweepy
import os
import textwrap
from PIL import ImageFont, ImageDraw, Image
import ffmpeg

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def text_on_img(f=1, text="Hello", size=60):
    if(f < 10):
        filename = 'IMGP00' + str(f) + '.jpg'
    else:
        filename ='IMGP0' + str(f) + '.jpg'
    fnt = ImageFont.truetype('arial.ttf', size)
    # create image
    image = Image.new(mode = "RGB", size = (800,600), color = "#1DA1F2")
    draw = ImageDraw.Draw(image)
    wrappedText = textwrap.wrap(text, width=23)
    # draw.text((10,10), wrappedText, font=fnt, fill=(255,255,255))
    y_text = 0
    for line in wrappedText:
        line_width, line_height = fnt.getsize(line)
        draw.text(((800 - line_width) / 2, y_text), 
                  line, font=fnt, fill=(255,255,255))
        y_text += line_height
    # save file
    image.save(filename)
    # show file
    # os.system(filename)
 
tweets = api.home_timeline()

i = 1
for tweet in tweets:
    text_on_img(f = i, text = tweet.text)
    i += 1

os.system("ffmpeg -framerate 1/3 -f image2 -i IMGP%3d.jpg test.avi")

