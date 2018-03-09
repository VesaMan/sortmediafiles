#!/usr/bin/env python
"""sort.py, by Vesa Mäntysaari, 2018-03-09
This program will sort media files to directories based on their bitrate.
"""
from tinytag import *
import glob
import os

def init():
    #Check if folders already exist, if not create them
    newpath = r'96 and less/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'112/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'128/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'160/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'192/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'224/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'256/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'320/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    #Call main function
    main()

def sortFiles():
    tag = TinyTag.get('Bingo.m4a')
    if 300 <= tag.bitrate <= 320:
        os.rename("Bingo.m4a", "320/Bingo.m4a")
    elif 240 <= tag.bitrate <= 264:
        os.rename("Bingo.m4a", "256/Bingo.m4a")
    elif 200 <= tag.bitrate <= 230:
        os.rename("Bingo.m4a", "224/Bingo.m4a")
    elif 180 <= tag.bitrate <= 198:
        os.rename("Bingo.m4a", "192/Bingo.m4a")
    elif 150 <= tag.bitrate <= 170:
        os.rename("Bingo.m4a", "160/Bingo.m4a")
    elif 120 <= tag.bitrate <= 140:
        os.rename("Bingo.m4a", "128/Bingo.m4a")
    elif 100 <= tag.bitrate <= 118:
        os.rename("Bingo.m4a", "112/Bingo.m4a")
    elif tag.bitrate <= 98:
        os.rename("Bingo.m4a", "96 and less/Bingo.m4a")


def main():
    files = glob.glob("*.m4a")
    print("Current folder contains these .m4a files")
    print(files)
    sortFiles()

if __name__ == "__main__":
    init()
