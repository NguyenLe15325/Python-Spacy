# 📖 spaCy Complete Curriculum

## Detailed Learning Objectives by Module

---

## 🟢 PART 1: FOUNDATIONS

### Module 1: Introduction & Setup

#### 1.1 What is spaCy
**Learning Objectives:**
- Understand what spaCy is and its position in the NLP landscape
- Compare spaCy with NLTK, Stanford NLP, and other libraries
- Identify ideal use cases for spaCy
- Understand spaCy's design philosophy (speed, accuracy, ease of use)

**Key Topics:**
- Industrial-strength NLP
- Statistical models vs rule-based systems
- spaCy's ecosystem (Prodigy, Thinc, etc.)
- When to use spaCy vs alternatives

---

#### 1.2 Installation & Setup
**Learning Objectives:**
- Install spaCy in different environments
- Set up virtual environments for NLP projects
- Configure GPU support for acceleration
- Troubleshoot common installation issues

**Key Topics:**
- pip vs conda installation
- CUDA and GPU setup
- Platform-specific considerations (Windows/Mac/Linux)
- Verifying installation

---

#### 1.3 Language Models
**Learning Objectives:**
- Understand the difference between model sizes (sm/md/lg/trf)
- Know when to use which model
- Download and manage multiple models
- Understand model versioning

**Key Topics:**
- Model architectures
- Word vectors in models
- Model metadata
- Memory and speed trade-offs

---

#### 1.4 First NLP Program
**Learning Objectives:**
- Process text with spaCy
- Explore basic outputs (tokens, entities, etc.)
- Understand the nlp() callable
- Inspect Doc objects

**Key Topics:**
- Basic text processing workflow
- Exploring output interactively
- Common beginner patterns

---

#### 1.5 spaCy Architecture
**Learning Objectives:**
- Understand the high-level architecture
- Know how data flows through the pipeline
- Grasp the relationship between core objects

**Key Topics:**
- Vocab, StringStore, Lexemes
- Doc, Token, Span relationships
- Pipeline architecture
- Memory efficiency design

---

### Module 2: Core Data Structures

#### 2.1 Doc Object
**Learning Objectives:**
- Create and manipulate Doc objects
- Access document-level properties
- Iterate over documents
- Serialize documents

**Key Topics:**
- Doc properties (text, ents, sents, noun_chunks)
- Doc iteration patterns
- Doc as sequence of Tokens
- Manual Doc creation

---

#### 2.2 Token Object
**Learning Objectives:**
- Access all token attributes
- Understand lexical vs linguistic attributes
- Filter tokens using boolean attributes
- Navigate token relationships

**Key Topics:**
- Lexical attributes (is_alpha, is_punct, etc.)
- Linguistic attributes (pos_, dep_, lemma_)
- Token navigation (head, children, ancestors)
- Token shape patterns

---

#### 2.3 Span Object
**Learning Objectives:**
- Create spans by slicing
- Work with entity spans
- Create labeled spans manually
- Use SpanGroups

**Key Topics:**
- Span creation methods
- Span properties (root, sent, label)
- Entity spans
- Named span groups

---

#### 2.4 Vocab & StringStore
**Learning Objectives:**
- Understand vocabulary management
- Work with StringStore for string interning
- Access Lexemes
- Understand memory efficiency

**Key Topics:**
- Hash-based string storage
- Lexeme vs Token distinction
- Vocabulary lookups
- Adding to vocabulary

---

#### 2.5 Advanced Data Structures
**Learning Objectives:**
- Create documents manually
- Copy and merge documents
- Handle token alignment
- Work with character offsets

**Key Topics:**
- Manual Doc construction
- Token/character alignment
- Merging tokens
- Whitespace handling

---

### Module 3: The NLP Pipeline

#### 3.1 Pipeline Overview
**Learning Objectives:**
- Understand pipeline architecture
- Know the order of components
- Trace data flow through pipeline

**Key Topics:**
- Tokenizer vs pipeline components
- Component ordering rules
- Pipeline configuration

---

#### 3.2 Built-in Components
**Learning Objectives:**
- Understand each built-in component
- Know what annotations each component adds
- Access component configurations

**Key Topics:**
- tok2vec, tagger, parser
- ner, lemmatizer
- attribute_ruler, morphologizer
- Component-specific settings

