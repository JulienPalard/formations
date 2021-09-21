.PHONY: help
help:
	@echo "Usage:"
	@echo "  make static  # to build static version."
	@echo "  make test  # to run tests."
	@echo "  make rsync  # rsync to prod"
	@echo "  make clean"

.PHONY: static
static: output/index.html

.PHONY: check
test:
	python test.py *.md

%.html: %.md
	mdtoreveal $< --output $@

output/index.md: django.md
	mkdir -p output
	cat $< > $@

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk_fr@mdk.fr:/var/www/mdk.fr/django-initiation/

.PHONY: clean
clean:
	rm -fr output/

.PHONY: serve
serve:
	python -m http.server -d output/
