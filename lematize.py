import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Create a spaCy Doc object
doc = nlp("The striped bats are hanging on their feet for best")

# Lemmatize the text
lemmas = [token.lemma_ for token in doc]

print(lemmas)
