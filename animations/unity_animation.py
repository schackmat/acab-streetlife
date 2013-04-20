#!/usr/bin/env python

import Image
import time
import os
import sys
from acabsl import *

FALLBACK = "dance/list"

# config
if len(sys.argv) != 2:
    img_file = FALLBACK
else:
    img_file = sys.argv[1]

img_file = os.path.join(os.path.dirname(__file__), img_file)

if not os.path.isfile(img_file):
    img_file = os.path.join(os.path.dirname(__file__), FALLBACK)

img_dir = os.path.dirname(img_file)

# setup
img = {}
frames = []
with open(img_file) as f:
    for line in f:
        line = line.strip()
        frames.append(line)
        if line not in img:
            img[line] = Image.open(os.path.join(img_dir, line)).getdata()

for wall in range(NOOFWALLS):
    for col in range(WALLSIZEX):
        for row in range(WALLSIZEY):
            send(wall,col,row,0,0,0,0)
update()


def render_frame(data):
    for wall in range(NOOFWALLS):
        for y in range(WALLSIZEY):
            for x in range(WALLSIZEX):
                ptr = x + y * WALLSIZEX
                if type(data[ptr]) == int:
                    send(wall,x,y,data[ptr],data[ptr],data[ptr]);
                else:
                    send(wall,x,y,data[ptr][0],data[ptr][1],data[ptr][2]);
    update()


while True:
    for f in frames:
        render_frame(img[f])
        time.sleep(0.42)
