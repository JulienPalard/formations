SRCS := $(wildcard *-*.md)
HTML := $(addprefix output/,$(SRCS:.md=.html))

.PHONY: check
test:
	python test.py *.md

index.md: $(SRCS)
	for file in *-*.md; \
	    do printf "# [%s](%s)\n\n" "$$file" "$$(printf "%s" "$$file" | sed s/.md/.html/)"; \
	    grep -h '^#' "$$file" | sed 's/^# /- /;s/^## /    - /'; \
	done | uniq > $@

index.html: index.md
	mkdir -p output
	python -m markdown -o html $< -f $@

.PHONY: static
static: $(HTML) index.html
	rm -f output/index.html
	cp index.html output/index.html

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
	rm -fr output index.md index.html
