import pandas as pd
import glob
import os
from natsort import natsorted

# The path of the file containing the list of image file paths
csvfile = 'fileName.csv'

# The directory containing the image files
img_dir = 'FileDirectory/no cracks RGB images'

# Get the file paths of all the images in the directory and sort them naturally
img_paths = natsorted(glob.glob(os.path.join(img_dir, '*.png')))

# Create a DataFrame of the sorted image file paths
df = pd.DataFrame({'path': img_paths})

# Save the DataFrame to a CSV file
df.to_csv(csvfile, index=False)

# Read the image file paths from the CSV file
df = pd.read_csv(csvfile)
print(df)
