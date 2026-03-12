import json
import sys

def convert_notebook(ipynb_file, py_file):
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    with open(py_file, 'w', encoding='utf-8') as f:
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                for line in cell.get('source', []):
                    f.write(line)
                f.write('\n\n')

if __name__ == "__main__":
    convert_notebook(sys.argv[1], sys.argv[2])
