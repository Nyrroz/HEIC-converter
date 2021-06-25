#By Nyrroz
#Simple HEIC to JPG (or other format supported by wand) converter
#This "all" script converts all HEIC files in the parent directory and puts them in an output folder 
#Note: keeps original files

from wand.image import Image
import os

def convert(file, format):
    img=Image(filename=file)
    img.format=format
    output = './output'
    try: 
        if not os.path.exists(output):
            os.makedirs(output)
        img.save(filename= output + '/' + file.replace('.HEIC',f'.{format.upper()}'))
    except:
        img.save(filename= 'converted_' + file.replace('.HEIC',f'.{format.upper()}'))

    img.close()
    print(f"Converted {file} to {format}")

print("HEIC to JPG (or PNG) converter by Nyrroz")
print("Converting all HEIC files in the directory...")
print("Find all converted files inside the 'output' folder")


counter = 0

for file in os.listdir('./'):
    if file.endswith('.HEIC'):
        convert(file, 'jpg')
        counter += 1

print(f"Successfully converted {counter} files")
