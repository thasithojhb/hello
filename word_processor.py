from functools import reduce

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

def convert_to_word_list(text):
    """
    Converts a string into lower case and into a list through removing delimiters present
    :param text: string to be converted
    :rerurn: a list of word converted
    """
    delimiters = [' ',',','.',',','?',';']
    
    list_words = list(filter(lambda  x: x != '', split(delimiters,text.lower())))
    return list_words

def words_longer_than(length, text):
    """
    Filters a list of words based of the length provided
    :param lenght: an int representing lenght of words to be filtered 
    :param text: string to be converted
    :rerurn: a list of filtered words
    """
    delimiters = [' ',',','.',',','?',';']

    list_words = list(filter(lambda  x: x != '', split(delimiters,text.lower())))
    filter_words = [x for x in list_words if len(x) > length]
    return filter_words
   

def words_lengths_map(text):
    """
    Converts a string into a dictionary show how many words occur of each length of word
    :param text: string to be converted
    :rerurn: a dictionary
    """


    delimiters = [' ',',','.',',','?',';']

    list_words = list(filter(lambda  x: x != '', split(delimiters,text.lower())))    
    words_length = [len(x) for x in [x for x in list_words]]
    words_lengths_map = {x: words_length.count(x) for x in words_length}
    return words_lengths_map
    
def letters_count_map(text):
    """
    Converts a string into a dictionary of letters and there corresponding occurence in a string
    :param text: string to be converted
    :rerurn: a dictionary
    """

    delimiters = [' ',',','.',',','?',';']
    
    str_ = ''.join(list(filter(lambda  x: x != '', split(delimiters,text.lower()))))
    count_map = {chr(x):str_.count(chr(x)) for x in range(97,123)}
    return count_map

def most_used_character(text):
    """
    Checks for the most used letter in a string
    :param text: string to be converted
    :rerurn: a string of the most used letter
    """

    s = letters_count_map(text)
    character = None
    if len([key  for (key,value) in s.items() if value != 0]) > 0:
        val = reduce(max,[value for (key,value) in s.items()])
        character = [key  for (key,value) in s.items() if value == val][0]
    return character