---

#### 3.3 Pipeline Management
**Learning Objectives:**
- Add, remove, replace components
- Enable/disable components
- Rename components
- Get component by name

**Key Topics:**
- nlp.add_pipe(), remove_pipe()
- nlp.select_pipes() context manager
- Component replacement
- Pipeline introspection

---

#### 3.4 Processing Text
**Learning Objectives:**
- Process single documents efficiently
- Batch process with nlp.pipe()
- Stream large datasets
- Handle processing errors

**Key Topics:**
- Single vs batch processing
- batch_size and n_process
- as_tuples for metadata
- Error handling in batches

---

#### 3.5 Pipeline Debugging
**Learning Objectives:**
- Debug pipeline issues
- Profile pipeline performance
- Understand error messages
- Optimize problematic pipelines

**Key Topics:**
- spacy.explain() for annotations
- Analyzing pipeline speed
- Common errors and fixes
- Debug mode

---

## 🟡 PART 2: CORE NLP FEATURES

### Module 4: Tokenization & Text Processing

#### 4.1-4.5 Tokenization Deep Dive
**Learning Objectives:**
- Master tokenization rules
- Customize tokenizer behavior
- Handle special cases
- Segment sentences correctly
- Normalize text effectively

**Key Topics:**
- Tokenization algorithm
- Special tokenization cases
- Prefix/suffix/infix rules
- Sentence boundaries
- Custom sentencizers
- Text cleaning patterns
- URLs, emails, hashtags, emojis

---

### Module 5: Linguistic Annotations

#### 5.1-5.6 Linguistic Analysis
**Learning Objectives:**
- Extract and use POS tags
- Apply lemmatization correctly
- Navigate dependency trees
- Analyze morphology
- Extract noun phrases
- Visualize linguistic structure

**Key Topics:**
- Universal POS tags vs fine-grained
- Lemmatizer modes (lookup, rule)
- Dependency relations
- Parse tree navigation
- MorphAnalysis object
- Noun chunk extraction
- displaCy visualization

---

### Module 6: Named Entity Recognition

#### 6.1-6.6 NER Mastery
**Learning Objectives:**
- Extract named entities
- Understand all entity types
- Work with entity properties
- Handle entity context
- Visualize entities
- Evaluate NER performance

**Key Topics:**
- Entity span access
- Built-in entity types
- Entity labels and KB IDs
- Context windows
- displaCy ENT rendering
- Precision, recall, F1 for NER

---

### Module 7: Word Vectors & Similarity

#### 7.1-7.6 Semantic Understanding
**Learning Objectives:**
- Understand word embeddings
- Access vectors in spaCy
- Compute similarity scores
- Perform vector operations
- Load custom vectors
- Know vector limitations

**Key Topics:**
- Word2Vec, GloVe concepts
- Token, Span, Doc vectors
- Cosine similarity
- Vector arithmetic
- Custom vector formats
- OOV handling

---

## 🟠 PART 3: PATTERN MATCHING & RULES

### Module 8: Token-Based Matching

#### 8.1-8.6 Matcher Mastery
**Learning Objectives:**
- Create token patterns
- Use all pattern operators
- Apply quantifiers
- Match on various attributes
- Handle match callbacks
- Build complex patterns

**Key Topics:**
- Matcher class
- Pattern specification
- OP operators (!, ?, +, *)
- Attribute matching
- On-match callbacks
- Pattern debugging

---

### Module 9: Advanced Matching

#### 9.1-9.6 Advanced Pattern Systems
**Learning Objectives:**
- Use PhraseMatcher efficiently
- Match on different attributes
- Create dependency patterns
- Combine multiple matchers
- Build rule-based NER

**Key Topics:**
- PhraseMatcher performance
- LOWER, LEMMA matching
- DependencyMatcher
- Anchor tokens
- EntityRuler component
- Pattern files (JSONL)

---

## 🔴 PART 4: CUSTOMIZATION & EXTENSION

### Module 10: Custom Pipeline Components

#### 10.1-10.6 Component Development
**Learning Objectives:**
- Build simple components
- Create configurable components
- Handle component lifecycle
- Build stateful components
- Manage dependencies
- Apply practical examples

**Key Topics:**
- @Language.component
- @Language.factory
- Initialization and processing
- Requires and assigns
- Training-aware components
- Real-world examples

