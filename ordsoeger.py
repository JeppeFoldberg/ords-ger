import re
import regex
import sys

def søgestreng():
    '''
    Tager søgestreng fra input og laver regex input der kan bruges til at søge i ordene
    '''
    # tager det første argument til programmet - søgestrengen
    søgestreng = sys.argv[1]

    # print(f'{sys.argv[1]}, {sys.argv[2]}')

    # opdaterer pattern så vi bruger den nye word operator - det sikrer at vi fjerne de bogstaver vi har prøvet 
    # hvis der ikke er nogle bogstaver vi har prøvet så kan vi bare bruge \w i søgningen
    if len(sys.argv) == 3:
        søgestreng = re.sub('_', f'[^{sys.argv[2]}]', søgestreng)
        # word_operator = f'[^{sys.argv[2]}]'
    else:
        # der er noget galt med regex her - for nu må man skrive \w når man kalder programmet?
        søgestreng = re.sub('_', r'\\w', søgestreng)
        # søgestreng = søgestreng.replace('_', r'\w')

        # pass

    print(f'{søgestreng}')
    # print(f'{type(sys.argv[1])}, {sys.argv=}')

    return søgestreng

def search(pattern: str, wordlist: str = "alle_ord_clean_n5.txt"): 
    with open(wordlist) as f:
        matches = re.findall(pattern, f.read()) 

    return matches

def main():
    if len(sys.argv) < 2:
        raise SystemExit(f"Usage: {sys.argv[0]} <search_pattern> <excluded_letters_optional>")

    # pattern = søgestreng()
    print(search(søgestreng()))

if __name__ == "__main__":
   main()