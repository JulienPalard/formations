.PHONY: help
help:
	@echo "Usage:"
	@echo "  make static  # to build static version."
	@echo "  make test  # to run tests."
	@echo "  make rsync  # rsync to prod"
	@echo "  make clean"

.PHONY: static
static: output/drf.html

.PHONY: check
test:
	python test.py *.md

output/%.html: %.md
	mdtoreveal $< --output $@
	cp -a static output

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk_fr@mdk.fr:/var/www/mdk.fr/drf-initiation/

.PHONY: clean
clean:
	rm -fr output/

.PHONY: serve
serve:
	python -m http.server -d output/
