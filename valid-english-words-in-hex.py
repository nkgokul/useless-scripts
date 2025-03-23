# Example using the 'english-words' package
#!pip install english-words

from english_words import get_english_words_set
#web2lowerset = get_english_words_set(['web2'], lower=True)
english_words = get_english_words_set(['web2'], lower=True)

allowed_letters = set("abcdef")
valid_words = [word for word in english_words if set(word.lower()).issubset(allowed_letters)]
valid_words = sorted(valid_words)

print(f"Found {len(valid_words)} valid words. Some examples:")
print(valid_words)
#print(valid_words[:100])
