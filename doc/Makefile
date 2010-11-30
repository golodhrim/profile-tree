MAN_SRC = $(wildcard *.1.md)
MAN_DST = $(MAN_SRC:.1.md=.1)
HTML_SRC = $(wildcard *.md)
HTML_DST = $(HTML_SRC:.md=.html)

man: $(MAN_DST)

%.1: %.1.md
	pandoc -s -w man $< -o $@

html: $(HTML_DST)

%.html: %.md
	pandoc -s -w html $< -o $@

.PHONY: clean

clean:
	@rm -vf $(MAN_DST) $(HTML_DST)
