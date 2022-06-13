import cv2
import numpy as np
import random
import os
import common

video = "videos/AI.mp4"

if not os.path.isdir(common.dir_images_sans_panneaux):
    os.mkdir(common.dir_images_sans_panneaux)

if not os.path.exists(video):
    print("Vidéo non présente:", video)
    quit()

cap = cv2.VideoCapture(video)

id = 0
nbr_image = 100000

nbr_image_par_frame = int(100000 / cap.get(cv2.CAP_PROP_FRAME_COUNT)) + 1

while True:
    ret, frame = cap.read()
    if ret is False:
        quit()
    h, w, c = frame.shape

    for cpt in range(nbr_image_par_frame):
        x = random.randint(0, w - common.size)
        y = random.randint(0, h - common.size)
        img = frame[y:y + common.size, x:x + common.size]
        cv2.imwrite(common.dir_images_sans_panneaux + "/{:d}.png".format(id), img)
        id += 1
        if id == nbr_image:
            quit()