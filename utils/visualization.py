"""
spaCy Learning Guide - Visualization Utilities
===============================================

Custom visualization functions for spaCy analysis.
"""

import spacy
from spacy.tokens import Doc, Span
from spacy import displacy
from typing import List, Dict, Any, Optional
import html


# =============================================================================
# DISPLACY HELPERS
# =============================================================================

def render_entities(
    doc: Doc,
    colors: Optional[Dict[str, str]] = None,
    jupyter: bool = True
) -> Optional[str]:
    """
    Render entity visualization with custom colors.
    
    Args:
        doc: spaCy Doc object
        colors: Dictionary mapping entity labels to colors
        jupyter: Whether to render in Jupyter (True) or return HTML (False)
        
    Returns:
        HTML string if jupyter=False, else renders in notebook
    """
    default_colors = {
        "PERSON": "#aa9cfc",
        "ORG": "#7aecec",
        "GPE": "#feca74",
        "LOC": "#ff9561",
        "DATE": "#bfeeb7",
        "TIME": "#bfeeb7",
        "MONEY": "#e4e7d2",
        "PRODUCT": "#ff8197",
        "EVENT": "#ffeb80",
        "WORK_OF_ART": "#f0d0ff",
        "LAW": "#d2e8d4",
        "LANGUAGE": "#b4d4e5",
        "PERCENT": "#c4e0d9",
        "QUANTITY": "#c4e0d9",
        "CARDINAL": "#c4e0d9",
        "ORDINAL": "#c4e0d9",
    }
    
    if colors:
        default_colors.update(colors)
    
    options = {"colors": default_colors}
    
    if jupyter:
        displacy.render(doc, style="ent", options=options, jupyter=True)
        return None
    else:
        return displacy.render(doc, style="ent", options=options)


def render_dependencies(
    doc: Doc,
    compact: bool = False,
    jupyter: bool = True
) -> Optional[str]:
    """
    Render dependency visualization.
    
    Args:
        doc: spaCy Doc object
        compact: Use compact mode
        jupyter: Whether to render in Jupyter (True) or return HTML (False)
        
    Returns:
        HTML string if jupyter=False, else renders in notebook
    """
    options = {
        "compact": compact,
        "bg": "#ffffff",
        "color": "#000000",
        "font": "Arial"
    }
    
    if jupyter:
        displacy.render(doc, style="dep", options=options, jupyter=True)
        return None
    else:
        return displacy.render(doc, style="dep", options=options)


def render_sentence_dependencies(
    doc: Doc,
    sent_idx: int = 0,
    jupyter: bool = True
) -> Optional[str]:
    """
    Render dependencies for a specific sentence.
    
    Args:
        doc: spaCy Doc object
        sent_idx: Index of sentence to render
        jupyter: Whether to render in Jupyter
        
    Returns:
        HTML string if jupyter=False
    """
    sents = list(doc.sents)
    if sent_idx >= len(sents):
        raise ValueError(f"Sentence index {sent_idx} out of range (0-{len(sents)-1})")
    
    sent = sents[sent_idx]
    sent_doc = sent.as_doc()
    
    return render_dependencies(sent_doc, jupyter=jupyter)


# =============================================================================
# CUSTOM TEXT VISUALIZATIONS
# =============================================================================

def highlight_entities_html(doc: Doc, colors: Optional[Dict[str, str]] = None) -> str:
    """
    Create simple HTML with highlighted entities.
    
    Args:
        doc: spaCy Doc object
        colors: Dictionary mapping entity labels to colors
        
    Returns:
        HTML string with highlighted entities
    """
    default_colors = {
        "PERSON": "#aa9cfc",
        "ORG": "#7aecec",
        "GPE": "#feca74",
        "DATE": "#bfeeb7",
        "MONEY": "#e4e7d2",
    }
    
    if colors:
        default_colors.update(colors)
    
    text = doc.text
    result = []
    last_idx = 0
    
    for ent in sorted(doc.ents, key=lambda e: e.start_char):
        # Add text before entity
        result.append(html.escape(text[last_idx:ent.start_char]))
        
        # Add highlighted entity
        color = default_colors.get(ent.label_, "#ddd")
        result.append(
            f'<mark style="background-color: {color}; padding: 2px 4px; '
            f'border-radius: 3px;">{html.escape(ent.text)}'
            f'<sub style="font-size: 0.7em; color: #666;"> {ent.label_}</sub></mark>'
        )
        
        last_idx = ent.end_char
    
    # Add remaining text
    result.append(html.escape(text[last_idx:]))
    
    return "".join(result)


def highlight_pos_html(doc: Doc, target_pos: List[str]) -> str:
    """
    Create HTML with highlighted parts of speech.
    
    Args:
        doc: spaCy Doc object
        target_pos: List of POS tags to highlight
        
    Returns:
        HTML string with highlighted POS tags
    """
    pos_colors = {
        "NOUN": "#a8d8ea",
        "VERB": "#aa96da",
        "ADJ": "#fcbad3",
        "ADV": "#ffffd2",
        "PROPN": "#a8e6cf",
    }
    
    result = []
    for token in doc:
        if token.pos_ in target_pos:
            color = pos_colors.get(token.pos_, "#ddd")
            result.append(
                f'<mark style="background-color: {color}; padding: 1px 3px; '
                f'border-radius: 2px;">{html.escape(token.text_with_ws)}</mark>'
            )
        else:
            result.append(html.escape(token.text_with_ws))
    
    return "".join(result)


