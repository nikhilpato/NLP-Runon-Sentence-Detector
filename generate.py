import nltk
import json
import random
import collections


# Remove random amount of commas from sentence
def remove_comma(sentence):
    counts = collections.Counter(sentence)
    num_commas = counts[',']
    return sentence.replace(',', '', random.randint(1, num_commas))

with open("tai-documents-v3.json") as json_file:
    data = json.load(json_file)

nltk.download('punkt')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

for document in data:
    essay = document['plaintext']
    raw_paragraphs = [p.strip() for p in essay.split("\n\n")]
    for p in raw_paragraphs:
        sents = sent_tokenizer.tokenize(p)
        for sent in sents:
            if ',' in sent:
                invalid = remove_comma(sent)
                print(invalid)


