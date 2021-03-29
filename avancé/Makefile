SRCS := $(sort $(wildcard *-*.md))

.PHONY: help
help:
	@echo "Usage:"
	@echo "  make static  # to build static version."
	@echo "  make test  # to run tests."
	@echo "  make rsync  # rsync to prod"
	@echo "  make clean"

.PHONY: check
test:
	python test.py *.md

.PHONY: static
static: output/index.html

%.html: %.md
	mdtoreveal $< -o $@

output/index.md: $(SRCS)
	mkdir -p output
	cat $(SRCS) > output/index.md

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk@mdk.fr:/var/www/mdk.fr/python-avancé/

.PHONY: clean
clean:
	rm -fr output
