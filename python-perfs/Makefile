export PATH := $(PATH):bin

# Only run watch with -j2 so entr and serve are run in parallel.
.PHONY: watch
watch: entr serve

.PHONY: static
static: output/index.html
	cp -a .cache/*.png output/

.PHONY: help
help:
	@echo "Usage:"
	@echo "  make static"
	@echo "  make test"
	@echo "  make rsync"
	@echo "  make clean"

.PHONY: entr
entr:
	ls -1 *.md include/*.py | entr $(MAKE) static

output/index.html: perfs.md
	mkdir -p .cache
	sed 's/#!//e;' perfs.md | mdtoreveal /dev/stdin --output $@
	if [ -d static ]; then cp -a static output; fi

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk_fr@mdk.fr:/var/www/mdk.fr/python-perfs/

.PHONY: clean
clean:
	rm -f $(HTML)

.PHONY: serve
serve:
	python3 -m http.server -d output/
