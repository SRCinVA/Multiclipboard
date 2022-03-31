import sys
import clipboard
import json

SAVED_DATA = "clipboard.json" # this is where we'll store our data

# clipboard.copy("abc")
# data = clipboard.paste()
# print(data)    

def save_data(filepath,data):
    with open(filepath, "w") as f:  # this creates or overrides an existing file
        json.dump(data,f)  # this will dump the data "the python dictionary" to the .json object onto the file ("f")

def load_data(filepath):
    with open(filepath,"r") as f:
        data = json.load(f)
        return data

# save_items("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command = sys.argv[1] # to pull out the first index in the list
    data = load_data(SAVED_DATA) # thsi gives us a Python dictionary

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()  # we put whatever key is inputted into the clipbaord.
        save_data(SAVED_DATA, data)  # this will save the dtaa persistently
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print ("Unknown command")
else:
    print("Please pass exactly one command.")
