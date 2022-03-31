import sys
import clipboard
import json

# clipboard.copy("abc")
# data = clipboard.paste()
# print(data)    

def save_items(filepath,data):
    with open(filepath, "w") as f:  # this creates or overrides an existing file
        json.dump(data,f)  # this will dump the data "the python dictionary" to the .json object onto the file ("f")

save_items("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command = sys.argv[1] # to pull out the first index in the list
    print(command)

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print ("Unknown command")
else:
    print("Please pass exactly one command.")
