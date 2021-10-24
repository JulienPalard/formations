.PHONY: static
static: output/index.html

.PHONY: help
help:
	@echo "Usage:"
	@echo "  make static"
	@echo "  make test"
	@echo "  make rsync"
	@echo "  make clean"

.PHONY: check
test:
	python test.py *.md

output/index.html: initiation.md
	mdtoreveal $< --output $@
	cp -a static output

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk_fr@mdk.fr:/var/www/mdk.fr/python-initiation/

.PHONY: clean
clean:
	rm -f $(HTML)

.PHONY: serve
serve:
	python3 -m http.server -d output/
