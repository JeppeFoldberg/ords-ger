import re

with open('alle_ord.txt') as f:
    lines = f.read()

def search(pattern: str, wordlist: str = "alle_ord_clean_n5.txt"): 
    with open(wordlist) as f:
        matches = re.findall(pattern, f.read()) 
    return matches

def main():
    print(search(r"\wi\wo\w"))

if __name__ == "__main__":
   main()