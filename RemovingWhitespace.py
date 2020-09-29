#-------------------------------------------------------------------------------|
#   Title:          RemovingWhitespace                                          |
#   Author:         Drake G. Cummings                                           |
#   Purpose:        Remove all the spaces from a file                           |
#-------------------------------------------------------------------------------|
#   Started:        September 27th, 2020                                        |
#   Last Updated:   September 29th, 2020                                        |
#   Condition:      Working                                                     |
#-------------------------------------------------------------------------------|
#   Time Spent Programming: 0 hour(s) 28 minute(s) 20 second(s)                 |
#-------------------------------------------------------------------------------|



# Get a correct filename
print()
fileDoesntExist = True
while fileDoesntExist:
    # Ask the user for the file name
    fileName = input("Remove all the whitespace from what file?\n")

    # Try to open the file
    try:
        file = open(fileName, 'r')
    except FileNotFoundError:
        print("File not found.")
        print()
        # return to beginning of loop
        continue

    # Exit while loop
    fileDoesntExist = False


# Update the user
print()
print("File successfully found...")
print("Removing whitespace...")


# Add each character in the file to a string
writing = ""
for x in file:
    writing += x


# Create a new string, this time ignoring whitespace
writingWithSpacesRemoved = ""
for x in writing:
    if (x != ' ' and
        x != '\n'):
        writingWithSpacesRemoved += x


# Write the editted content to a new file
newFileName = "New" + fileName
newFile     = open(newFileName, 'w')
newFile.write(writingWithSpacesRemoved)
newFile.close()


# Update the user
print("Complete.")
print()
print(f"New file is {newFileName}")
