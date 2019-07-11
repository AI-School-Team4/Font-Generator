import os
from PIL import Image, ImageDraw, ImageFont

# make sure you have the fonts locally in a fonts/ directory
#===========================================================
# directory for Windows :D
use_path_list = False
if use_path_list:
    path = "C:/WINDOWS/Fonts/{}.{}"
    font_id_ttf = ['HMFMPYUN']
    font_id_ttc = ['BATANG']
    font_name_ttf = ['휴먼필기체'] # 순서 맞춰서
    font_name_ttc = ['바탕']
    font_dir_list = [path.format(iD, "ttf") if iD in font_id_ttf else path.format(iD, "ttc") for iD in font_id_ttf + font_id_ttc]
    font_name_ = font_name_ttf + font_name_ttc
elif not use_path_list:
    # font_dir = 'C:/WINDOWS/Fonts/HMFMPYUN.ttf' # .ttf file
    font_dir = 'C:/WINDOWS/Fonts/BATANG.ttc' # .ttc file
    font_name = '바탕' # font_name으로 해당 폰트의 이미지 파일 디렉토리 생성
    font_dir_list = [font_dir]
    font_name_ = [font_name]
#===========================================================
W, H = (200, 200) # image size (width, height)
background = (255,255,255) # white / dataset background
background2 = (0, 164, 201) # light blue / sample background
fontsize = 100
# on (True) / off (False)
create_sample = True
create_all = True
create_alphabet = True
#===========================================================
for ii, font_dir in enumerate(font_dir_list):
    font_name = font_name_[ii]
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
    if create_all:
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
    #===========================================================
    if create_alphabet:
        for idx in range(12593, 12644): # 자음 모음
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