SRCS := $(wildcard *-*.md)
HTML := $(addprefix output/,$(SRCS:.md=.html))
REVEAL_JS_VERSION := 3.9.2
REVEAL_JS := output/reveal.js-$(REVEAL_JS_VERSION)/up-to-date


.PHONY: help
help:
	@echo "Usage:"
	@echo "  make static  # to build static version."
	@echo "  make test  # to run tests."
	@echo "  make rsync  # rsync to prod"
	@echo "  make clean"

$(REVEAL_JS):
	mkdir -p output
	cd output; wget https://github.com/hakimel/reveal.js/archive/$(REVEAL_JS_VERSION).tar.gz
	cd output; tar -xzf $(REVEAL_JS_VERSION).tar.gz
	touch $(REVEAL_JS)

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

# To discover pandoc variables: less $(dpkg -L pandoc-data | grep reveal)
output/%.html: %.md $(REVEAL_JS)
	# cp -a output/reveal.js-$(REVEAL_JS_VERSION)/plugin/ output/
	python3 ../md2reveal/md2reveal.py --revealjs-url "reveal.js-$(REVEAL_JS_VERSION)" $< $@
	cp -a static output

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk@mdk.fr:/var/www/mdk.fr/python-initiation/

.PHONY: clean
clean:
	rm -f output/*.html index.md index.html
