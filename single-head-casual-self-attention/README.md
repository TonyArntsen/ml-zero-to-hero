# Single-Head Causal Self-Attention

This area focuses on the core attention mechanism used in transformer models, especially the single-head, causal version where each token can only attend to earlier tokens.

## Good sources to look up
- Attention Is All You Need by Vaswani et al.
- GPT papers and transformer notes
- Karpathy's attention and transformer walkthroughs
- Minimal attention implementation tutorials and derivations

## Handy math concepts
- Linear algebra: matrices, vectors, projections, and dot products
- Softmax and probability distributions
- Scaled dot-product attention
- Causal masking and sequence modeling
- Matrix shape reasoning and broadcasting
- Cross-entropy and optimization during training

## Typical things to practice
- Computing attention scores from queries, keys, and values
- Applying causal masks to prevent future leakage
- Understanding multi-head attention as an extension of the same idea
- Training a tiny causal transformer on short text
- Interpreting attention matrices and token relationships
