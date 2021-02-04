import spacy, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.absolute())) 
from fileMod import FileMod

nlp = spacy.load("en_core_web_sm")

file = open(FileMod().read_file(), encoding="utf8")

doc = nlp(file.read())

#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)