import re

def delete_special_characters(sentence) :
    match_exp = r'[^A-Za-z0-9 ]'
    special_symbols = re.findall(match_exp,sentence)
    for symbol in special_symbols :
        sentence_without_special_symbols = sentence.replace(symbol,'')
        sentence = sentence_without_special_symbols
    return sentence_without_special_symbols