import cv2
import matplotlib.pyplot as plt
import os
import sys


def rgb_equalized(image):
    channels = cv2.split(image)
    eq_channels = []
    for ch, color in zip(channels, ['b', 'g', 'r']):
        eq_channels.append(cv2.equalizeHist(ch))
    return cv2.merge(eq_channels)


def hsv_equalized(image):
    h, s, v = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    eq_v = cv2.equalizeHist(v)
    return cv2.cvtColor(cv2.merge([h, s, eq_v]), cv2.COLOR_HSV2RGB)


def hide_axis(axis):
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)


def draw_histogram(image, axis):
    channels = ('b', 'g', 'r')
    for i, color in enumerate(channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        axis.plot(histogram, color=color)
        hide_axis(axis)


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
        # Initialise the subplot function using number of rows and columns
        figure, axis = plt.subplots(2, 2)
        if os.path.isfile(full_file_name):
            print(full_file_name)
            image = cv2.imread(full_file_name)

            # Show original image
            hide_axis(axis[0, 0])
            axis[0, 0].set_title("Original")
            axis[0, 0].imshow(image)
            # Show histogram of original image
            draw_histogram(image, axis[1, 0])
            axis[1, 0].set_title("Original Histogram")

            if sys.argv[2] == 'rgb':
                image = rgb_equalized(image)
            else:
                image = hsv_equalized(image)

            # Show equalized image
            hide_axis(axis[0, 1])
            axis[0, 1].imshow(image)
            axis[0, 1].set_title("Equalized")
            # Show histogram of equalized image
            draw_histogram(image, axis[1, 1])
            axis[1, 1].set_title("Equalized Histogram")

            plt.show()

            cv2.imwrite(dir_path + "out_" + file_name, image)


if __name__ == '__main__':
    main()