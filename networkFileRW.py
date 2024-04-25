#!/usr/bin/env python3
#networkFileRW.py
#Pamela Brauda
#Thursday, March 3, 2022
#Update routers and switches
#read equipment from a file, write updates & errors to file

##---->>>> Use a try/except clause to import the JSON module
try:
    import json
except ImportError:
    print("Error: JSON module not found.")


##---->>>> Create file constants for the file names; file constants can be reused
##         There are 2 files to read this program: equip_r.txt and equip_s.txt
##         There are 2 files to write in this program: updated.txt and errors.txt
      
EQUIP_R_FILE = "equip_r.txt"
EQUIP_S_FILE = "equip_s.txt"
UPDATED_FILE = "updated.txt"
ERRORS_FILE = "errors.txt"


#prompt constants
UPDATE = "\nWhich device would you like to update "
QUIT = "(enter x to quit)? "
NEW_IP = "What is the new IP address (111.111.111.111) "
SORRY = "Sorry, that is not a valid IP address\n"

#function to get valid device
def getValidDevice(routers, switches):
    validDevice = False
    while not validDevice:
        #prompt for device to update
        device = input(UPDATE + QUIT).lower()
        if device in routers.keys():
            return device
        elif device in switches.keys():
            return device
        elif device == 'x':
            return device  
        else:
            print("That device is not in the network inventory.")

# Dictionaries
routers = {'R1': '10.10.10.1', 'R2': '20.20.20.1', 'R3': '30.30.30.1'}
switches = {'S1': '10.10.10.2', 'S2': '10.10.10.3', 'S3': '10.10.10.4', 'S4': '10.10.10.5',
            'S5': '20.20.20.2', 'S6': '20.20.20.3', 'S7': '30.30.30.2', 'S8': '30.30.30.3', 'S9': '30.30.30.4'}

#function to get valid IP address
def getValidIP(invalidIPCount, invalidIPAddresses):
    validIP = False
    while not validIP:
        ipAddress = input(NEW_IP)
        octets = ipAddress.split('.')
        #print("octets", octets)
        for byte in octets:
            byte = int(byte)
            if byte < 0 or byte > 255:
                invalidIPCount += 1
                invalidIPAddresses.append(ipAddress)
                print(SORRY)
                break
        else:
            #validIP = True
                return ipAddress, invalidIPCount
                #don't need to return invalidIPAddresses list - it's an object
        
def main():
    routers = {}
    switches = {}
    updated = {}
    invalidIPAddresses = []
    devicesUpdatedCount = 0
    invalidIPCount = 0
    quitNow = False

    while not quitNow:
        # Your main logic goes here

    ##---->>>> open files here
        try:
            with open(EQUIP_R_FILE, 'r') as file:
                routers = json.load(file)
                with open(EQUIP_S_FILE, 'r') as file:
                    switches = json.load(file)
        except FileNotFoundError:
            print("One or both of the equipment files not found.")

    #dictionaries
    ##---->>>> read the routers and addresses into the router dictionary
try:
    with open(EQUIP_R_FILE, 'r') as file:
        routers = json.load(file)
except FileNotFoundError:
    print("Router file not found.")


    ##---->>>> read the switches and addresses into the switches dictionary
try:
    with open(EQUIP_S_FILE, 'r') as file:
        switches = json.load(file)
except FileNotFoundError:
    print("Switch file not found.")

    #the updated dictionary holds the device name and new ip address
    updated = {}

    #list of bad addresses entered by the user
    invalidIPAddresses = []

    #accumulator variables
    devicesUpdatedCount = 0
    invalidIPCount = 0

    #flags and sentinels
    quitNow = False
    validIP = False

    print("Network Equipment Inventory\n")
    print("\tequipment name\tIP address")
    for router, ipa in routers.items(): 
        print("\t" + router + "\t\t" + ipa)
    for switch, ipa in switches.items():
        print("\t" + switch + "\t\t" + ipa)

device = None  

while not quitNow:
        #function call to get valid device
    device = getValidDevice(routers, switches)

    if device == 'x':
        quitNow = True
        break


     #function call to get valid IP address
ipAddress, invalidIPCount = getValidIP(invalidIPCount, invalidIPAddresses)

        #python lets you return two or more values at one time

  
       # update device
if 'r' in device:
    # modify the value associated with the key
    routers[device] = ipAddress
else:
    switches[device] = ipAddress

devicesUpdatedCount += 1

        #add the device and ipAddress to the dictionary
updated[device] = ipAddress

print(device, "was updated; the new IP address is", ipAddress)
        #loop back to the beginning
        

    #user finished updating devices
print("\nSummary:")
print()
print("Number of devices updated:", devicesUpdatedCount)

    ##---->>>> write the updated equipment dictionary to a file
try:
        with open(UPDATED_FILE, 'w') as file:
            json.dump(updated, file)
        print("Updated equipment written to file 'updated.txt'")
except Exception as e:
    print("Error occurred while writing updated equipment:", e)

print("\nNumber of invalid addresses attempted:", invalidIPCount)


print("Updated equipment written to file 'updated.txt'")
print()
print("\nNumber of invalid addresses attempted:", invalidIPCount)

    ##---->>>> write the list of invalid addresses to a file
try:
    with open(ERRORS_FILE, 'w') as file:
        json.dump(invalidIPAddresses, file)
    print("List of invalid addresses written to file 'errors.txt'")
except Exception as e:
    print("Error occurred while writing list of invalid addresses:", e)


    print("List of invalid addresses written to file 'errors.txt'")

#top-level scope check
if __name__ == "__main__":
    main()