# =============================================================================
# ASCII VISUALIZATIONS
# =============================================================================

def ascii_dependency_tree(doc: Doc) -> str:
    """
    Create an ASCII representation of the dependency tree.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        ASCII tree string
    """
    lines = []
    
    for sent in doc.sents:
        # Find root
        root = [token for token in sent if token.head == token][0]
        
        def print_tree(token, depth=0):
            indent = "  " * depth
            connector = "└─ " if depth > 0 else ""
            lines.append(f"{indent}{connector}{token.text} [{token.dep_}]")
            
            for child in token.children:
                print_tree(child, depth + 1)
        
        print_tree(root)
        lines.append("")
    
    return "\n".join(lines)


def ascii_entity_chart(doc: Doc) -> str:
    """
    Create an ASCII chart of entity distribution.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        ASCII chart string
    """
    from collections import Counter
    
    counts = Counter(ent.label_ for ent in doc.ents)
    
    if not counts:
        return "No entities found."
    
    max_count = max(counts.values())
    max_label_len = max(len(label) for label in counts.keys())
    
    lines = ["Entity Distribution:", "-" * 40]
    
    for label, count in sorted(counts.items(), key=lambda x: -x[1]):
        bar_len = int(count / max_count * 20)
        bar = "█" * bar_len
        lines.append(f"{label.ljust(max_label_len)} | {bar} ({count})")
    
    return "\n".join(lines)


def ascii_pos_chart(doc: Doc) -> str:
    """
    Create an ASCII chart of POS tag distribution.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        ASCII chart string
    """
    from collections import Counter
    
    counts = Counter(token.pos_ for token in doc if not token.is_space)
    
    max_count = max(counts.values())
    max_label_len = max(len(label) for label in counts.keys())
    
    lines = ["POS Tag Distribution:", "-" * 40]
    
    for label, count in sorted(counts.items(), key=lambda x: -x[1]):
        bar_len = int(count / max_count * 20)
        bar = "█" * bar_len
        lines.append(f"{label.ljust(max_label_len)} | {bar} ({count})")
    
    return "\n".join(lines)


# =============================================================================
# COMPARISON VISUALIZATIONS
# =============================================================================

def side_by_side_entities(doc1: Doc, doc2: Doc) -> str:
    """
    Compare entities from two documents side by side.
    
    Args:
        doc1: First spaCy Doc
        doc2: Second spaCy Doc
        
    Returns:
        Comparison string
    """
    lines = []
    lines.append(f"{'Document 1':<40} | {'Document 2':<40}")
    lines.append("-" * 83)
    
    ents1 = [(e.text, e.label_) for e in doc1.ents]
    ents2 = [(e.text, e.label_) for e in doc2.ents]
    
    max_len = max(len(ents1), len(ents2))
    
    for i in range(max_len):
        left = f"{ents1[i][0]} ({ents1[i][1]})" if i < len(ents1) else ""
        right = f"{ents2[i][0]} ({ents2[i][1]})" if i < len(ents2) else ""
        lines.append(f"{left:<40} | {right:<40}")
    
    return "\n".join(lines)


# =============================================================================
# NETWORK VISUALIZATIONS
# =============================================================================

def create_entity_cooccurrence_graph(doc: Doc) -> Dict[str, Any]:
    """
    Create entity co-occurrence data for network visualization.
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        Dictionary with nodes and edges for visualization
    """
    nodes = []
    edges = []
    seen_entities = {}
    
    # Get entities per sentence
    for sent in doc.sents:
        sent_ents = [ent for ent in doc.ents 
                    if ent.start >= sent.start and ent.end <= sent.end]
        
        # Add nodes
        for ent in sent_ents:
            if ent.text not in seen_entities:
                seen_entities[ent.text] = len(nodes)
                nodes.append({
                    "id": len(nodes),
                    "label": ent.text,
                    "type": ent.label_
                })
        
        # Add edges (co-occurrence within sentence)
        for i, ent1 in enumerate(sent_ents):
            for ent2 in sent_ents[i+1:]:
                edges.append({
                    "source": seen_entities[ent1.text],
                    "target": seen_entities[ent2.text]
                })
    
    return {"nodes": nodes, "edges": edges}


# =============================================================================
# EXPORT FUNCTIONS
# =============================================================================

def save_visualization(html_content: str, filepath: str) -> None:
    """
    Save HTML visualization to file.
    
    Args:
        html_content: HTML string
        filepath: Output file path
    """
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>spaCy Visualization</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)


if __name__ == "__main__":
    # Test visualizations
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple Inc. was founded by Steve Jobs in California. The company makes the iPhone.")
    
    print("=" * 60)
    print("ASCII DEPENDENCY TREE")
    print("=" * 60)
    print(ascii_dependency_tree(doc))
    
    print("\n" + "=" * 60)
    print("ASCII ENTITY CHART")
    print("=" * 60)
    print(ascii_entity_chart(doc))
    
    print("\n" + "=" * 60)
    print("ASCII POS CHART")
    print("=" * 60)
    print(ascii_pos_chart(doc))
