import re
import json
import uuid
from pathlib import Path

SEP_RE = re.compile(r'^# <(.*)>[ \t]*$')

NOTEBOOK_METADATA = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.8.0"
    }
}


def _cell_id():
    return uuid.uuid4().hex[:8]


def _make_code_cell(lines):
    return {
        "cell_type": "code",
        "id": _cell_id(),
        "metadata": {},
        "source": lines,
        "outputs": [],
        "execution_count": None
    }


def _make_markdown_cell(content):
    text = content.replace(r'\n', '\n')
    lines = text.splitlines(keepends=True)
    if lines and lines[-1].endswith('\n'):
        lines[-1] = lines[-1].rstrip('\n')
    return {
        "cell_type": "markdown",
        "id": _cell_id(),
        "metadata": {},
        "source": lines
    }


def _flush_code(cells, current_lines):
    while current_lines and current_lines[0].strip() == '':
        current_lines.pop(0)
    while current_lines and current_lines[-1].strip() == '':
        current_lines.pop()
    if current_lines:
        cells.append(_make_code_cell(list(current_lines)))


def convert_py_to_nb(source: str) -> dict:
    cells = []
    current_lines = []

    for raw_line in source.splitlines(keepends=True):
        line_stripped = raw_line.rstrip('\n').rstrip('\r')
        m = SEP_RE.match(line_stripped)
        if m:
            _flush_code(cells, current_lines)
            current_lines.clear()
            md_content = m.group(1).strip()
            if md_content:
                cells.append(_make_markdown_cell(md_content))
        else:
            current_lines.append(raw_line)

    _flush_code(cells, current_lines)

    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": NOTEBOOK_METADATA,
        "cells": cells
    }


def py_to_nb_file(input_path, output_path=None):
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.with_suffix('.ipynb')
    else:
        output_path = Path(output_path)

    source = input_path.read_text(encoding='utf-8')
    notebook = convert_py_to_nb(source)
    output_path.write_text(json.dumps(notebook, indent=1), encoding='utf-8')
    return output_path
