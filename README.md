# Image-File-name-extration-and-save-into-CSV-file

This code reads in a list of image file paths from a directory, sorts them naturally, creates a pandas DataFrame of the sorted image file paths, and saves the DataFrame to a CSV file. Then, it reads in the image file paths from the CSV file and prints the DataFrame.

The glob module is used to retrieve the file paths of all images in the specified directory that have the .png file extension. The natsorted function from the natsort module is used to sort the file paths naturally, so that they are ordered as expected (e.g., image1.png, image2.png, ..., image10.png instead of image1.png, image10.png, ..., image2.png).

A pandas DataFrame is created from the sorted file paths, with the path column containing the file paths. The DataFrame is then saved to a CSV file using the to_csv method.

Finally, the CSV file is read back into a pandas DataFrame using the read_csv function, and the resulting DataFrame is printed to the console.
