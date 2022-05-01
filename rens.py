import pickle
import re

with open('alle_ord.txt') as f:
    lines = f.read()

# print(type(lines), lines[:100])

# multiline flaget gør at ^ og $ gælder for hver ny linje i strengen og ikke bare for start og slut på strengen en gang! 
cleaned_word_list = re.findall(r'^[\d\.\s]*([^;]+);.+$', lines, re.MULTILINE)

# gem liste som pickle - måske ikke så smart til det her! 
# with open('alle_ord_renset.txt', 'wb') as f:
#    pickle.dump(cleaned_word_list, f)

cleaned_word_list_n5 = [word for word in cleaned_word_list if len(word) == 5]

cleaned_words_str = "\n".join(cleaned_word_list_n5)

print(type(cleaned_words_str), len(cleaned_words_str))

with open('alle_ord_clean_n5.txt', 'w') as f:
    f.write(cleaned_words_str)

# cleaned_word_list_n5 = re.findall(r'')
