AsciiDict = {}

for letter in range(ord('a'), ord('z') + 1):
    # Add the key-value pair to the dictionary
    AsciiDict[chr(letter)] = letter

print(AsciiDict)
