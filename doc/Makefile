ETOOLS_VERSION ?= 0.2.1

prefix ?= /usr/local
bindir ?= $(prefix)/bin
mandir ?= $(prefix)/share/man
man1dir = $(mandir)/man1

INSTALL ?= install
RM ?= rm -f

ASCIIDOC = asciidoc
ASCIIDOC_CONF = asciidoc.conf
ASCIIDOC_EXTRA += -a asciidoc7compatible -a no-inline-literal
ASCIIDOC_EXTRA += -a git-asciidoc-no-roff

MANPAGE_XSL = manpage-normal.xsl

XMLTO_EXTRA =

MAN1_TXT = $(filter-out $(addsuffix .txt, $(ARTICLES)), $(wildcard *.txt))

MAN_TXT = $(MAN1_TXT)
MAN_XML = $(patsubst %.txt,%.xml,$(MAN_TXT))
MAN_HTML = $(patsubst %.txt,%.html,$(MAN_TXT))

DOC_MAN1 = $(patsubst %.txt,%.1,$(MAN1_TXT))
DOC_HTML = $(MAN_HTML)

ARTICLES = index

DOC_HTML += $(patsubst %,%.html,$(ARTICLES))

ifneq ($(findstring $(MAKEFLAGS),s),s)
ifndef V
	QUIET_ASCIIDOC	= @echo '   ' 'ASCIIDOC' $@;
	QUIET_XMLTO	= @echo '   ' 'XMLTO   ' $@;
	QUIET_DB2TEXI	= @echo '   ' 'DB2TEXI ' $@;
	QUIET_MAKEINFO	= @echo '   ' 'MAKEINFO' $@;
	QUIET_DBLATEX	= @echo '   ' 'DBLATEX ' $@;
	QUIET_XSLTPROC	= @echo '   ' 'XSLTPROC' $@;
	QUIET_GEN	= @echo '   ' 'GEN     ' $@;
	QUIET_STDERR	= 2> /dev/null
	QUIET_SUBDIR0	= +@subdir=
	QUIET_SUBDIR1	= ;$(NO_SUBDIR) echo '   ' SUBDIR $$subdir; \
			  $(MAKE) $(PRINT_DIR) -C $$subdir
	export V
endif
endif

all: html man

html: $(DOC_HTML)

$(DOC_HTML) $(DOC_MAN1): asciidoc.conf

man: man1
man1: $(DOC_MAN1)

$(MAN_HTML): %.html : %.txt
	$(QUIET_ASCIIDOC)$(RM) $@+ $@ && \
	$(ASCIIDOC) -b xhtml11 -d manpage -f asciidoc.conf \
		$(ASCIIDOC_EXTRA) -aetl_version=$(ETOOLS_VERSION) -o $@+ $< && \
	mv $@+ $@

%.1: %.xml
	$(QUIET_XMLTO)$(RM) $@ && \
	xmlto -m $(MANPAGE_XSL) $(XMLTO_EXTRA) man $<

%.xml: %.txt
	$(QUIET_ASCIIDOC)$(RM) $@+ $@ && \
	$(ASCIIDOC) -b docbook -d manpage -f asciidoc.conf \
		$(ASCIIDOC_EXTRA) -aetl_version=$(ETOOLS_VERSION) -o $@+ $< && \
	mv $@+ $@

$(patsubst %,%.html,$(ARTICLES)) : %.html : %.txt
	$(QUIET_ASCIIDOC)$(ASCIIDOC) $(ASCIIDOC_EXTRA) -b xhtml11 $*.txt

install: install-man

install-man: man
	$(INSTALL) -d -m 755 $(DESTDIR)$(man1dir)
	$(INSTALL) -d -m 755 $(DESTDIR)$(man5dir)
	$(INSTALL) -m 644 $(DOC_MAN1) $(DESTDIR)$(man1dir)
	$(INSTALL) -m 644 $(DOC_MAN5) $(DESTDIR)$(man5dir)

clean:
	$(RM) *.xml *.xml+ *.html *.html+ *.1 *.5 *.7
	$(RM) *.texi *.texi+ *.texi++ git.info gitman.info
	$(RM) howto-index.txt howto/*.html doc.dep
	$(RM) technical/api-*.html technical/api-index.txt
	$(RM) $(cmds_txt) *.made
