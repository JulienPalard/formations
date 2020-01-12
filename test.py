#!/usr/bin/env python3

import argparse
from string import ascii_letters, digits
import re
import doctest
from tempfile import NamedTemporaryFile
import importlib.util

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="+")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

for file_to_test in args.file:
    with open(file_to_test) as f:
        source = f.read()

    with NamedTemporaryFile(mode="w", suffix=".py") as f:
        for example_match in re.finditer("```python.*?```", source, re.S):
            example = example_match.group()
            example = "\n".join(example.split("\n")[1:-1])
            lineno = source[:example_match.start()].count("\n") + 1
            function_name = ''.join(letter if letter in ascii_letters + digits else '_' for letter in file_to_test[:-3]) + "_line_" + str(lineno)
            if example.startswith(">>> "):
                if '"""' in example:
                    f.write(f"""def _{function_name}():\n    r'''""" + example + """\n'''\n\n""")
                else:
                    f.write(f'''def _{function_name}():\n    r"""''' + example + '''\n"""\n\n''')
            else:
                f.write(example + "\n\n")
        f.flush()
        if args.debug:
            with open(f.name) as py_source:
                print(py_source.read())
        spec = importlib.util.spec_from_file_location("to_test", f.name)
        to_test = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(to_test)
        doctest.testmod(to_test, verbose=args.verbose)
