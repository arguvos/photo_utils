# photo_utils
As an enthusiast of film photography, my repository serves as a collection of various utilities tailored for manipulating photographs. The process of working with film comprises several crucial steps: exposure, development, and scanning. Following the exposure phase, the film undergoes development and subsequent scanning in the laboratory. Typically, laboratories employ standard settings for scanning, resulting in raw photographs that necessitate refinement.

# histogram.py
A vital step in post-processing involves histogram equalization, a technique I regularly apply to each photograph. Histogram equalization is an image processing method designed to enrich contrast by fine-tuning the intensity distribution. To simplify and automate this process, I created a tool called histogram.py.

This program facilitates histogram equalization on images sourced from a designated directory. It offers support for both RGB and HSV color spaces, enabling versatile equalization options. For every image processed, the program generates a window showcasing the original and adjusted images, alongside their respective histograms.

![Image](img/img.png?raw=true)

## Dependencies
The utilities in this repository depend on the following libraries:
- OpenCV
- Matplotlib

To install the required libraries, run the following command:
```bash
pip install opencv-python matplotlib
```

## Usage
To use the histogram.py utility, run the following command:
```bash
python histogram.py path/to/image.jpg
```
To use the program, run it from the command line with the following syntax:
```bash
python histogram.py <path_to_images_directory> <color_space>
```
Where:
- <path_to_images_directory>: Path to the directory containing images.
- <color_space>: Specify 'rgb' or 'hsv' for histogram equalization color space.

Example:
```bash
python histogram.py ./images/ rgb
```
This command will process images located in the ./images/ directory using RGB histogram equalization.

## Notes:
- Supported image formats: JPEG (.jpg).
- The program will save the equalized images in the same directory with a prefix 'out_' added to the original file name.

# rename_files.py
This Python script renames all files in a specified directory according to a given pattern.

## Usage:
```bash
python rename_files.py <directory> <pattern>
```
Where:
- <directory>: The path to the directory where file renaming will be performed.
- <pattern>: The renaming pattern to be applied to the files. The pattern can contain placeholders:
  - {date}: Current date in the format YYYYMMDD.
  - {counter}: Counter for appending to file names.

Example:
```bash
python rename_files.py /path/to/directory "{date}_{counter}_qwertylab"
```
This command will rename all files in the specified directory according to the provided pattern.

## Note:
- Make sure to enclose the pattern in double quotes.
- The script preserves the original file extension.
- If a file with the new name already exists, it will not be renamed.