# 🔧 spaCy Troubleshooting & FAQ

## Common Issues and Solutions

---

## Installation Issues

### Issue: Model not found
```
OSError: [E050] Can't find model 'en_core_web_sm'
```

**Solution:**
```bash
python -m spacy download en_core_web_sm
```

Or install directly via pip:
```bash
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.0/en_core_web_sm-3.7.0.tar.gz
```

---

### Issue: Version mismatch
```
spacy.errors.VersionNotFoundError: Model version mismatch
```

**Solution:**
```bash
# Reinstall compatible model
pip uninstall en_core_web_sm
python -m spacy download en_core_web_sm

# Or validate all models
python -m spacy validate
```

---

### Issue: CUDA/GPU not detected
```
WARNING: CUDA not found
```

**Solution:**
```bash
# Install CUDA-enabled spaCy
pip install spacy[cuda11x]  # For CUDA 11.x
pip install spacy[cuda12x]  # For CUDA 12.x

# Or with cupy
pip install cupy-cuda11x
```

---

## Memory Issues

### Issue: Out of memory when processing large texts

**Solution 1: Process in batches**
```python
def process_large_text(text, nlp, chunk_size=100000):
    docs = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        docs.append(nlp(chunk))
    return docs
```

**Solution 2: Disable unused components**
```python
# Only use what you need
doc = nlp(text, disable=["parser", "ner"])
```

**Solution 3: Use nlp.pipe with smaller batches**
```python
for doc in nlp.pipe(texts, batch_size=10):
    # Process doc
    pass
```

---

### Issue: Memory grows when processing many documents

**Solution: Use generator pattern**
```python
def process_texts(texts, nlp):
    for doc in nlp.pipe(texts):
        yield extract_data(doc)  # Don't keep docs in memory
        
# Process without keeping all docs
for data in process_texts(texts, nlp):
    save_to_database(data)
```

---

## Performance Issues

### Issue: Processing is too slow

**Solution 1: Use smaller model**
```python
nlp = spacy.load("en_core_web_sm")  # Instead of lg or trf
```

**Solution 2: Disable unneeded components**
```python
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
```

**Solution 3: Use nlp.pipe() for batch processing**
```python
# Slow
docs = [nlp(text) for text in texts]

# Fast
docs = list(nlp.pipe(texts))
```

**Solution 4: Increase batch size**
```python
docs = list(nlp.pipe(texts, batch_size=50))
```

**Solution 5: Use multiple processes**
```python
docs = list(nlp.pipe(texts, n_process=4))
```

---

### Issue: Word vectors are slow

**Solution: Use PhraseMatcher instead of similarity**
```python
# Slow: Computing similarity for many comparisons
for token in doc:
    for target in targets:
        if token.similarity(nlp(target)) > 0.8:
            pass

# Fast: Use PhraseMatcher
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(t) for t in targets]
matcher.add("TARGETS", patterns)
matches = matcher(doc)
```

---

## Entity Recognition Issues

### Issue: Entity not recognized

**Solution 1: Use larger model**
```python
nlp = spacy.load("en_core_web_lg")  # Better than sm
```

**Solution 2: Use EntityRuler for specific entities**
```python
from spacy.pipeline import EntityRuler

ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [{"label": "ORG", "pattern": "My Company Name"}]
ruler.add_patterns(patterns)
```

**Solution 3: Train custom NER**
```python
# See Module 14 for detailed training guide
```

---

### Issue: Wrong entity type assigned

**Solution: Use EntityRuler to override**
```python
# Add EntityRuler BEFORE the NER component
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [{"label": "PRODUCT", "pattern": "iPhone"}]  # Override ORG
ruler.add_patterns(patterns)
```

---

### Issue: Overlapping entities

**Solution: Use SpanGroup for overlapping annotations**
```python
from spacy.tokens import SpanGroup

doc = nlp("New York City")
spans = SpanGroup(doc, name="overlapping_ents")
spans.append(doc[0:2])  # "New York"
spans.append(doc[0:3])  # "New York City"
doc.spans["my_ents"] = spans
```

