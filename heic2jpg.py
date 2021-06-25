#By Nyrroz
#Simple HEIC to JPG (or other format supported by wand) converter

from wand.image import Image

SourceFile= "IMG_3265.HEIC"
TargetFile= "IMG_3265.JPG"

img=Image(filename=SourceFile)
img.format='jpg'
img.save(filename=TargetFile)
img.close()