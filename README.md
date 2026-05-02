# 🧠 Python spaCy - Complete Comprehensive Guide

> **A modular, hands-on learning guide covering spaCy from absolute fundamentals to production-ready advanced techniques.**

[![spaCy](https://img.shields.io/badge/spaCy-v3.x-09a3d5)](https://spacy.io)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Course Structure](#-course-structure)
- [Learning Path](#-learning-path)

---

## 🎯 Overview

This comprehensive guide is designed to take you from zero knowledge to expert-level proficiency in spaCy, the industrial-strength NLP library. Each module is self-contained with practical examples and exercises.

**What you'll learn:**
- Core NLP concepts and spaCy architecture
- Text processing, tokenization, and linguistic analysis
- Named Entity Recognition (NER) and information extraction
- Word vectors, embeddings, and semantic similarity
- Pattern matching and rule-based systems
- Building custom pipeline components
- Training and fine-tuning models
- Production deployment and optimization
- Real-world project implementations

---

## 📖 Prerequisites

| Requirement | Level |
|-------------|-------|
| Python | 3.8+ (3.10+ recommended) |
| Python Knowledge | Intermediate |
| NLP Background | Not required (covered in Module 1) |
| Machine Learning | Helpful but not required |

---

## 🚀 Quick Start

```bash
# Create virtual environment
python -m venv spacy-env
source spacy-env/bin/activate  # Linux/Mac
spacy-env\Scripts\activate     # Windows

# Install spaCy
pip install spacy

# Download language models
python -m spacy download en_core_web_sm    # Small (12MB) - Fast, no vectors
python -m spacy download en_core_web_md    # Medium (40MB) - With word vectors
python -m spacy download en_core_web_lg    # Large (560MB) - Best accuracy
python -m spacy download en_core_web_trf   # Transformer (400MB) - State-of-the-art

# Verify installation
python -m spacy validate
```

---

## 📚 Course Structure

### 🟢 PART 1: FOUNDATIONS (Modules 1-3)
*Build a solid understanding of spaCy fundamentals*

---

### Module 1: Introduction & Setup
> *Getting started with spaCy and understanding NLP basics*

**Notebook:** `01_introduction.ipynb`

**Topics Covered:**
- What is spaCy, comparison with NLTK/other libraries, use cases
- Installation methods, virtual environments, GPU setup
- Model types (sm/md/lg/trf), downloading, model selection guide
- Hello World, basic text processing, exploring outputs
- High-level architecture, data flow, design philosophy

---

### Module 2: Core Data Structures
> *Master the fundamental objects: Doc, Token, Span, Vocab*

**Notebook:** `02_core_data_structures.ipynb`

**Topics Covered:**
- Doc creation, properties, iteration, serialization
- Token attributes, lexical/linguistic properties
- Span creation, slicing, labeled spans, span groups
- Vocabulary, StringStore, Lexemes, memory efficiency
- Manual creation, copying, merging, alignment

---

### Module 3: The NLP Pipeline
> *Understand how spaCy processes text through its pipeline*

**Notebook:** `03_nlp_pipeline.ipynb`

**Topics Covered:**
- Pipeline architecture, component order, data flow
- Tokenizer, Tagger, Parser, NER, Lemmatizer details
- Adding, removing, disabling, replacing components
- Single docs, batch processing with nlp.pipe(), streaming
- Debugging, profiling, understanding errors

---

### 🟡 PART 2: CORE NLP FEATURES (Modules 4-7)
*Master essential NLP capabilities*

---

### Module 4: Tokenization & Text Processing
> *Break down text into meaningful units*

**Notebook:** `04_tokenization.ipynb`

**Topics Covered:**
- How tokenization works, rules, edge cases
- Custom tokenization rules, special cases, prefixes/suffixes
- Sentence boundaries, Sentencizer, custom rules
- Lowercasing, removing punctuation, cleaning text
- URLs, emails, hashtags, emojis, code snippets

---

### Module 5: Linguistic Annotations
> *Extract grammatical and syntactic information*

**Notebook:** `05_linguistic_annotations.ipynb`

**Topics Covered:**
- Part-of-speech tags (coarse & fine-grained), tag explanations
- Lemmas, lemmatizer modes, custom lemmatization
- Dependency trees, relations, navigating parse trees
- Morphology, inflection, MorphAnalysis object
- Extracting noun phrases, chunk properties
- displaCy visualizations, dependency trees, entity highlighting

---

### Module 6: Named Entity Recognition (NER)
> *Identify and classify named entities in text*

**Notebook:** `06_named_entity_recognition.ipynb`

**Topics Covered:**
- What is NER, entity types, accessing entities
- PERSON, ORG, GPE, DATE, MONEY, etc. - complete reference
- Entity spans, labels, KB IDs, entity linking
- Entity context, coreference hints, disambiguation
- Visualizing entities with displaCy, custom styling
- Evaluating NER performance, precision/recall/F1

---

### Module 7: Word Vectors & Similarity
> *Understand semantic meaning through vector representations*

**Notebook:** `07_vectors_similarity.ipynb`

**Topics Covered:**
- What are word vectors, Word2Vec, GloVe basics
- Accessing vectors in spaCy, vector properties
- Token, Span, Doc similarity, cosine similarity
- Vector arithmetic, analogies, clustering
- Loading custom vectors, training word vectors
- OOV words, limitations, when to use transformers

---

### 🟠 PART 3: PATTERN MATCHING & RULES (Modules 8-9)
*Build rule-based NLP systems*

---

### Module 8: Token-Based Matching
> *Find patterns using token attributes*

**Notebook:** `08_token_matching.ipynb`

**Topics Covered:**
- Matcher class, creating patterns, finding matches
- Pattern operators (OP), attributes, wildcards
- Optional (?), one or more (+), zero or more (*)
- TEXT, LEMMA, POS, DEP, ENT_TYPE, SHAPE, etc.
- On-match callbacks, custom actions on matches
- Multi-token patterns, nested patterns, pattern debugging

---

### Module 9: Advanced Matching
> *Efficient phrase matching and syntactic patterns*

**Notebook:** `09_advanced_matching.ipynb`

**Topics Covered:**
- PhraseMatcher for exact/fuzzy phrase matching
- Matching on different attributes (LOWER, LEMMA)
- DependencyMatcher for syntactic patterns
- Creating dependency patterns, anchor tokens, relations
- Using multiple matchers together, priority handling
- EntityRuler for rule-based NER, pattern files

---

### 🔴 PART 4: CUSTOMIZATION & EXTENSION (Modules 10-12)
*Extend spaCy with custom functionality*

---

### Module 10: Custom Pipeline Components
> *Build your own pipeline components*

**Notebook:** `10_custom_pipeline_components.ipynb`

**Topics Covered:**
- @Language.component decorator, simple components
- @Language.factory, configurable components
- Initialization, processing, serialization
- Components with state, training-aware components
- Requiring other components, ordering
- Practical examples: sentiment, keywords, custom NER

---

### Module 11: Extension Attributes
> *Add custom data to Doc, Token, and Span*

**Notebook:** `11_extension_attributes.ipynb`

**Topics Covered:**
- Setting custom attributes with set_extension
- Default values, mutable defaults
- Property getters for computed attributes
- Custom methods on Doc/Token/Span
- Common patterns, best practices
- Saving/loading custom attributes

---

### Module 12: Custom Tokenization
> *Complete control over tokenization*

**Notebook:** `12_custom_tokenization.ipynb`

**Topics Covered:**
- How the tokenizer works internally
- Adding special tokenization cases
- Customizing prefix/suffix/infix rules
- Custom token matching functions
- Building a completely custom tokenizer
- Merging and splitting tokens after processing

---

### 🟣 PART 5: TRAINING & FINE-TUNING (Modules 13-16)
*Train custom models for your domain*

---

### Module 13: Training Fundamentals
> *Understand spaCy's training system*

**Notebook:** `13_training_fundamentals.ipynb`

**Topics Covered:**
- When to train, training vs rules, data requirements
- Training data structure, Example objects, DocBin
- config.cfg, base configs, config overrides
- init config, train, evaluate commands
- Understanding scores, loss curves, early stopping
- Best practices, common pitfalls, debugging

---

### Module 14: Training NER Models
> *Train custom Named Entity Recognition*

**Notebook:** `14_training_ner_models.ipynb`

**Topics Covered:**
- Preparing NER training data, annotation formats
- Prodigy, Label Studio, Doccano, manual annotation
- NER-specific configuration, architecture choices
- Training process, monitoring, checkpoints
- Fine-tuning existing NER, adding new entity types
- Evaluation metrics, error analysis, improving models

---

### Module 15: Training Text Classification
> *Build text classifiers*

**Notebook:** `15_training_text_classification.ipynb`

**Topics Covered:**
- Text classification use cases, single vs multi-label
- Preparing classification data, handling imbalance
- TextCatBOW, TextCatCNN, TextCatEnsemble
- Training process, configuration, tuning
- Multi-label classification setup
- Accuracy, precision, recall, confusion matrices

---

### Module 16: Advanced Training
> *Complex training scenarios and techniques*

**Notebook:** `16_advanced_training.ipynb`

**Topics Covered:**
- Training NER + TextCat together
- Using pretrained models, domain adaptation
- Augmentation techniques for NLP
- Active learning strategies with spaCy
- Multi-GPU training, Ray integration
- Weights & Biases, MLflow integration

---

### 🔵 PART 6: TRANSFORMERS & MODERN NLP (Modules 17-18)
*State-of-the-art language models*

---

### Module 17: spaCy Transformers
> *Use transformer models in spaCy*

**Notebook:** `17_spacy_transformers.ipynb`

**Topics Covered:**
- What are transformers, BERT/RoBERTa/GPT overview
- Installing spacy-transformers, trf models
- Processing text with transformer models
- Accessing transformer outputs, contextualized embeddings
- When to use transformers vs static vectors
- Using custom HuggingFace models in spaCy

---

### Module 18: Training with Transformers
> *Fine-tune transformer-based models*

**Notebook:** `18_training_with_transformers.ipynb`

**Topics Covered:**
- Transformer training configuration
- Training NER with transformers
- Training text classification with transformers
- Freezing transformer weights, efficiency
- Gradient accumulation, mixed precision
- Best practices for transformer training

---

### 🟤 PART 7: PRODUCTION & DEPLOYMENT (Modules 19-21)
*Deploy spaCy in real-world applications*

---

### Module 19: Performance Optimization
> *Make spaCy fast and efficient*

**Notebook:** `19_performance_optimization.ipynb`

**Topics Covered:**
- Profiling spaCy pipelines, identifying bottlenecks
- Selective processing, minimal pipelines
- Efficient batch processing with nlp.pipe()
- Parallel processing, n_process parameter
- Reducing memory usage, streaming large files
- GPU setup, CUDA, performance comparison

---

### Module 20: Serialization & Deployment
> *Save, load, and deploy models*

**Notebook:** `20_serialization_deployment.ipynb`

**Topics Covered:**
- nlp.to_disk(), nlp.from_disk(), packaging
- DocBin, saving processed documents
- Creating installable model packages
- FastAPI, Flask REST APIs for spaCy
- Containerizing spaCy applications
- AWS, GCP, Azure deployment strategies

---

### Module 21: spaCy Projects
> *Reproducible NLP workflows*

**Notebook:** `21_spacy_projects.ipynb`

**Topics Covered:**
- What are spaCy projects, project structure
- project.yml configuration, commands, workflows
- Managing data assets, remote storage
- Creating custom project commands
- Data Version Control integration
- Using and creating project templates

---

### ⚫ PART 8: SPECIALIZED TOPICS (Modules 22-25)
*Domain-specific and advanced applications*

---

### Module 22: Multilingual NLP
> *Process multiple languages*

**Notebook:** `22_multilingual_nlp.ipynb`

**Topics Covered:**
- Available language models, xx_ent_wiki_sm
- Detecting languages in text
- Cross-lingual transfer, multilingual embeddings
- CJK language processing specifics
- Arabic, Hebrew - right-to-left text
- Working with low-resource languages

---

### Module 23: Information Extraction
> *Extract structured information from text*

**Notebook:** `23_information_extraction.ipynb`

**Topics Covered:**
- Extracting relationships between entities
- Detecting events and their arguments
- Coreference resolution with spaCy
- Linking entities to knowledge bases
- Building knowledge graphs from text
- Structured data extraction patterns

---

### Module 24: Document Processing
> *Process full documents and corpora*

**Notebook:** `24_document_processing.ipynb`

**Topics Covered:**
- Handling sections, paragraphs, headers
- Processing large documents efficiently
- Extracting text from PDFs
- Analyzing document collections
- Document-level similarity and clustering
- Extractive summarization techniques

---

### Module 25: Integration & Ecosystem
> *Integrate spaCy with other tools*

**Notebook:** `25_integration_ecosystem.ipynb`

**Topics Covered:**
- Using HuggingFace models and datasets
- Feature extraction for ML pipelines
- Processing DataFrames with spaCy
- NetworkX, Matplotlib, Plotly visualizations
- Building NLP apps with Streamlit
- Prodigy annotation tool integration

---

### 🏆 PART 9: REAL-WORLD PROJECTS (Module 26)
*Apply everything in practical projects*

---

### Module 26: Capstone Projects
> *End-to-end NLP applications*

**Notebook:** `26_capstone_projects.ipynb`

**Topics Covered:**
- Extract structured info from resumes
- News article analysis pipeline
- Sentiment analysis and entity extraction
- Contract and legal document processing
- Medical entity recognition system
- Intent classification and slot filling
- Semantic search implementation
- Toxic content detection system

---

## 🗺️ Learning Path

### 🚶 Beginner Path (2-3 weeks)
```
Module 1 → Module 2 → Module 3 → Module 4 → Module 5 → Module 6
```

### 🏃 Intermediate Path (4-6 weeks)
```
Beginner Path → Module 7 → Module 8 → Module 9 → Module 10 → Module 11
```

### 🏎️ Advanced Path (8-10 weeks)
```
Intermediate Path → Module 13-16 (Training) → Module 17-18 (Transformers)
```

### 🎯 Production Path
```
Advanced Path → Module 19-21 (Deployment) → Module 26 (Projects)
```

### 📍 Specialized Paths

| Path | Modules | Focus |
|------|---------|-------|
| **NER Specialist** | 1-3, 6, 8-9, 14 | Entity recognition mastery |
| **Classification Expert** | 1-3, 7, 15, 17-18 | Text classification |
| **Rule-Based NLP** | 1-5, 8-9, 12 | Pattern matching systems |
| **Production Engineer** | 1-3, 19-21 | Deployment and scaling |
| **Research/ML Engineer** | All modules | Complete understanding |

---

## 📁 Repository Structure

```
Python-Spacy/
├── README.md
├── requirements.txt
├── setup.py
│
├── 01_introduction/
│   ├── 01_what_is_spacy.ipynb
│   ├── 02_installation_setup.ipynb
│   ├── 03_language_models.ipynb
│   ├── 04_first_nlp_program.ipynb
│   └── 05_spacy_architecture.ipynb
│
├── 02_core_data_structures/
│   ├── 01_doc_object.ipynb
│   ├── 02_token_object.ipynb
│   ├── 03_span_object.ipynb
│   ├── 04_vocab_stringstore.ipynb
│   └── 05_doc_token_span_advanced.ipynb
│
├── 03_nlp_pipeline/
│   ├── 01_pipeline_overview.ipynb
│   ├── 02_built_in_components.ipynb
│   ├── 03_pipeline_management.ipynb
│   ├── 04_processing_text.ipynb
│   └── 05_pipeline_debugging.ipynb
│
├── 04_tokenization/
│   ├── 01_tokenization_basics.ipynb
│   ├── 02_customizing_tokenizer.ipynb
│   ├── 03_sentence_segmentation.ipynb
│   ├── 04_text_normalization.ipynb
│   └── 05_handling_special_text.ipynb
│
├── 05_linguistic_annotations/
│   ├── 01_pos_tagging.ipynb
│   ├── 02_lemmatization.ipynb
│   ├── 03_dependency_parsing.ipynb
│   ├── 04_morphological_analysis.ipynb
│   ├── 05_noun_chunks.ipynb
│   └── 06_visualizing_annotations.ipynb
│
├── 06_named_entity_recognition/
│   ├── 01_ner_fundamentals.ipynb
│   ├── 02_built_in_entity_types.ipynb
│   ├── 03_entity_properties.ipynb
│   ├── 04_ner_with_context.ipynb
│   ├── 05_ner_visualization.ipynb
│   └── 06_ner_evaluation.ipynb
│
├── 07_vectors_similarity/
│   ├── 01_word_vectors_intro.ipynb
│   ├── 02_spacy_vectors.ipynb
│   ├── 03_similarity_computation.ipynb
│   ├── 04_vector_operations.ipynb
│   ├── 05_custom_vectors.ipynb
│   └── 06_vectors_limitations.ipynb
│
├── 08_token_matching/
│   ├── 01_matcher_basics.ipynb
│   ├── 02_pattern_syntax.ipynb
│   ├── 03_quantifiers_operators.ipynb
│   ├── 04_pattern_attributes.ipynb
│   ├── 05_matcher_callbacks.ipynb
│   └── 06_complex_patterns.ipynb
│
├── 09_advanced_matching/
│   ├── 01_phrase_matcher.ipynb
│   ├── 02_phrase_matcher_attrs.ipynb
│   ├── 03_dependency_matcher.ipynb
│   ├── 04_dependency_patterns.ipynb
│   ├── 05_combining_matchers.ipynb
│   └── 06_entity_ruler.ipynb
│
├── 10_custom_components/
│   ├── 01_component_basics.ipynb
│   ├── 02_component_factories.ipynb
│   ├── 03_component_lifecycle.ipynb
│   ├── 04_stateful_components.ipynb
│   ├── 05_component_dependencies.ipynb
│   └── 06_component_examples.ipynb
│
├── 11_extension_attributes/
│   ├── 01_extension_basics.ipynb
│   ├── 02_default_values.ipynb
│   ├── 03_getter_extensions.ipynb
│   ├── 04_method_extensions.ipynb
│   ├── 05_extension_patterns.ipynb
│   └── 06_serializing_extensions.ipynb
│
├── 12_custom_tokenization/
│   ├── 01_tokenizer_explained.ipynb
│   ├── 02_special_cases.ipynb
│   ├── 03_prefix_suffix_infix.ipynb
│   ├── 04_token_match.ipynb
│   ├── 05_custom_tokenizer.ipynb
│   └── 06_retokenization.ipynb
│
├── 13_training_fundamentals/
│   ├── 01_training_overview.ipynb
│   ├── 02_training_data_format.ipynb
│   ├── 03_config_system.ipynb
│   ├── 04_training_workflow.ipynb
│   ├── 05_training_metrics.ipynb
│   └── 06_training_tips.ipynb
│
├── 14_training_ner/
│   ├── 01_ner_training_data.ipynb
│   ├── 02_annotation_tools.ipynb
│   ├── 03_ner_config.ipynb
│   ├── 04_training_ner.ipynb
│   ├── 05_updating_ner.ipynb
│   └── 06_ner_evaluation.ipynb
│
├── 15_training_textcat/
│   ├── 01_textcat_overview.ipynb
│   ├── 02_textcat_data.ipynb
│   ├── 03_textcat_architectures.ipynb
│   ├── 04_training_textcat.ipynb
│   ├── 05_multilabel_textcat.ipynb
│   └── 06_textcat_evaluation.ipynb
│
├── 16_advanced_training/
│   ├── 01_training_multiple_components.ipynb
│   ├── 02_transfer_learning.ipynb
│   ├── 03_data_augmentation.ipynb
│   ├── 04_active_learning.ipynb
│   ├── 05_distributed_training.ipynb
│   └── 06_experiment_tracking.ipynb
│
├── 17_spacy_transformers/
│   ├── 01_transformers_intro.ipynb
│   ├── 02_spacy_transformers_setup.ipynb
│   ├── 03_using_trf_models.ipynb
│   ├── 04_transformer_embeddings.ipynb
│   ├── 05_trf_vs_static.ipynb
│   └── 06_custom_transformers.ipynb
│
├── 18_training_with_transformers/
│   ├── 01_trf_training_config.ipynb
│   ├── 02_trf_ner.ipynb
│   ├── 03_trf_textcat.ipynb
│   ├── 04_frozen_vs_finetuned.ipynb
│   ├── 05_memory_optimization.ipynb
│   └── 06_trf_best_practices.ipynb
│
├── 19_performance_optimization/
│   ├── 01_profiling.ipynb
│   ├── 02_disabling_components.ipynb
│   ├── 03_batch_processing.ipynb
│   ├── 04_multiprocessing.ipynb
│   ├── 05_memory_management.ipynb
│   └── 06_gpu_acceleration.ipynb
│
├── 20_serialization_deployment/
│   ├── 01_saving_loading_models.ipynb
│   ├── 02_serializing_docs.ipynb
│   ├── 03_model_packaging.ipynb
│   ├── 04_api_deployment.ipynb
│   ├── 05_docker_deployment.ipynb
│   └── 06_cloud_deployment.ipynb
│
├── 21_spacy_projects/
│   ├── 01_projects_overview.ipynb
│   ├── 02_project_yml.ipynb
│   ├── 03_data_assets.ipynb
│   ├── 04_custom_commands.ipynb
│   ├── 05_dvc_integration.ipynb
│   └── 06_project_templates.ipynb
│
├── 22_multilingual/
│   ├── 01_multilingual_models.ipynb
│   ├── 02_language_detection.ipynb
│   ├── 03_cross_lingual.ipynb
│   ├── 04_chinese_japanese.ipynb
│   ├── 05_rtl_languages.ipynb
│   └── 06_low_resource.ipynb
│
├── 23_information_extraction/
│   ├── 01_relation_extraction.ipynb
│   ├── 02_event_extraction.ipynb
│   ├── 03_coreference.ipynb
│   ├── 04_entity_linking.ipynb
│   ├── 05_knowledge_graphs.ipynb
│   └── 06_template_filling.ipynb
│
├── 24_document_processing/
│   ├── 01_document_structure.ipynb
│   ├── 02_large_documents.ipynb
│   ├── 03_pdf_processing.ipynb
│   ├── 04_corpus_analysis.ipynb
│   ├── 05_document_similarity.ipynb
│   └── 06_summarization.ipynb
│
├── 25_integration_ecosystem/
│   ├── 01_huggingface_integration.ipynb
│   ├── 02_scikit_learn.ipynb
│   ├── 03_pandas_integration.ipynb
│   ├── 04_visualization_tools.ipynb
│   ├── 05_streamlit_apps.ipynb
│   └── 06_prodigy.ipynb
│
├── 26_capstone_projects/
│   ├── 01_resume_parser.ipynb
│   ├── 02_news_analyzer.ipynb
│   ├── 03_customer_feedback.ipynb
│   ├── 04_legal_document_analysis.ipynb
│   ├── 05_medical_ner.ipynb
│   ├── 06_chatbot_nlu.ipynb
│   ├── 07_search_engine.ipynb
│   └── 08_content_moderation.ipynb
│
├── data/
│   ├── sample_texts/
│   ├── training_data/
│   └── models/
│
├── utils/
│   ├── helpers.py
│   └── visualization.py
│
└── assets/
    └── images/
```

---

## 📊 Quick Reference

### spaCy Models Comparison

| Model | Size | Vectors | Speed | Accuracy | Use Case |
|-------|------|---------|-------|----------|----------|
| `en_core_web_sm` | 12 MB | ❌ | ⚡⚡⚡ | ⭐⭐ | Prototyping, simple tasks |
| `en_core_web_md` | 40 MB | ✅ 300d | ⚡⚡ | ⭐⭐⭐ | General use |
| `en_core_web_lg` | 560 MB | ✅ 300d | ⚡⚡ | ⭐⭐⭐⭐ | Best accuracy (non-trf) |
| `en_core_web_trf` | 400 MB | ✅ Contextual | ⚡ | ⭐⭐⭐⭐⭐ | State-of-the-art |

### Entity Types Quick Reference

| Entity | Description | Example |
|--------|-------------|---------|
| PERSON | Named person | "Elon Musk" |
| ORG | Organization | "Google" |
| GPE | Geopolitical entity | "France" |
| LOC | Non-GPE location | "Mount Everest" |
| DATE | Date/period | "January 2024" |
| TIME | Time | "3:00 PM" |
| MONEY | Monetary value | "$1 million" |
| PERCENT | Percentage | "25%" |
| PRODUCT | Product name | "iPhone 15" |
| EVENT | Named event | "World Cup" |
| WORK_OF_ART | Title of work | "Mona Lisa" |
| LAW | Legal document | "GDPR" |
| LANGUAGE | Language | "English" |

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- [spaCy Documentation](https://spacy.io/usage)
- [Explosion AI](https://explosion.ai)
- [Advanced NLP with spaCy Course](https://course.spacy.io)

---

<p align="center">
  <b>Happy Learning! 🚀</b><br>
  <i>Star ⭐ this repo if you find it helpful!</i>
</p>
