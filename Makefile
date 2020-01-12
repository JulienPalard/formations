SRCS := $(wildcard *-*.md)
HTML := $(addprefix output/,$(SRCS:.md=.html))

.PHONY: check
test:
	python test.py *.md

index.md:
	for file in *-*.md; do printf "%s\n\n" "$$file"; grep '^#' "$$file" | sed 's/.md:/  /;s/^/    /'; printf "\n\n"; done | uniq > $@

.PHONY: static
static: $(HTML)
	rm -f output/index.html
	cp index.html output/index.html
	cd output; printf "%s\n" *-*.html | sed 's#.*#<li><a href="\0">\0</a></li>#g' >> index.html

output/%.html: %.md node_modules/.bin/reveal-md
	./node_modules/.bin/reveal-md $< --theme simple --css static/fifix.css --highlight-theme github --static output/

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk@mdk.fr:/var/www/mdk.fr/python-initiation/

.PHONY: serve
serve: node_modules/.bin/reveal-md
	./node_modules/.bin/reveal-md $(FILE) -w --theme simple --css static/fifix.css --highlight-theme github

node_modules/.bin/reveal-md:
	npm i reveal-md

.PHONY: clean
clean:
	rm -fr output
