sortmediafiles
=======

This program will sort audio files to directories based on their bit rate.

Requirements:

 - [tinytag](https://github.com/devsnd/tinytag) 0.18.0 or up
 - Python 3.6 (tested)

Usage:

 1. place in the directory where audio files are located

 1.1 make sure you have the rights to make folders and move audio files in said directory

 2. run sort.py in command-line or Python IDLE environment

Changelog:

* 0.06 (2018/03/22): User now gets info about how many files were sorted + files that weren't sorted
* 0.05 (2018/03/22): Tell user when a file doesn't meet defined bit rate requirements
* 0.04 (2018/03/22): Stricter sorting logic, allows only 2 kbps of deviation from the target bit rate
* 0.03 (2018/03/12): Inform the user more about current situation and don't run init() if list is empty
* 0.02 (2018/03/12): If file list is empty, don't progress to sorting
* 0.01 (2018/03/11): Initial release
