# set title for mp3 file
import os
import sys
from mutagen.id3 import ID3
from mutagen.id3 import TIT2

def set_title_for_mp3(dir):
    f = os.listdir(dir)
    for filename in f:
        if os.path.splitext(filename)[1] == ".mp3":
            filepath = dir + ("" if dir.endswith("/") else "/") + filename
            title = os.path.splitext(filename)[0]
            audio = ID3(filepath)
            audio["TIT2"] = TIT2(text=title)
            audio.save()
            print(filepath + ": success")


if __name__ == '__main__':
    dir = "./"
    if len(sys.argv) == 2:
        dir = sys.argv[1]
    else:
        print("Usage: python main.py [dir]")
        print("if dir is not provided, the current directory will be used.")
        dir = "./"
    set_title_for_mp3(dir)

