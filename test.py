#!/usr/bin/env python3

import argparse
import re
import doctest
from tempfile import NamedTemporaryFile
import importlib.util

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="+")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

for file_to_test in args.file:
    with open(file_to_test) as f:
        source = f.read()

    with NamedTemporaryFile(mode="w", suffix=".py") as f:
        for example in re.findall("```python.*?```", source, re.S):
            example = "\n".join(example.split("\n")[1:-1])
            if example.startswith(">>> "):
                if '"""' in example:
                    f.write("""def _():\n    '''""" + example + """\n'''\n\n""")
                else:
                    f.write('''def _():\n    """''' + example + '''\n"""\n\n''')
            else:
                f.write(example + "\n\n")
        f.flush()
        spec = importlib.util.spec_from_file_location("to_test", f.name)
        to_test = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(to_test)
        doctest.testmod(to_test, verbose=args.verbose)
