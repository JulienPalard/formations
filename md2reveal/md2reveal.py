import re
from pathlib import Path
import jinja2
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("md", help="Markdown input file")
    parser.add_argument("html", help="HTML output file")
    parser.add_argument("--revealjs-url", help="Path or URL to revealjs")
    return parser.parse_args()

def main():
    args = parse_args()
    with open(Path(__file__).parent / "default.revealjs") as f:
        tpl = jinja2.Template(f.read())

    with open(args.md) as f:
        md = f.read()

    sections = []
    for section in re.split("^# ", md, flags=re.M):
        if not section:
            continue
        slides = []
        for slide in re.split("^## ", section, flags=re.M):
            slide = re.sub("^::: notes$", '<aside class="notes">', slide, flags=re.M)
            slide = re.sub("^:::$", "</aside>", slide, flags=re.M)
            slides.append('## ' + slide)
        sections.append(slides)

    with open(args.html, "w") as f:
        f.write(tpl.render(slides=sections, revealjs_url=args.revealjs_url))

main()
