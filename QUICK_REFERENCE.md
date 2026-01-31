# 📋 spaCy Quick Reference Card

## Installation & Setup

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Loading Models

```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Your text here")
```

---

## Core Objects

### Doc
```python
doc.text          # Original text
doc.ents          # Named entities
doc.sents         # Sentences (generator)
doc.noun_chunks   # Noun phrases (generator)
len(doc)          # Number of tokens
doc[0]            # First token
doc[0:3]          # Span (slice)
doc.vector        # Document vector
```

### Token
```python
token.text        # Original text
token.i           # Index in doc
token.lemma_      # Base form
token.pos_        # Coarse POS tag
token.tag_        # Fine-grained POS tag
token.dep_        # Dependency relation
token.head        # Syntactic head
token.children    # Syntactic children
token.ancestors   # Syntactic ancestors
token.ent_type_   # Entity type (if entity)
token.ent_iob_    # IOB tag (B/I/O)
token.is_alpha    # Is alphabetic?
token.is_punct    # Is punctuation?
token.is_space    # Is whitespace?
token.is_stop     # Is stop word?
token.is_digit    # Is digit?
token.like_num    # Looks like number?
token.like_email  # Looks like email?
token.like_url    # Looks like URL?
token.shape_      # Shape (e.g., Xxxx)
token.vector      # Word vector
token.has_vector  # Has word vector?
```

### Span
```python
span = doc[0:3]
span.text         # Span text
span.start        # Start token index
span.end          # End token index
span.start_char   # Start character index
span.end_char     # End character index
span.label_       # Label (for entities)
span.root         # Root token of span
span.sent         # Sentence containing span
span.vector       # Span vector
```

### Entity
```python
for ent in doc.ents:
    ent.text      # Entity text
    ent.start     # Start token index
    ent.end       # End token index
    ent.label_    # Entity label
    ent.kb_id_    # Knowledge base ID
```

---

## Entity Types

| Type | Description | Example |
|------|-------------|---------|
| `PERSON` | Named person | "Barack Obama" |
| `ORG` | Organization | "Apple Inc." |
| `GPE` | Country/City/State | "France" |
| `LOC` | Non-GPE location | "Mount Everest" |
| `PRODUCT` | Product name | "iPhone" |
| `EVENT` | Named event | "World War II" |
| `WORK_OF_ART` | Work of art | "Mona Lisa" |
| `LAW` | Legal document | "GDPR" |
| `LANGUAGE` | Language | "English" |
| `DATE` | Date/period | "January 2024" |
| `TIME` | Time | "3:00 PM" |
| `PERCENT` | Percentage | "25%" |
| `MONEY` | Monetary value | "$1 million" |
| `QUANTITY` | Measurement | "100 kg" |
| `ORDINAL` | Ordinal | "first" |
| `CARDINAL` | Cardinal number | "100" |
| `FAC` | Facility | "Empire State Building" |
| `NORP` | Nationality/Group | "American" |

---

## POS Tags (Universal)

| Tag | Description | Example |
|-----|-------------|---------|
| `ADJ` | Adjective | "big" |
| `ADP` | Adposition | "in", "to" |
| `ADV` | Adverb | "quickly" |
| `AUX` | Auxiliary verb | "is", "has" |
| `CCONJ` | Coordinating conjunction | "and" |
| `DET` | Determiner | "the", "a" |
| `INTJ` | Interjection | "oh" |
| `NOUN` | Noun | "dog" |
| `NUM` | Numeral | "one", "1" |
| `PART` | Particle | "'s", "not" |
| `PRON` | Pronoun | "he", "she" |
| `PROPN` | Proper noun | "John" |
| `PUNCT` | Punctuation | "." |
| `SCONJ` | Subordinating conjunction | "if" |
| `SYM` | Symbol | "$" |
| `VERB` | Verb | "run" |
| `X` | Other | "etc" |

---

## Dependency Relations (Common)

| Relation | Description | Example |
|----------|-------------|---------|
| `nsubj` | Nominal subject | "John runs" |
| `dobj` | Direct object | "ate pizza" |
| `iobj` | Indirect object | "gave him" |
| `ROOT` | Root of sentence | Main verb |
| `amod` | Adjectival modifier | "red car" |
| `advmod` | Adverbial modifier | "runs quickly" |
| `det` | Determiner | "the dog" |
| `prep` | Prepositional modifier | "in the park" |
| `pobj` | Object of preposition | "in Paris" |
| `compound` | Compound | "apple pie" |
| `punct` | Punctuation | "." |
| `aux` | Auxiliary | "is running" |
| `cc` | Coordinating conjunction | "and" |
| `conj` | Conjunct | "cats and dogs" |

---

## Pattern Matching

### Matcher
```python
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

# Pattern: adjective + noun
pattern = [{"POS": "ADJ"}, {"POS": "NOUN"}]
matcher.add("ADJ_NOUN", [pattern])

matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)
```

### Pattern Operators

| Operator | Meaning |
|----------|---------|
| `{"OP": "!"}` | Negation (token must NOT match) |
| `{"OP": "?"}` | Optional (0 or 1) |
| `{"OP": "+"}` | One or more |
| `{"OP": "*"}` | Zero or more |

### Pattern Attributes

```python
{"TEXT": "apple"}       # Exact text match
{"LOWER": "apple"}      # Lowercase match
{"LEMMA": "be"}         # Lemma match
{"POS": "NOUN"}         # POS tag
{"TAG": "NNS"}          # Fine-grained tag
{"DEP": "nsubj"}        # Dependency
{"ENT_TYPE": "PERSON"}  # Entity type
{"IS_ALPHA": True}      # Is alphabetic
{"IS_DIGIT": True}      # Is digit
{"IS_PUNCT": True}      # Is punctuation
{"SHAPE": "Xxxx"}       # Shape pattern
{"LENGTH": 5}           # Token length
```

