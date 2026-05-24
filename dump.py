import nbformat

with open("Bayesian A-B Test - Notebook.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == "code":
        print(f"\n--- Cell {i} ---")
        lines = cell.source.split('\n')
        for idx, line in enumerate(lines):
            print(f"{idx+1:03d}: {line}")
