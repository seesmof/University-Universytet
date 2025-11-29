import nltk
text='This is an example text of usage of a tokenizer function and then processing those words into parts of speech using a built-in method from a language processing library called nltk for a Python programming language.'
words=nltk.tokenize.word_tokenize(text)
parts_of_speech=nltk.pos_tag(words)
print(parts_of_speech)