"""
spaCy Learning Guide - Utility Functions
========================================

Common helper functions used across notebooks.
"""

import spacy
from spacy.tokens import Doc, Token, Span
from typing import List, Dict, Tuple, Any, Optional
import json


# =============================================================================
# DISPLAY HELPERS
# =============================================================================

def print_tokens_table(doc: Doc, attributes: List[str] = None) -> None:
    """
    Print a formatted table of tokens with their attributes.
    
    Args:
        doc: spaCy Doc object
        attributes: List of token attributes to display
                   Default: ['text', 'lemma_', 'pos_', 'tag_', 'dep_', 'is_stop']
    """
    if attributes is None:
        attributes = ['text', 'lemma_', 'pos_', 'tag_', 'dep_', 'is_stop']
    
    # Calculate column widths
    widths = {attr: max(len(attr), max(len(str(getattr(t, attr))) for t in doc)) 
              for attr in attributes}
    
    # Print header
    header = " | ".join(attr.upper().ljust(widths[attr]) for attr in attributes)
    print(header)
    print("-" * len(header))
    
    # Print rows
    for token in doc:
        row = " | ".join(str(getattr(token, attr)).ljust(widths[attr]) 
                        for attr in attributes)
        print(row)


def print_entities_table(doc: Doc) -> None:
    """
    Print a formatted table of named entities.
    
    Args:
        doc: spaCy Doc object
    """
    if not doc.ents:
        print("No entities found.")
        return
    
    print(f"{'TEXT':<25} | {'LABEL':<15} | {'DESCRIPTION':<35} | {'START':<5} | {'END':<5}")
    print("-" * 95)
    
    for ent in doc.ents:
        description = spacy.explain(ent.label_) or "N/A"
        print(f"{ent.text:<25} | {ent.label_:<15} | {description:<35} | {ent.start:<5} | {ent.end:<5}")


def print_dependency_tree(doc: Doc) -> None:
    """
    Print a text-based dependency tree.
    
    Args:
        doc: spaCy Doc object
    """
    for token in doc:
        ancestors = " → ".join([t.text for t in token.ancestors])
        if ancestors:
            print(f"{token.text} ←[{token.dep_}]← {token.head.text} (ancestors: {ancestors})")
        else:
            print(f"{token.text} [ROOT]")


def print_noun_chunks(doc: Doc) -> None:
    """
    Print noun chunks with their properties.
    
    Args:
        doc: spaCy Doc object
    """
    if not list(doc.noun_chunks):
        print("No noun chunks found.")
        return
    
    print(f"{'CHUNK':<30} | {'ROOT':<15} | {'ROOT DEP':<12} | {'ROOT HEAD':<15}")
    print("-" * 80)
    
    for chunk in doc.noun_chunks:
        print(f"{chunk.text:<30} | {chunk.root.text:<15} | {chunk.root.dep_:<12} | {chunk.root.head.text:<15}")


# =============================================================================
# DATA EXTRACTION HELPERS
# =============================================================================

def extract_entities(doc: Doc) -> List[Dict[str, Any]]:
    """
    Extract entities as a list of dictionaries.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of entity dictionaries
    """
    return [
        {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start,
            "end": ent.end,
            "start_char": ent.start_char,
            "end_char": ent.end_char
        }
        for ent in doc.ents
    ]


def extract_tokens(doc: Doc, include_punct: bool = False) -> List[Dict[str, Any]]:
    """
    Extract token information as a list of dictionaries.
    
    Args:
        doc: spaCy Doc object
        include_punct: Whether to include punctuation tokens
        
    Returns:
        List of token dictionaries
    """
    tokens = []
    for token in doc:
        if not include_punct and token.is_punct:
            continue
        tokens.append({
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "is_stop": token.is_stop,
            "is_alpha": token.is_alpha
        })
    return tokens


def extract_sentences(doc: Doc) -> List[str]:
    """
    Extract sentences as a list of strings.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of sentence strings
    """
    return [sent.text.strip() for sent in doc.sents]


def extract_noun_chunks(doc: Doc) -> List[Dict[str, str]]:
    """
    Extract noun chunks with their properties.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of noun chunk dictionaries
    """
    return [
        {
            "text": chunk.text,
            "root": chunk.root.text,
            "root_dep": chunk.root.dep_,
            "root_head": chunk.root.head.text
        }
        for chunk in doc.noun_chunks
    ]


# =============================================================================
# ANALYSIS HELPERS
# =============================================================================

def get_entity_counts(doc: Doc) -> Dict[str, int]:
    """
    Get counts of each entity type.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        Dictionary mapping entity labels to counts
    """
    counts = {}
    for ent in doc.ents:
        counts[ent.label_] = counts.get(ent.label_, 0) + 1
    return counts


def get_pos_counts(doc: Doc) -> Dict[str, int]:
    """
    Get counts of each POS tag.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        Dictionary mapping POS tags to counts
    """
    counts = {}
    for token in doc:
        counts[token.pos_] = counts.get(token.pos_, 0) + 1
    return counts


def get_token_stats(doc: Doc) -> Dict[str, Any]:
    """
    Get statistics about tokens in the document.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        Dictionary with various token statistics
    """
    tokens = [t for t in doc if not t.is_space]
    words = [t for t in tokens if t.is_alpha]
    
    return {
        "total_tokens": len(tokens),
        "total_words": len(words),
        "unique_words": len(set(t.lower_ for t in words)),
        "sentences": len(list(doc.sents)),
        "entities": len(doc.ents),
        "noun_chunks": len(list(doc.noun_chunks)),
        "avg_word_length": sum(len(t.text) for t in words) / len(words) if words else 0,
        "stop_word_ratio": sum(1 for t in words if t.is_stop) / len(words) if words else 0
    }


