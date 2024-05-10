import os
import re
import sys
import datetime

def rename_files(directory, pattern):
    # Get the list of files in the specified directory
    files = os.listdir(directory)
    
    # Determine the current date
    current_date = datetime.datetime.now().strftime('%Y%m%d')

    # Counter for appending to file names
    counter = 1

    # Iterate over each file
    for file_name in files:
        # Get the file extension
        extension = os.path.splitext(file_name)[1]

        # Generate a new file name according to the pattern
        new_name = pattern.format(date=current_date, counter=counter, extension=extension)

        # Construct full paths to the files
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)

        # Check if a file with the same name already exists
        if os.path.exists(new_path):
            print(f"File '{new_name}' already exists.")
        else:
            # Rename the file
            os.rename(old_path, new_path)
            print(f"File '{file_name}' renamed to '{new_name}'.")

        # Increment the counter
        counter += 1

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <pattern>")
        sys.exit(1)

    # Get the command line arguments
    directory = sys.argv[1]
    pattern = sys.argv[2] + "{extension}"

    # Check if the specified directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        sys.exit(1)

    # Call the function to rename files
    rename_files(directory, pattern)
