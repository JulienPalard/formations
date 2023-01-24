SRCS := $(sort $(wildcard *.md))
DEST := $(notdir $(PWD))

.PHONY: static
static: output/index.html
	if [ -d static ]; then cp -a static/ output/; fi

%.html: %.md
	sed 's/#!//e;' $< | mdtoreveal /dev/stdin --output $@

output/index.md: $(SRCS)
	mkdir -p output
	cat $(SRCS) > output/index.md

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk_fr@mdk.fr:/var/www/mdk.fr/$(DEST)/

.PHONY: clean
clean:
	rm -fr output

.PHONY: entr
entr:
	ls -1 *.md | entr $(MAKE) static

.PHONY: serve
serve: static
	python3 -m http.server -d output/

.PHONY: test
test:
	if [ -f test.py ]; then \
	    python test.py *.md; \
	fi
