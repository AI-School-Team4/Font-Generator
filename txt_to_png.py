import os
from PIL import Image, ImageDraw, ImageFont

# make sure you have the fonts locally in a fonts/ directory
#===========================================================
# directory for Windows :D
# font_dir = 'C:/WINDOWS/Fonts/HMFMPYUN.ttf' # .ttf file
font_dir = 'C:/WINDOWS/Fonts/BATANG.ttc' # .ttc file
font_name = '바탕' # font_name으로 해당 폰트의 이미지 파일 디렉토리 생성
#===========================================================
W, H = (200, 200) # image size (width, height)
background = (255,255,255) # white / dataset background
background2 = (0, 164, 201) # light blue / sample background
fontsize = 100
create_sample = True
#===========================================================
if create_sample:
    for idx in range(44032,44033): # sample data ('가')
        txt = chr(idx) # text to render
        font = ImageFont.truetype(font_dir, fontsize)
        image = Image.new('RGBA', (W, H), background2)
        draw = ImageDraw.Draw(image)
    # w, h = draw.textsize(txt) # not that accurate in getting font size
        w, h = font.getsize(txt)
        draw.text(((W-w)/2,(H-h)/2), txt, fill='white', font=font)
    # draw.text((10, 0), txt, (0,0,0), font=font)
    # img_resized = image.resize((188,45), Image.ANTIALIAS)
        save_location = os.getcwd() + '/{}'.format(font_name)
    # print(save_location)
    # img_resized.save(save_location + '/sample.jpg')
        image.save(save_location + '/sample.png')
#===========================================================
for idx in range(44032, 55204): # all data ('가'부터 '힣'까지)
    txt = chr(idx)
    saved_file_name = txt
    font = ImageFont.truetype(font_dir, fontsize)
    image = Image.new('RGBA', (W, H), background)
    draw = ImageDraw.Draw(image)
# w, h = draw.textsize(txt) # not that accurate in getting font size
    w, h = font.getsize(txt)
    draw.text(((W-w)/2,(H-h)/2), txt, fill='black', font=font)
# draw.text((10, 0), txt, (0,0,0), font=font)
# img_resized = image.resize((188,45), Image.ANTIALIAS)
    save_location = os.getcwd() + '/{}'.format(font_name)
# print(save_location)
# img_resized.save(save_location + '/sample.jpg')
    image.save(save_location + '/{}.png'.format(saved_file_name))