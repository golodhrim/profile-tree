% ELONE(1) Etools User Manual
% Jonas Bernoulli
% November 2010

# NAME

elone - list files not owned by any package

# SYNOPSIS

elone [*OPTIONS*] [*PATH*]...

# DESCRIPTION

Elone lists files not owned by any package (installed using portage or a
compatible package manager).  Since there likely exist many files that are
not owned by any package */etc/eclone.conf* contains patterns for files
not to be listed by elone.

Think of */etc/elone.conf* as a list of files known not to belong to any
package, it starts out with a list of such files that exist on most gentoo
installations.  Use `--no-exclude` in order not to read this file.  If you
want to read exclude patterns from a different file use `--exclude`.

Unless `PATH` or `--protected` is provided list all files not explicitly
excluded.  By providing `PATH` (optionally multiple times) the search is
limited to the given directories.  Option `--protected` limits the search
to config protected files.

# OPTIONS

\--version
:   Show version information and exit.

-h, \--help
:   Show help message and exit.

-e *FILE*, \--exclude *FILE*
:   Load exclude rules from FILE instead of the default /etc/elone.conf.

-n, \--no-exclude
:   Ignore exclude rules.

-l, \--no-links
:   Exclude symlinks.

-p, \--protected
:   Only include config protected files.

*PATH*...
: Only list files under these directories.

# SEE ALSO

`echanged`(1).