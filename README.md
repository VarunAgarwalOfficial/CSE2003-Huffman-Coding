# Huffman Coding in Python

> **Archived.** Superseded by [huffman](https://github.com/VarunAgarwalOfficial/huffman), the Rust rewrite that compresses arbitrary files. This repository is kept as a record and is read-only.

A small Python implementation of Huffman coding. It reads a text file, counts how often each character appears, builds a Huffman tree and prints the input encoded as a string of 0s and 1s.

## Why it is interesting

- The tree is built greedily: the two least frequent nodes are repeatedly merged into a parent whose frequency is their sum, so frequent characters end up near the root and get shorter codes.
- Codes are read off the tree with a recursive walk that appends `0` for a left branch and `1` for a right branch, which shows why the result is a prefix-free code.
- It is deliberately simple: the queue is a list re-sorted after each merge (a hand-written O(n²) sort) rather than a heap, and it only encodes. There is no decoder and the output is a printed bit string, not a packed file.

## Run it

No dependencies beyond Python 3.

```bash
python engine.py
```

`engine.py` reads `text.txt` from the current directory, prints each character with its frequency, then prints the encoded bit string. Edit `text.txt` to try other input.

## Tech

Python 3, standard library only.

## Context

VIT coursework, CSE2003 Data Structures and Algorithms, J component, group project, Fall 2020. The original submission was written in C; this repository holds the Python version. A later rewrite in Rust: https://github.com/VarunAgarwalOfficial/huffman

## License

MIT, see LICENSE. This is the Python version; the group's original C submission is not included.
