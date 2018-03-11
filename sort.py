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
    main()

def sortFiles(list):
    #sort files in list
    for file in list:
        tag = TinyTag.get(file)
        if 310 <= tag.bitrate <= 320:
            os.rename(file, "320/"+file)
        elif 244 <= tag.bitrate <= 264:
            os.rename(file, "256/"+file)
        elif 216 <= tag.bitrate <= 230:
            os.rename(file, "224/"+file)
        elif 180 <= tag.bitrate <= 196:
            os.rename(file, "192/"+file)
        elif 150 <= tag.bitrate <= 170:
            os.rename(file, "160/"+file)
        elif 120 <= tag.bitrate <= 132:
            os.rename(file, "128/"+file)
        elif 105 <= tag.bitrate <= 115:
            os.rename(file, "112/"+file)
        elif tag.bitrate <= 98:
            os.rename(file, "96 and less/"+file)

def main():
    files = glob.glob("*.m4a") #get specified files in current folder, supports multiple media extensions
    sortFiles(files)

if __name__ == "__main__":
    init()
