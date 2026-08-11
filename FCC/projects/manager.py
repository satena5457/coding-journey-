"""build a User Configuration Manager that allows users to 
manage their settings such as theme, language, 
and notifications. You will implement functions to 
add, update, delete, and view user settings."""

test_settings = {"Theme": "dark", "Notifications":"enabled", "Volume": "high"}

#Function for adding a new adding setting

def add_setting(Dict, Tup):
    for key in list(Dict.keys()): #Changes the key to lowercase
        Dict[key.lower()] = Dict.pop(key)
    for key in Dict: #Changes the value to lowercase
        Dict[key] = Dict[key].lower()
    key = Tup[0].lower()
    value = Tup[1].lower()
    if key in Dict:  #Checking whether a key exists or not
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else: #If a key is not found, adding the key
        Dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
  
#Function for updating the existing setting   
    
def update_setting(uDict, uTup):
    for key in list(uDict.keys()): #Change keys to lowercase
        uDict[key.lower()] = uDict.pop(key)
    for key in uDict: #Change values to lowercase
        uDict[key] = uDict[key].lower()
    key = uTup[0].lower()
    value = uTup[1].lower()
    if key in uDict: #Checking if the key exists for updating 
        uDict[key] = uTup[1].lower()
        return f"Setting '{key}' updated to '{value}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting." 

# Function for deleting the existing setting 
           
def delete_setting(dDict, dkey):
    for key in list(dDict.keys()): #Change keys to lowercase
        dDict[key.lower()] = dDict.pop(key)
    if dkey in dDict: #Checking whether a key exists inorder to delete 
        del dDict[dkey]
        return f"Setting '{dkey}' deleted successfully!"
    else:
        return f"Setting not found!"  
       
#Function for displaying the key value pair
  
def view_setting(vDict):
    if not vDict: #Checking whether a dictionary is empty or not
    
        return "No settings available."
    else: #If not, displaying the formatted key value pair
         lines = [f"{key.capitalize()}: {value}" for key, value in vDict.items()]
         result = '\n'.join(lines)
         return "Current User Settings:\n" + result
         
print(view_setting(test_settings))
