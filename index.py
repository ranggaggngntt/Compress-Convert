
from PIL import Image
from subprocess import Popen
import subprocess
import os
import platform

try:
    from docx2pdf import convert
except Exception:
    print('pip3 install docx2pdf')

current_path = os.getcwd()
output_path = current_path + '/result/'
def convertDoc():
    namefile = input("Nama File (contoh = word.doc) : ")
    if platform.system() == 'Linux':
        LIBRE_OFFICE = r"/usr/bin/libreoffice"

        def convert_to_pdf(input_docx, output):
            p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',output + 'document/', input_docx])
            p.communicate()

        convert_to_pdf(namefile, output_path)
    else:
        convert(namefile, output_path + namefile + '-convert.pdf')


def compressImage():
    namefile = input("Nama File (contoh = background.jpg) : ")
    foo = Image.open(namefile)
    try:
        foo.save(output_path + 'image/' + namefile + '-compress.jpg',optimize=True,quality=75)
    except Exception:
        print('File harus didalam folder Compress-Convert')

def compressVideo():
    namefile = input("Nama Video (contoh = input.mp4) : ")
    subprocess.run('ffmpeg -i ' + namefile + ' -vcodec libx264 -crf 20 -b 800k ' + output_path + 'video/' + namefile + '-compress.mp4', shell=True)

if __name__ == "__main__":
    print(' 1. Compress Image (Resize Image)')
    print(' 2. Convert Word to Pdf')
    print(' 3. Compress Video')
    inp = int(input(" Pilih angka : "))
    if inp == 1:
        compressImage()
    elif inp == 2:
        convertDoc()
    elif inp == 3:
        compressVideo()
    else:
        print('nomor hanya 1-3')