---

### Module 11: Extension Attributes

#### 11.1-11.6 Custom Attributes
**Learning Objectives:**
- Add custom attributes
- Set default values properly
- Create computed properties
- Add custom methods
- Follow best practices
- Serialize custom data

**Key Topics:**
- set_extension()
- Default vs getter extensions
- Method extensions
- Force overwrite
- Serialization patterns

---

### Module 12: Custom Tokenization

#### 12.1-12.6 Tokenizer Control
**Learning Objectives:**
- Understand tokenizer internals
- Add special cases
- Modify tokenization rules
- Build custom tokenizers
- Retokenize documents

**Key Topics:**
- Tokenizer algorithm
- Special cases
- Prefix/suffix/infix rules
- Token match functions
- Custom Tokenizer class
- Doc.retokenize()

---

## 🟣 PART 5: TRAINING & FINE-TUNING

### Module 13: Training Fundamentals

#### 13.1-13.6 Training System
**Learning Objectives:**
- Know when to train
- Prepare training data
- Understand config system
- Run training workflow
- Monitor training
- Apply best practices

**Key Topics:**
- Training vs rules
- Example objects, DocBin
- config.cfg structure
- spacy train command
- Metrics and loss
- Common pitfalls

---

### Module 14: Training NER

#### 14.1-14.6 Custom NER Models
**Learning Objectives:**
- Prepare NER data
- Use annotation tools
- Configure NER training
- Train NER models
- Update existing models
- Evaluate NER

**Key Topics:**
- NER data formats
- Annotation tools
- NER config options
- Training process
- Fine-tuning
- Error analysis

---

### Module 15: Training Text Classification

#### 15.1-15.6 Text Classifiers
**Learning Objectives:**
- Understand classification types
- Prepare classification data
- Choose architectures
- Train classifiers
- Handle multi-label
- Evaluate classifiers

**Key Topics:**
- Single vs multi-label
- Data balancing
- TextCat architectures
- Training configuration
- Multi-label setup
- Evaluation metrics

---

### Module 16: Advanced Training

#### 16.1-16.6 Advanced Techniques
**Learning Objectives:**
- Train multiple components
- Apply transfer learning
- Augment training data
- Use active learning
- Scale training
- Track experiments

**Key Topics:**
- Multi-component training
- Pretrained models
- Data augmentation
- Active learning
- Distributed training
- W&B, MLflow

---

## 🔵 PART 6: TRANSFORMERS & MODERN NLP

### Module 17: spaCy Transformers

#### 17.1-17.6 Transformer Integration
**Learning Objectives:**
- Understand transformers
- Set up spacy-transformers
- Use transformer models
- Access embeddings
- Compare approaches
- Use custom models

**Key Topics:**
- Transformer concepts
- spacy-transformers setup
- trf model usage
- Contextualized embeddings
- Trade-offs
- HuggingFace integration

---

### Module 18: Training with Transformers

#### 18.1-18.6 Transformer Training
**Learning Objectives:**
- Configure transformer training
- Train NER with transformers
- Train classification
- Optimize for efficiency
- Handle memory constraints
- Apply best practices

**Key Topics:**
- Transformer config
- Fine-tuning strategies
- Frozen vs trainable
- Gradient accumulation
- Mixed precision
- Best practices

---

## 🟤 PART 7: PRODUCTION & DEPLOYMENT

### Module 19: Performance Optimization

#### 19.1-19.6 Optimization Techniques
**Learning Objectives:**
- Profile pipelines
- Optimize selectively
- Batch efficiently
- Parallelize processing
- Manage memory
- Use GPU effectively

**Key Topics:**
- Profiling tools
- Component selection
- Batch optimization
- n_process usage
- Memory streaming
- CUDA optimization

---

### Module 20: Serialization & Deployment

#### 20.1-20.6 Production Deployment
**Learning Objectives:**
- Save and load models
- Serialize documents
- Package models
- Build REST APIs
- Containerize apps
- Deploy to cloud

**Key Topics:**
- to_disk/from_disk
- DocBin serialization
- Model packaging
- FastAPI/Flask
- Docker
- Cloud platforms

---

### Module 21: spaCy Projects

