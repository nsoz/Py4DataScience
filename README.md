# Python for Data Science

![Python](https://img.shields.io/badge/language-Python%203-blue.svg)
![School](https://img.shields.io/badge/school-42-black.svg)

A project from the 42 School curriculum, an introduction to Python built as a bridge toward data science: after months of low-level C and manual memory management, this project covers Python's core data structures, standard idioms, and packaging tools — the language most of the data science ecosystem (NumPy, pandas, etc.) is built on.

## Exercises

| Exercise | Topic | Description |
|----------|-------|-------------|
| `ex00` | Built-in data structures | Mutating `list`, `tuple`, `set`, and `dict`, and understanding which are mutable and which aren't |
| `ex01` | Time handling | Formatting a Unix timestamp with `time`/`datetime`, including scientific notation |
| `ex02` | Type introspection | `all_thing_is_obj` — detecting an object's type at runtime with `isinstance` |
| `ex03` | "Null-like" values | `NULL_not_found` — distinguishing `None`, `NaN`, `0`, `""`, and `False`, values that are all "falsy" but semantically different |
| `ex04` | CLI argument handling | `whatis` — validating and parsing a single command-line integer argument, even/odd check |
| `ex05` | String analysis | `building` — counting uppercase, lowercase, digit, punctuation, and whitespace characters in a string |
| `ex06` | Functional programming | A from-scratch `ft_filter` (a simplified `filter()`) applied to filter words in a string by length |
| `ex07` | Text processing | `sos` — a Morse code encoder/decoder |
| `ex08` | Generators & iterators | `ft_tqdm` — a from-scratch reimplementation of the `tqdm` progress bar, showing percentage, elapsed time, ETA, and speed |
| `ex09` | Packaging | `ft_package` — a real installable Python package (`pyproject.toml`, `setuptools`, MIT license) exposing a `count_in_list` function, built and distributed as a wheel/sdist |

## Usage

Most exercises run directly:

```sh
python3 ex04/whatis.py 12
python3 ex06/filterstring.py "a bird flew" 3
python3 ex07/sos.py "SOS"
```

`ex09` is a proper package — build and install it locally:

```sh
cd ex09
python -m venv venv && source venv/bin/activate
pip install build
python -m build
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

```python
from ft_package import count_in_list
count_in_list(["a", "b", "a"], "a")  # 2
```

## Context

Part of the [42 School](https://42.fr/) curriculum — the introduction to Python and the first step toward its data science module track.
