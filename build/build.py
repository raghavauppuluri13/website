from pathlib import Path
import hashlib
import os
import tempfile
import shutil

from utils import read_lines, write_lines, run_command, make_tmp_copy
from preprocess import preprocess_lines

root_dir = Path().absolute()


def preprocess(file: Path):
    tmp_file = make_tmp_copy(file)
    lines = read_lines(file)
    lines = preprocess_lines(lines, file, root_dir)
    write_lines(tmp_file, lines)
    return tmp_file


def build_html(file: Path):
    file = Path(file)
    assert file.exists(), f"File {file} does not exist"
    tmp_file = preprocess(file)

    html_file = file.parent / file.name.replace(".md", ".html")
    print(f"{file} -> {html_file}")
    # os.system(f"cat {tmp_file}")
    run_command(
        f"pandoc -f markdown+raw_attribute+raw_html -t html --filter ./build/css_filter.py {tmp_file} -o {html_file}"
    )
    Path(tmp_file).unlink()


ignore_files = ["README.md"]

# grab all .md files recursively and exclude venv

md_files = list(Path(".").glob("**/*.md"))
md_files = [f for f in md_files if "venv" not in str(f)]

# remove the files we don't want to convert
for ignore_file in [Path(e) for e in ignore_files]:
    if ignore_file in md_files:
        md_files.remove(ignore_file)

# run the rest of the files through pandoc
for md_file in md_files:
    build_html(md_file)
