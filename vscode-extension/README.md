# py2nb VS Code Extension

Adds a one-click toolbar button to convert the active `.py` file to a Jupyter notebook.

Output is saved next to the source file with `_py2nb` appended:
```
myfile.py  →  myfile_py2nb.ipynb
```

---

## Prerequisites

- VS Code 1.74 or later
- Python with the `py2nb` package installed (step 1 below)

---

## Installation

### Step 1 — Install the Python package

```bash
pip install -e /rodata/osail/m309406/Current/py2nb/
```

Verify:
```bash
python -m py2nb --help
```

### Step 2 — Install the VS Code extension

**Option A — symlink** (recommended: edits to the extension take effect after a reload, no re-copy needed)

```bash
ln -s /rodata/osail/m309406/Current/py2nb/vscode-extension \
      ~/.vscode/extensions/py2nb-0.1.0
```

**Option B — copy**

```bash
cp -r /rodata/osail/m309406/Current/py2nb/vscode-extension \
      ~/.vscode/extensions/py2nb-0.1.0
```

### Step 3 — Reload VS Code

`Ctrl+Shift+P` → `Developer: Reload Window`

---

## Verify the button appears

1. Open any `.py` file
2. Look at the top-right toolbar — you should see a notebook icon **⊞**
3. The icon only appears when a `.py` file is the active editor

---

## Configure the Python interpreter

By default the extension calls `python`. If that is the wrong environment:

1. Open Settings: `Ctrl+,`
2. Search `py2nb`
3. Set **py2nb: Python Path** to the full interpreter path, e.g.:
   ```
   /rodata/osail/m309406/Envs/MyEnvs/BaseEnv/bin/python
   ```

To find your interpreter path:
```bash
which python
# or for conda:
conda activate myenv && which python
```

---

## Usage

1. Open a `.py` file
2. Click the notebook icon **⊞** in the top-right toolbar
3. The file is saved automatically, then converted
4. A popup appears — click **Open** to open the notebook immediately

### Cell separator syntax

| Comment | Result |
|---|---|
| `# <>` | Split into a new code cell |
| `# <Some text>` | Split + markdown cell "Some text" |
| `# <## Heading\nBody>` | Split + multi-line markdown (`\n` → real newline) |

Separators must start at column 0. Indented `    # <>` is a regular comment.

---

## Troubleshooting

**Button does not appear**
- Confirm the directory is named exactly `py2nb-0.1.0` inside `~/.vscode/extensions/`
- Run `Developer: Reload Window` and reopen a `.py` file

**`python: command not found`**
- Set `py2nb.pythonPath` to the full path of your Python interpreter (see above)

**`No module named py2nb`**
- The package is not installed in the interpreter the extension is using
- Run `pip install -e /rodata/osail/m309406/Current/py2nb/` with the same interpreter set in `py2nb.pythonPath`
- Verify with: `python -m py2nb --help`
