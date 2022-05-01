import re
import sys

def søgestreng():
    '''
    Tager søgestreng fra input og laver regex input der kan bruges til at søge i ordene
    '''
    # tager det første argument til programmet - søgestrengen
    søgestreng = sys.argv[1]

    # opdaterer pattern så vi bruger den nye word operator - det sikrer at vi fjerne de bogstaver vi har prøvet 
    # hvis der ikke er nogle bogstaver vi har prøvet så kan vi bare bruge \w i søgningen
    if len(sys.argv) == 3:
        søgestreng = re.sub('_', fr'[^{sys.argv[2]}\\s]', søgestreng)
    else:
        # putter \w ind i søgestrengen - af en eller anden grund skal den escapes to gange! 
        søgestreng = re.sub('_', r'\\w', søgestreng)

    # print(f'{søgestreng=}')

    return søgestreng

def search(pattern: str, wordlist: str = "alle_ord_clean_n5.txt"): 
    with open(wordlist) as f:
        matches = re.findall(pattern, f.read()) 

    return matches

def main():
    if len(sys.argv) < 2:
        raise SystemExit(f"Usage: {sys.argv[0]} <search_pattern> <excluded_letters_optional>")

    print(search(søgestreng()))

if __name__ == "__main__":
   main()