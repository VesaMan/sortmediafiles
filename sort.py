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
    count = 0
    skipped = 0
    for file in list: #sort files in list
        tag = TinyTag.get(file)
        if 318 <= tag.bitrate <= 322:
            os.rename(file, "320/"+file)
            count = count + 1
        elif 254 <= tag.bitrate <= 258:
            os.rename(file, "256/"+file)
            count = count + 1
        elif 222 <= tag.bitrate <= 226:
            os.rename(file, "224/"+file)
            count = count + 1
        elif 190 <= tag.bitrate <= 194:
            os.rename(file, "192/"+file)
            count = count + 1
        elif 158 <= tag.bitrate <= 162:
            os.rename(file, "160/"+file)
            count = count + 1
        elif 126 <= tag.bitrate <= 130:
            os.rename(file, "128/"+file)
            count = count + 1
        elif 110 <= tag.bitrate <= 114:
            os.rename(file, "112/"+file)
            count = count + 1
        elif 94 <= tag.bitrate <= 98:
            os.rename(file, "96/"+file)
            count = count + 1
        else:
            print(file, " didn't meet any of the requirements and wasn't moved.")
            skipped = skipped + 1
    return(count, skipped)

def main():
    print("sortmediafiles v. 0.06\n-----------------------\n")
    files = glob.glob("*.m4a") #get specified files in current folder, supports multiple media extensions
    if not files: #if list is empty
        print("Current directory doesn't contain any files with the specified extension")
        print("Stopping sortmediafiles")
    if files: #if list has data
        init()
        count, skipped = sortFiles(files)
        print(count, " files sorted.")
        print(skipped, " files didn't meet any of the requirements.")

if __name__ == "__main__":
    main()
