# set-title-for-mp3
A simple python script to set the title for mp3 file

## Usage

Usage: python main.py [dir|filename] [title]

```sh
python main.py                               # print usage
python main.py /path/to/dir                  # set title for all mp3 files in the directory by filename
python main.py /path/to/file.mp3             # set title for the mp3 file by filename
python main.py /path/to/file.mp3 'my title'  # set title for the mp3 file by title
```

## FAQ

1. You get an error "ModuleNotFoundError: No module named 'mutagen'":

You need mutagen module. Please install:
```sh
pip install mutagen
```