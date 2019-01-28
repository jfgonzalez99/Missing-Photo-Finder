from os import listdir

folder = "Europe"

# Removes .arw and .jpg extensions from file names
def removeExtensions(files):
    files = [file[:-4] for file in files]
    return(files)

# Compile all the raw photo file names
raw_files = listdir("/Users/jgratata/Desktop/" + folder)
raw_files = removeExtensions(raw_files)

# Compile all file names of the photos already converted to jpg
jpg_files = listdir("/Users/jgratata/Desktop/" + folder + "/JPEG")
jpg_files = removeExtensions(jpg_files)

# print(raw_files)
# print(jpg_files)

# Check for raw files without jpgs
missing_files = set(raw_files) - set(jpg_files)
print(missing_files)
