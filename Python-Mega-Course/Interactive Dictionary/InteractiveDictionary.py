import json
from difflib import get_close_matches

def load_json(filepath):
    data = json.load(open(filepath,'r'))
    return data

def search_definition(word):
    word = word.lower()
    try:
        return dictionary[word]
    except KeyError:
        try:
            similar_word = get_close_matches(word, dictionary.keys())[0]
            yn = input('Did you mean %s? Type Y for yes, or N for no.\n' % similar_word)
            if yn.upper() == 'Y':
                return dictionary[similar_word]
            else:
                print('No such word. Try again.')
        except:
            print('No such word. Try again.')

def dictionary_standardize_key(old_dictionary):
    standardized_key_dictionary = {x.lower():old_dictionary[x] for x in old_dictionary.keys()}
    return standardized_key_dictionary

def input_word():
    return input('Search for a definition:\n')

def display_definition(definition):
    if definition != None:
        if type(definition) == list:
            for subdef in definition:
                print(subdef)

dictionary = load_json('data.json')
dictionary = dictionary_standardize_key(dictionary)
definition = search_definition(input_word())
display_definition(definition)
