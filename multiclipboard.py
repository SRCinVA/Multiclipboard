import sys
import clipboard
import json

# clipboard.copy("abc")
# data = clipboard.paste()
# print(data)    

if len(sys.argv) == 2:
    command = sys.argv[1] # to pull out the first index in the list
    print(command)
