# main.py
# Name: Matthew Lisowsky, Harrison Moore, Maddy Wogomon
# email: lisowsmd@mail.uc.edu, wogomomr@mail.uc.edu, moorehc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/04/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a program that uses a Pokemon API to pull information from a massive JSON database about Pokemon. We chose to pull info on Maddy's favorite Appletun.
# Citations: https://pokeapi.co/
# Anything else that's relevant: 

# imports (ex: from functionPackage.functions import *)
import json
import requests
'''
import dataClassPackage.dataClass import iterate_dictionary
'''

if __name__ == "__main__": # Entry point
  
    #Harrison found the API and set up to pull information on Appletun
    response = requests.get('https://pokeapi.co/api/v2/pokemon-species/appletun')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    
    #Maddy worked on what info would pulled by the API below
    
    pokemon_name = parsed_json['name'] #Pull and label the Pokemon name
    print(f"Name: {pokemon_name}")
    
    flavor_text_entries = parsed_json['flavor_text_entries'] #Pull and label the Pokemon flavor text
    for entry in flavor_text_entries:
        if entry['language']['name']== 'en': #english
            print(f"Flavor Text (English): {entry['flavor_text']}")
            break
        
    base_happiness = parsed_json['base_happiness'] #Pull and label the Pokemon base happiness
    print(f"Base Happiness: {base_happiness}")
