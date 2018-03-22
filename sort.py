#!/usr/bin/env python
"""
sort.py, by Vesa Mäntysaari - 2018/03/22
This program will sort audio files to directories based on their bit rate.
"""
from tinytag import *
import glob
import os

def init():
    #Check if folders already exist, if not create them
    newpath = r'96/'
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

def sortFiles(list):
    #sort files in list
    for file in list:
        tag = TinyTag.get(file)
        if 318 <= tag.bitrate <= 322:
            os.rename(file, "320/"+file)
        elif 254 <= tag.bitrate <= 258:
            os.rename(file, "256/"+file)
        elif 222 <= tag.bitrate <= 226:
            os.rename(file, "224/"+file)
        elif 190 <= tag.bitrate <= 194:
            os.rename(file, "192/"+file)
        elif 158 <= tag.bitrate <= 162:
            os.rename(file, "160/"+file)
        elif 126 <= tag.bitrate <= 130:
            os.rename(file, "128/"+file)
        elif 110 <= tag.bitrate <= 114:
            os.rename(file, "112/"+file)
        elif 94 <= tag.bitrate <= 98:
            os.rename(file, "96/"+file)
        else:
            print(file, " didn't meet any of the requirements and wasn't moved.")

def main():
    print("sortmediafiles v. 0.05\n-----------------------\n")
    files = glob.glob("*.m4a") #get specified files in current folder, supports multiple media extensions
    if not files: #if list is empty
        print("Current directory doesn't contain any files with the specified extension")
        print("Stopping sortmediafiles")
    if files: #if list has data
        init()
        print("Sorting the following files:\n")
        for file in files:
            print(file)
        sortFiles(files)

if __name__ == "__main__":
    main()