### PhraseMatcher
```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(text) for text in ["Google", "Facebook"]]
matcher.add("COMPANIES", patterns)
```

### DependencyMatcher
```python
from spacy.matcher import DependencyMatcher

matcher = DependencyMatcher(nlp.vocab)
pattern = [
    {"RIGHT_ID": "verb", "RIGHT_ATTRS": {"POS": "VERB"}},
    {"LEFT_ID": "verb", "REL_OP": ">", "RIGHT_ID": "subject", 
     "RIGHT_ATTRS": {"DEP": "nsubj"}}
]
matcher.add("VERB_SUBJECT", [pattern])
```

---

## Pipeline Management

```python
# View pipeline components
nlp.pipe_names  # ['tok2vec', 'tagger', 'parser', 'ner', ...]

# Disable components temporarily
with nlp.select_pipes(enable=["tagger"]):
    doc = nlp(text)

# Disable when processing
doc = nlp(text, disable=["parser", "ner"])

# Add component
nlp.add_pipe("my_component", last=True)
nlp.add_pipe("my_component", before="ner")
nlp.add_pipe("my_component", after="tagger")
nlp.add_pipe("my_component", first=True)

# Remove component
nlp.remove_pipe("ner")

# Replace component
nlp.replace_pipe("ner", new_ner)
```

---

## Custom Components

### Simple Component
```python
from spacy.language import Language

@Language.component("my_component")
def my_component(doc):
    # Process doc
    return doc

nlp.add_pipe("my_component", last=True)
```

### Factory Component
```python
@Language.factory("configurable_component", 
                  default_config={"threshold": 0.5})
def create_component(nlp, name, threshold: float):
    return MyComponent(nlp, threshold)
```

---

## Extension Attributes

```python
from spacy.tokens import Doc, Token, Span

# Default attribute
Token.set_extension("is_custom", default=False)

# Getter attribute
def get_is_long(token):
    return len(token.text) > 5
Token.set_extension("is_long", getter=get_is_long)

# Method attribute
def get_similarity(doc, other_doc):
    return doc.vector @ other_doc.vector
Doc.set_extension("custom_similarity", method=get_similarity)

# Usage
token._.is_custom
token._.is_long
doc._.custom_similarity(other_doc)
```

---

## Similarity

```python
# Token similarity
token1.similarity(token2)

# Span similarity  
span1.similarity(span2)

# Doc similarity
doc1.similarity(doc2)

# Check if has vector
token.has_vector
doc.has_vector

# Access vector
token.vector
doc.vector
```

---

## Batch Processing

```python
# Efficient batch processing
texts = ["Text 1", "Text 2", "Text 3"]

# Basic
docs = list(nlp.pipe(texts))

# With batch size
docs = list(nlp.pipe(texts, batch_size=50))

# With multiprocessing
docs = list(nlp.pipe(texts, n_process=4))

# With metadata
data = [("Text 1", {"id": 1}), ("Text 2", {"id": 2})]
for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["id"])
```

---

## Serialization

```python
# Save model
nlp.to_disk("/path/to/model")

# Load model
nlp = spacy.load("/path/to/model")

# Serialize docs with DocBin
from spacy.tokens import DocBin
doc_bin = DocBin()
doc_bin.add(doc)
doc_bin.to_disk("/path/to/docs.spacy")

# Load docs
doc_bin = DocBin().from_disk("/path/to/docs.spacy")
docs = list(doc_bin.get_docs(nlp.vocab))
```

---

## Visualization

```python
from spacy import displacy

# Dependency visualization
displacy.render(doc, style="dep")

# Entity visualization
displacy.render(doc, style="ent")

# Serve in browser
displacy.serve(doc, style="dep", port=5000)

# Save to file
svg = displacy.render(doc, style="ent")
with open("entities.svg", "w", encoding="utf-8") as f:
    f.write(svg)
```

---

## Training (CLI)

```bash
# Create config
python -m spacy init config config.cfg --lang en --pipeline ner

# Fill config
python -m spacy init fill-config base_config.cfg config.cfg

# Train
python -m spacy train config.cfg --output ./output

# Evaluate
python -m spacy evaluate ./model ./test.spacy

# Package model
python -m spacy package ./model ./packages
```

---

## Useful Functions

```python
# Explain annotation
spacy.explain("GPE")  # "Countries, cities, states"
spacy.explain("nsubj")  # "nominal subject"

# Available languages
spacy.util.get_lang_class("en")

# Validate installation
spacy.validate()

# Info about model
spacy.info("en_core_web_sm")
```

---

## Common Patterns

### Extract Entities by Type
```python
persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
```

### Get Sentences with Entities
```python
for sent in doc.sents:
    if sent.ents:
        print(sent.text)
```

### Extract Subject-Verb-Object Triples
```python
def get_svo(doc):
    triples = []
    for token in doc:
        if token.dep_ == "ROOT":
            verb = token
            subjects = [c for c in token.children if c.dep_ == "nsubj"]
            objects = [c for c in token.children if c.dep_ == "dobj"]
            for subj in subjects:
                for obj in objects:
                    triples.append((subj.text, verb.text, obj.text))
    return triples
```

### Filter Stop Words
```python
filtered = [token.text for token in doc if not token.is_stop and not token.is_punct]
```

### Get Noun Chunks with Context
```python
for chunk in doc.noun_chunks:
    print(f"{chunk.text} (root: {chunk.root.text}, head: {chunk.root.head.text})")
```