---

## Tokenization Issues

### Issue: Word not tokenized correctly
```python
doc = nlp("can't")  # Tokenized as ["ca", "n't"]
```

**Solution: Add special case**
```python
from spacy.symbols import ORTH

nlp.tokenizer.add_special_case("can't", [{ORTH: "can't"}])
```

---

### Issue: Hashtags/mentions split incorrectly

**Solution: Customize tokenizer**
```python
import re
from spacy.tokenizer import Tokenizer

# Keep hashtags and mentions together
special_cases = {}
prefix_re = re.compile(r'''^[\[\("']''')
suffix_re = re.compile(r'''[\]\)"']$''')
infix_re = re.compile(r'''[-~]''')
simple_url_re = re.compile(r'''^https?://''')

def custom_tokenizer(nlp):
    return Tokenizer(
        nlp.vocab,
        prefix_search=prefix_re.search,
        suffix_search=suffix_re.search,
        infix_finditer=infix_re.finditer,
        token_match=simple_url_re.match,
    )

nlp.tokenizer = custom_tokenizer(nlp)
```

---

## Training Issues

### Issue: Training loss not decreasing

**Solutions:**
1. **Check data quality** - Ensure annotations are correct
2. **Increase training data** - More examples help
3. **Adjust learning rate** - Try lower values
4. **Check for label imbalance** - Balance entity types

---

### Issue: Model overfitting

**Solutions:**
1. **Add dropout** - Increase dropout in config
2. **Early stopping** - Stop when dev score plateaus
3. **Add more training data** - Especially varied examples
4. **Data augmentation** - Use nlp-aug or similar

---

### Issue: Catastrophic forgetting when updating

**Solution: Include examples of all types**
```python
# When adding new entity type, include examples of existing types
training_data = [
    # New entity examples
    ("New Corp is hiring", {"entities": [(0, 8, "NEW_TYPE")]}),
    # Existing entity examples (to prevent forgetting)
    ("Apple released iPhone", {"entities": [(0, 5, "ORG"), (15, 21, "PRODUCT")]}),
]
```

---

## Extension Attribute Issues

### Issue: Extension attribute already set
```
ValueError: [E090] Extension 'my_attr' already exists
```

**Solution: Check before setting or use force**
```python
# Check first
if not Token.has_extension("my_attr"):
    Token.set_extension("my_attr", default=None)

# Or force overwrite
Token.set_extension("my_attr", default=None, force=True)
```

---

### Issue: Extension lost after serialization

**Solution: Re-register extensions before loading**
```python
# Register extension before loading docs
Token.set_extension("my_attr", default=None)

# Then load
doc_bin = DocBin().from_disk("docs.spacy")
docs = list(doc_bin.get_docs(nlp.vocab))
```

---

## Similarity Issues

### Issue: Similarity always returns 0

**Solution: Use model with word vectors**
```python
# sm models don't have word vectors
nlp = spacy.load("en_core_web_md")  # or lg

# Check if vectors exist
print(nlp.vocab.vectors.shape)  # Should not be (0, 0)
```

---

### Issue: OOV words have no vector

**Solution: Handle OOV explicitly**
```python
if token.has_vector:
    print(token.vector)
else:
    print(f"'{token.text}' has no vector")

# Or use subword information with transformers
nlp = spacy.load("en_core_web_trf")
```

---

## Matcher Issues

### Issue: Pattern not matching

**Debug steps:**
```python
# 1. Check tokens
print([token.text for token in doc])

# 2. Check attributes you're matching
for token in doc:
    print(f"{token.text}: POS={token.pos_}, LEMMA={token.lemma_}")

# 3. Simplify pattern to find issue
pattern = [{"POS": "VERB"}]  # Start simple
matches = matcher(doc)
```

---

### Issue: Too many matches

**Solution: Make pattern more specific**
```python
# Too broad
pattern = [{"POS": "NOUN"}]

# More specific
pattern = [
    {"POS": "ADJ", "OP": "?"},  # Optional adjective
    {"POS": "NOUN", "IS_ALPHA": True}  # Alpha noun only
]
```

