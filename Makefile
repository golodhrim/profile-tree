MAN_SRC = $(wildcard *.1.md)
MAN_DST = $(MAN_SRC:.1.md=.1)

man: $(MAN_DST)

%.1: %.1.md
	pandoc -s -w man $< -o $@

.PHONY: clean

clean:
	@rm -vf $(MAN_DST)