def find_similar_tokens(doc: Doc, target: str, threshold: float = 0.5) -> List[Tuple[str, float]]:
    """
    Find tokens similar to a target word.
    
    Args:
        doc: spaCy Doc object
        target: Target word to compare
        threshold: Minimum similarity threshold
        
    Returns:
        List of (token_text, similarity_score) tuples
    """
    nlp = doc.vocab
    target_token = doc.vocab[target]
    
    if not target_token.has_vector:
        return []
    
    similar = []
    seen = set()
    
    for token in doc:
        if token.text.lower() in seen:
            continue
        if token.has_vector and token.text.lower() != target.lower():
            sim = token.similarity(target_token)
            if sim >= threshold:
                similar.append((token.text, sim))
                seen.add(token.text.lower())
    
    return sorted(similar, key=lambda x: x[1], reverse=True)


# =============================================================================
# PATTERN MATCHING HELPERS
# =============================================================================

def create_entity_pattern(label: str, texts: List[str]) -> List[Dict]:
    """
    Create patterns for EntityRuler from a list of texts.
    
    Args:
        label: Entity label
        texts: List of text patterns
        
    Returns:
        List of pattern dictionaries
    """
    return [{"label": label, "pattern": text} for text in texts]


def pattern_to_string(pattern: List[Dict]) -> str:
    """
    Convert a Matcher pattern to a readable string.
    
    Args:
        pattern: Matcher pattern (list of dictionaries)
        
    Returns:
        Human-readable pattern string
    """
    parts = []
    for token_pattern in pattern:
        token_str = []
        for key, value in token_pattern.items():
            token_str.append(f"{key}={value}")
        parts.append("{" + ", ".join(token_str) + "}")
    return " ".join(parts)


# =============================================================================
# TRAINING DATA HELPERS
# =============================================================================

def convert_to_spacy_format(
    texts: List[str],
    annotations: List[List[Tuple[int, int, str]]]
) -> List[Tuple[str, Dict]]:
    """
    Convert annotation data to spaCy training format.
    
    Args:
        texts: List of text strings
        annotations: List of annotation lists [(start, end, label), ...]
        
    Returns:
        List of (text, {"entities": [...]}) tuples
    """
    training_data = []
    for text, ents in zip(texts, annotations):
        training_data.append((text, {"entities": ents}))
    return training_data


def validate_training_data(training_data: List[Tuple[str, Dict]], nlp) -> List[str]:
    """
    Validate training data for common issues.
    
    Args:
        training_data: Training data in spaCy format
        nlp: spaCy language model
        
    Returns:
        List of warning messages
    """
    warnings = []
    
    for i, (text, annotations) in enumerate(training_data):
        entities = annotations.get("entities", [])
        
        # Check for overlapping entities
        sorted_ents = sorted(entities, key=lambda x: x[0])
        for j in range(len(sorted_ents) - 1):
            if sorted_ents[j][1] > sorted_ents[j + 1][0]:
                warnings.append(f"Example {i}: Overlapping entities")
        
        # Check for misaligned entities
        doc = nlp.make_doc(text)
        for start, end, label in entities:
            span = doc.char_span(start, end)
            if span is None:
                warnings.append(f"Example {i}: Entity '{text[start:end]}' not aligned with tokens")
    
    return warnings


# =============================================================================
# FILE HELPERS
# =============================================================================

def save_patterns_jsonl(patterns: List[Dict], filepath: str) -> None:
    """
    Save patterns to a JSONL file.
    
    Args:
        patterns: List of pattern dictionaries
        filepath: Output file path
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for pattern in patterns:
            f.write(json.dumps(pattern) + '\n')


def load_patterns_jsonl(filepath: str) -> List[Dict]:
    """
    Load patterns from a JSONL file.
    
    Args:
        filepath: Input file path
        
    Returns:
        List of pattern dictionaries
    """
    patterns = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                patterns.append(json.loads(line))
    return patterns


# =============================================================================
# COMPARISON HELPERS
# =============================================================================

def compare_docs(doc1: Doc, doc2: Doc) -> Dict[str, Any]:
    """
    Compare two documents and return differences.
    
    Args:
        doc1: First spaCy Doc
        doc2: Second spaCy Doc
        
    Returns:
        Dictionary with comparison results
    """
    return {
        "text_same": doc1.text == doc2.text,
        "token_count_diff": len(doc1) - len(doc2),
        "entity_count_diff": len(doc1.ents) - len(doc2.ents),
        "similarity": doc1.similarity(doc2) if doc1.has_vector and doc2.has_vector else None,
        "shared_entities": set(e.text for e in doc1.ents) & set(e.text for e in doc2.ents)
    }


if __name__ == "__main__":
    # Test the helpers
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple Inc. was founded by Steve Jobs in California. The company makes the iPhone.")
    
    print("=" * 60)
    print("TOKEN TABLE")
    print("=" * 60)
    print_tokens_table(doc)
    
    print("\n" + "=" * 60)
    print("ENTITY TABLE")
    print("=" * 60)
    print_entities_table(doc)
    
    print("\n" + "=" * 60)
    print("NOUN CHUNKS")
    print("=" * 60)
    print_noun_chunks(doc)
    
    print("\n" + "=" * 60)
    print("TOKEN STATS")
    print("=" * 60)
    stats = get_token_stats(doc)
    for key, value in stats.items():
        print(f"  {key}: {value}")
