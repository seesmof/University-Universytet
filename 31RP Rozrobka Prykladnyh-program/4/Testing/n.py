import nltk
request='admin'
words=nltk.word_tokenize(request)
text=nltk.Text(words)
vocab=text.vocab()
print(len(vocab))