'''
Program to convert all SVG files in the current folder to PNG.

Bug: drawing must be within page boundaries
'''

from os import walk
import subprocess

# put all filenames in the current directory in the variable filenames
for (dirpath, dirnames, filenames) in walk("."):
    break

# convert each file in filenames from svg to png
for file in filenames:
    if file.endswith("svg"):
        subprocess.Popen(['C:\\Program Files (x86)\\Inkscape\\Inkscape.exe', "-w1024 --export-area-drawing -f", file, "-e", file[:-4] + ".png"])

