SRCS := $(sort $(wildcard *-*.md))
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

.PHONY: static
static: output/index.html

output/index.md: $(SRCS)
	mkdir -p output/
	cat $(SRCS) > output/index.md

# To discover pandoc variables: less $(dpkg -L pandoc-data | grep reveal)
output/index.html: output/index.md $(REVEAL_JS)
	python3 ../md2reveal/md2reveal.py --revealjs-url "reveal.js-$(REVEAL_JS_VERSION)" output/index.md output/index.html
	if [ -d static ]; then cp -a static output; fi

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk@mdk.fr:/var/www/mdk.fr/python-avancé/

.PHONY: clean
clean:
	rm -fr output
