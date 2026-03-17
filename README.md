# py2nb

Convert annotated `.py` files to Jupyter notebooks using special comment separators.

## Separator Syntax

| Comment | Result |
|---|---|
| `# <>` | End current code cell, start new code cell |
| `# <Some text>` | End code cell, insert markdown cell "Some text", start new code cell |
| `# <## Heading\nBody>` | Same, but `\n` expands to a real newline in the markdown |

**Rules:**
- Must start at column 0 — `    # <>` (indented) is a regular comment
- Nothing after the closing `>` except whitespace — `# <foo>bar` is a regular comment

## Quick Start

```bash
# Install (once)
pip install -e /rodata/osail/m309406/Current/py2nb/

# Convert
python -m py2nb myfile.py              # → myfile.ipynb
python -m py2nb myfile.py -o out.ipynb
```

## Example

```python
import numpy as np

# <## Data generation\nCreate a simple quadratic sequence>

x = np.arange(10)
y = x ** 2

# <>

print(y)
```

Produces three cells:
1. **Code** — `import numpy as np`
2. **Markdown** — two-line heading + body
3. **Code** — `x = np.arange(10)` … `print(y)`

## VS Code Extension

See [`vscode-extension/README.md`](vscode-extension/README.md) to add a one-click toolbar button.

## Python API

```python
from py2nb import convert_py_to_nb, py_to_nb_file

notebook_dict = convert_py_to_nb(source_string)
py_to_nb_file("input.py", "output.ipynb")   # output path is optional
```

## Package Structure

```
py2nb/
├── py2nb/
│   ├── __init__.py      # public API
│   ├── converter.py     # core logic
│   ├── cli.py           # argparse entry point
│   └── __main__.py      # enables python -m py2nb
├── vscode-extension/    # VS Code toolbar button
└── pyproject.toml
```

## Requirements

Python 3.8+. No third-party dependencies.
