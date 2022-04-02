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
    try:  #for when you don't know if something will work
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except: # if the "try" does not work
        return {} # return an empty dictionary

# save_items("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command = sys.argv[1] # to pull out the first index in the list
    data = load_data(SAVED_DATA) # thsi gives us a Python dictionary

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()  # we put whatever key is inputted into the clipbaord.
        save_data(SAVED_DATA, data)  # this will save the dtaa persistently
        print("data saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data: # if we already have the key they;ve typed in ...
            clipboard.copy(data[key])  # we will access the value attached to that key and put it inot their clipboard.
            print("Data copied to clipboard.")
        else:
            print("Key does not exist") # ... in case that key cannot be found
    elif command == "list":
        print(data)  # here, we will simply print out the keys and values in the dictionary.
    else:
        print ("Unknown command")
else:
    print("Please pass exactly one command.")
