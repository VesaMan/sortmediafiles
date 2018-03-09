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

def main():
    files = glob.glob("*.m4a")
    print("Current folder contains these .m4a files")
    print(files)
    tag = TinyTag.get('Bingo.m4a')
    print('This track is by %s.' %tag.artist)
    print('The bitrate is %s.' %tag.bitrate)
    os.rename("Bingo.m4a", "96 and less/Bingo.m4a")


if __name__ == "__main__":
    init()