---

## Multiprocessing Issues

### Issue: Pickle error with n_process > 1

**Solution: Use simpler objects or spawn method**
```python
import multiprocessing as mp
mp.set_start_method("spawn")

# Avoid lambda functions in callbacks
def on_match(matcher, doc, id, matches):
    pass  # Can't use lambda with multiprocessing
```

---

### Issue: n_process not speeding up

**Reasons:**
1. **Too few documents** - Overhead > benefit
2. **Documents too small** - Use larger batch_size
3. **Already using GPU** - CPU multiprocessing doesn't help GPU

---

## FAQ

### Q: Which model should I use?

| Scenario | Recommended Model |
|----------|-------------------|
| Prototyping/Testing | `en_core_web_sm` |
| Production (speed priority) | `en_core_web_sm` or `md` |
| Production (accuracy priority) | `en_core_web_lg` |
| Best accuracy needed | `en_core_web_trf` |
| Need word vectors | `en_core_web_md` or `lg` |
| Memory constrained | `en_core_web_sm` |

---

### Q: How do I process multiple languages?

```python
# Load multiple models
nlp_en = spacy.load("en_core_web_sm")
nlp_de = spacy.load("de_core_news_sm")

# Or use language detection
from spacy_langdetect import LanguageDetector
# Then route to appropriate model
```

---

### Q: Can I use spaCy with pandas?

```python
import pandas as pd

df = pd.DataFrame({"text": ["Text 1", "Text 2"]})

# Process efficiently
df["doc"] = list(nlp.pipe(df["text"]))

# Extract features
df["entities"] = df["doc"].apply(lambda d: [e.text for e in d.ents])
df["tokens"] = df["doc"].apply(lambda d: [t.text for t in d])
```

---

### Q: How do I handle special characters/emojis?

```python
# spaCy handles Unicode well
doc = nlp("I love 🍕!")

for token in doc:
    print(f"'{token.text}' - is_alpha: {token.is_alpha}")
# '🍕' is recognized as a token

# For emoji-specific analysis
# pip install spacymoji
import spacymoji
nlp.add_pipe("emoji", first=True)
```

---

### Q: Can I use spaCy offline?

Yes! After downloading models:
```python
# Models are cached locally
nlp = spacy.load("en_core_web_sm")  # Works offline

# Or load from specific path
nlp = spacy.load("/path/to/model")
```

---

### Q: How do I speed up transformer models?

```python
# 1. Use GPU
spacy.require_gpu()

# 2. Batch processing
docs = list(nlp.pipe(texts, batch_size=8))

# 3. Limit pipeline
nlp = spacy.load("en_core_web_trf", disable=["lemmatizer"])

# 4. Use smaller context
# Configure in training config
```

---

### Q: How do I handle very long documents?

```python
# Increase max_length
nlp.max_length = 2000000  # Default is 1000000

# Or process in chunks
def chunk_text(text, chunk_size=100000):
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]

for chunk in chunk_text(long_text):
    doc = nlp(chunk)
    # Process chunk
```

---

### Q: spaCy vs Hugging Face Transformers?

| Aspect | spaCy | HuggingFace |
|--------|-------|-------------|
| Focus | Production NLP pipelines | Model hub & research |
| Ease of use | Very easy | Moderate |
| Speed | Optimized | Varies |
| Tasks | Full NLP pipeline | Mainly transformers |
| Integration | Full solution | Component |
| Best for | Production apps | Research/fine-tuning |

**Use both:** spacy-transformers combines them!

---

## Getting Help

1. **Documentation:** https://spacy.io/usage
2. **GitHub Issues:** https://github.com/explosion/spaCy/issues
3. **Discussions:** https://github.com/explosion/spaCy/discussions
4. **Stack Overflow:** Tag `spacy`
5. **Prodigy Support:** https://support.prodi.gy (for Prodigy users)
