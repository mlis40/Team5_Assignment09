# main.py
# Name: Matthew Lisowsky, Harrison Moore, Maddy Wogomon
# email: lisowsmd@mail.uc.edu, wogomomr@mail.uc.edu, moorehc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/04/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Citations:
# Anything else that's relevant:

# imports (ex: from functionPackage.functions import *)
import json
import requests
'''
import dataClassPackage.dataClass import iterate_dictionary
'''

if __name__ == "__main__": 
    '''
    I added the API string to the correct location just make sure thats the right one
    I also added the iterate function in the dataClass package
    We are going to have to change the info that we want to pull which should go where the total and for statement is at
    Additionally we will need to use the iterate function then we can use that import statement from above
    Harrison can you look at the API like and write a comment above that u worked on the API stuff
    Maddy can you try an work out what info we want to pull from the API
    '''
    response = requests.get('https://pokeapi.co/api/v2/pokemon-species/appletun')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    
    total = int(parsed_json['total']) # The number of parks that were returned
    
    for park in parsed_json['data']:
        print (park)
