# ft_package

A simple Python package that counts occurrences of items in a list.

## Description

This package provides the `count_in_list` function which counts how many times a specified item appears in a given list.

## Installation

You can install this package using pip:
```bash


python -m venv venv

source venv/bin/activate

pip install build

python -m build
```

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

or

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

# Count occurrences of an item in a list
result = count_in_list(["toto", "tata", "toto"], "toto")
print(result)  # Output: 2

result = count_in_list(["toto", "tata", "toto"], "tutu")
print(result)  # Output: 0
```

## Features

- Simple and efficient list item counting
- Easy to use function interface
- Lightweight package

## License

MIT License - See LICENSE file for details
