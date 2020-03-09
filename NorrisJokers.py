'''
File: Week 10 Assignment: Exceptions and Testing.ipynb
Name: Jonathan Lawrence
Date: 2/08/2019
Course DSC510 - Intro to Programming
Desc: This program will use an open API to obtain data for the end user.
'''

import requests
import json

def main():
    firstWelcome = input("Welcome! Would you like to hear a Chuck Norris joke?\n'Y' = Yes\n'N' = No.\n\n")
    if firstWelcome == "Y":
        firstJoke()
        nextJoke()
    elif firstWelcome =="N":
        print("Goodbye!")
    else:
        print("\nERROR: PLEASE ENTER ONLY 'Y' OR 'N'!\n")
        main()
    return

def firstJoke():
    # sending get request and saving the response as response object
    response = requests.get("https://api.chucknorris.io/jokes/random")
    # 200 -- everything went okay, and the result has been returned (if any)
    #print("Response code: {}".format(response.status_code))

    # Print the content of the response (the data the server returned)
    itemized_bytes = response.content
    #print("\nContent: {}\n\n{}".format(type(itemized_bytes), itemized_bytes))

    # Get the response data as a python object.  Verify that it's a dictionary.
    itemized_json = response.json()
    #print("\nContent: {}\n\n{}".format(type(itemized_json), itemized_json))

    # dumps -- Takes in a Python object, and converts it to a string.
    itemized_json_string = json.dumps(itemized_json)
    #print("\nContent (string):\n\n{}".format(itemized_json_string))

    # loads -- Takes a JSON string, and converts it to a Python object.
    d = json.loads(itemized_json_string)
    print("\n")
    print("*"*(len(d["value"])+2))
    print("{}{}{}".format("*",d["value"],"*"))
    print("*"*(len(d["value"])+2))
    print("\n")

    #for eachItem in d.items():
    #    print(eachItem)
    return

def nextJoke():
    nextWelcome = input("Would you like to hear another joke?\n'Y' = Yes\n'N' = No.\n\n")
    if nextWelcome == "Y":
        firstJoke()
        nextJoke()
    elif nextWelcome =="N":
        print("Goodbye!")
    else:
        print("\nERROR: PLEASE ENTER ONLY 'Y' OR 'N'!\n")
        nextJoke()
    return

main()
