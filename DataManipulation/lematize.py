import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Create a spaCy Doc object
doc = nlp("Kevin Zheng is the best Coder in the whole world")

for ent in doc.ents:
    print(ent.text,ent.label)
# Lemmatize the text
lemmas = [token.lemma_ for token in doc]

print(lemmas)
