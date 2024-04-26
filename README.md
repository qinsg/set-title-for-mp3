# set-title-for-mp3
A simple python script to set the title for mp3 file

## Usage

Usage: python main.py [dir]
if dir is not provided, the current directory will be used.

```sh
python main.py
python main.py dir
```

## FAQ

1. You get an error "ModuleNotFoundError: No module named 'mutagen'":

You need mutagen module. Please install:
```sh
pip install mutagen
```