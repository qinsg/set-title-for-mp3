# set title for mp3 file
import os
import sys
from mutagen.id3 import ID3
from mutagen.id3 import TIT2

def set_title_by_dir(dir):
    f = os.listdir(dir)
    for filename in f:
        if os.path.splitext(filename)[1] == ".mp3":
            filepath = dir + ("" if dir.endswith("/") else "/") + filename
            title = os.path.splitext(filename)[0]
            set_title_by_file(filepath, title)

def set_title_by_file(filename, title=""):
    if title == "":
        title = os.path.splitext(os.path.basename(filename))[0]
    audio = ID3(filename)
    audio["TIT2"] = TIT2(text=title)
    audio.save()
    print(filename + ": success")


if __name__ == '__main__':
    argsnum = len(sys.argv)

    if argsnum == 1:
        print("Usage: python main.py [dir|filename] [title]")
        print("Example:")
        print("python main.py /path/to/dir                  # set title for all mp3 files in the directory by filename")
        print("python main.py /path/to/file.mp3             # set title for the mp3 file by filename")
        print("python main.py /path/to/file.mp3 'my title'  # set title for the mp3 file by title")
        sys.exit()
    else:
        dir = sys.argv[1]
        
        ## if dir is directory, get the list of files in the directory
        if os.path.isdir(dir):
            set_title_by_dir(dir)
        else:
            # if filename is provided, set the title for the mp3 file
            if argsnum == 3:
                title = sys.argv[2]
            else:
                title = ""
            set_title_by_file(dir, title)
