import spacy
import os
import sys

# change directory to be able import from fileMod
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from urlProcessor.fileMod import FileMod

nlp = spacy.load("en_core_web_sm")

file = open(FileMod().read_file(), encoding="utf8")

doc = nlp(file.read())

#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)