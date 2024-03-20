import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def rgb_equalized(image):
    channels = cv2.split(image)
    eq_channels = []
    for ch, color in zip(channels, ['B', 'G', 'R']):
        eq_channels.append(cv2.equalizeHist(ch))
    return cv2.merge(eq_channels)


def hsv_equalized(image):
    h, s, v = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    eq_v = cv2.equalizeHist(v)
    return cv2.cvtColor(cv2.merge([h, s, eq_v]), cv2.COLOR_HSV2RGB)


def main():
    if len(sys.argv) != 3 and (sys.argv[2] != 'rgb' or sys.argv[2] != 'hsv'):
        print("ERROR: Util expected two arguments: <path to images> <rgb or hsv>")

    dir_path = sys.argv[1]
    print("Files and directories in '", dir_path, "':")
    dir_list = os.listdir(dir_path)
    print(dir_list)

    # Iterate directory
    for file_name in os.listdir(dir_path):
        # check if current file_name is a image file
        if 'jpg' not in file_name:
            print("Skip file: ", file_name)
            continue
        full_file_name = os.path.join(dir_path, file_name)
        if os.path.isfile(full_file_name):
            print(full_file_name)
            image = cv2.imread(full_file_name)
            if sys.argv[2] == 'rgb':
                image = rgb_equalized(image)
            else:
                image = hsv_equalized(image)
            cv2.imwrite(dir_path + "out_" + file_name, image)


if __name__ == '__main__':
    main()