#### 21.1-21.6 Project Workflows
**Learning Objectives:**
- Understand spaCy projects
- Configure project.yml
- Manage data assets
- Create custom commands
- Integrate DVC
- Use templates

**Key Topics:**
- Project structure
- Workflows and commands
- Asset management
- Custom scripts
- Version control
- Templates

---

## ⚫ PART 8: SPECIALIZED TOPICS

### Module 22: Multilingual NLP

#### 22.1-22.6 Multi-language Support
**Learning Objectives:**
- Use multilingual models
- Detect languages
- Apply cross-lingual techniques
- Process CJK languages
- Handle RTL text
- Work with low-resource languages

**Key Topics:**
- Available models
- Language detection
- Cross-lingual transfer
- Chinese/Japanese
- Arabic/Hebrew
- Low-resource strategies

---

### Module 23: Information Extraction

#### 23.1-23.6 Structured Extraction
**Learning Objectives:**
- Extract relations
- Detect events
- Resolve coreference
- Link entities
- Build knowledge graphs
- Fill templates

**Key Topics:**
- Relation extraction
- Event detection
- Coreference resolution
- Entity linking
- Knowledge graphs
- Template filling

---

### Module 24: Document Processing

#### 24.1-24.6 Document Analysis
**Learning Objectives:**
- Handle document structure
- Process large documents
- Extract from PDFs
- Analyze corpora
- Compute document similarity
- Summarize text

**Key Topics:**
- Document structure
- Large file handling
- PDF extraction
- Corpus analysis
- Document clustering
- Extractive summarization

---

### Module 25: Integration & Ecosystem

#### 25.1-25.6 Tool Integration
**Learning Objectives:**
- Integrate with HuggingFace
- Connect with scikit-learn
- Process DataFrames
- Create visualizations
- Build Streamlit apps
- Use Prodigy

**Key Topics:**
- HuggingFace integration
- ML pipeline features
- Pandas processing
- Visualization tools
- Streamlit apps
- Prodigy annotation

---

## 🏆 PART 9: CAPSTONE PROJECTS

### Module 26: Real-World Projects

#### 26.1-26.8 End-to-End Applications
**Projects:**
1. **Resume Parser** - Extract structured information from resumes
2. **News Analyzer** - Analyze news articles for entities, sentiment, topics
3. **Customer Feedback** - Process and analyze customer reviews
4. **Legal Document Analysis** - Extract clauses and entities from contracts
5. **Medical NER** - Recognize medical entities
6. **Chatbot NLU** - Intent classification and slot filling
7. **Semantic Search** - Build a search engine with spaCy
8. **Content Moderation** - Detect toxic/inappropriate content

---

## 📈 Skills Progression

```
Beginner          Intermediate           Advanced              Expert
   │                   │                    │                    │
   ▼                   ▼                    ▼                    ▼
┌──────────┐     ┌───────────┐      ┌──────────────┐     ┌────────────┐
│ Modules  │     │  Modules  │      │   Modules    │     │  Modules   │
│  1 - 6   │ ──▶ │   7 - 12  │ ──▶  │   13 - 18    │ ──▶ │  19 - 26   │
└──────────┘     └───────────┘      └──────────────┘     └────────────┘
     │                │                   │                    │
     ▼                ▼                   ▼                    ▼
  Basic NLP      Pattern Matching    Training Models     Production
  Processing     Custom Components   Transformers        Deployment
```

---

## ⏱️ Time Estimates

| Part | Modules | Estimated Time | Difficulty |
|------|---------|----------------|------------|
| Foundations | 1-3 | 1-2 weeks | ⭐ |
| Core Features | 4-7 | 2-3 weeks | ⭐⭐ |
| Pattern Matching | 8-9 | 1 week | ⭐⭐ |
| Customization | 10-12 | 1-2 weeks | ⭐⭐⭐ |
| Training | 13-16 | 2-3 weeks | ⭐⭐⭐⭐ |
| Transformers | 17-18 | 1-2 weeks | ⭐⭐⭐⭐ |
| Production | 19-21 | 1-2 weeks | ⭐⭐⭐ |
| Specialized | 22-25 | 2-3 weeks | ⭐⭐⭐⭐ |
| Projects | 26 | 2-4 weeks | ⭐⭐⭐⭐⭐ |

**Total: 13-22 weeks for complete mastery**
