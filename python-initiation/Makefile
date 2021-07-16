SRCS := $(wildcard *-*.md)
HTML := $(addprefix output/,$(SRCS:.md=.html))

.PHONY: static
static: $(HTML) index.html
	rm -f output/index.html
	cp index.html output/index.html

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

index.md: $(SRCS)
	for file in *-*.md; \
	    do printf "# [%s](%s)\n\n" "$$file" "$$(printf "%s" "$$file" | sed s/.md/.html/)"; \
	    grep -h '^#' "$$file" | sed 's/^# /- /;s/^## /    - /'; \
	done | uniq > $@

index.html: index.md
	mkdir -p output
	python -m markdown -o html $< -f $@

output/%.html: %.md $(REVEAL_JS)
	mdtoreveal $< --output $@
	cp -a static output

.PHONY: rsync
rsync: static
	rsync -vah --delete output/ mdk_fr@mdk.fr:/var/www/mdk.fr/python-initiation/

.PHONY: clean
clean:
	rm -f output/*.html index.md index.html
