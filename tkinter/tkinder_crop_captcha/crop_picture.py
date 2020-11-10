from PIL import Image



def resimKirp(resim_adi):
    img = Image.open(resim_adi)
    aa = (62, 210, 280, 265)
    crop_img = img.crop(aa)
    crop_img.load()
    crop_img.save(".\\tmp\cropped.png")

resimKirp(".\\tmp\captcha.png")