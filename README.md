# Ordsøger

Meget simpel command line ordsøger der kan hjælpe når wordle er lidt for svært. 

Kaldes hangman-style efter denne opskrift 
python ordsoeger.py <search_pattern> <excluded_letters_optional> <included_letters_optional>. 

## eksempel
```
$ python ordsoeger.py ka_de abcd
['kalde', 'kande']
```

## Ting der kan implementeres
- [x] en måde at inkludere de bogstaver der skal være med i ordet
- [ ] en måde at inkludere information om hvor bogstaverne ikke må placeres
