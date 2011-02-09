% PROFILE-TREE(1) Etools User Manual
% Jonas Bernoulli
% January 2011

# NAME

profile-tree - list portage profiles and optionally config files

# SYNOPSIS

profile-tree [-c[=*REGEXP*]] [*PROFILE*]

# DESCRIPTION

profile-tree lists the paths to portage profiles and optionally their
contents in a tree-like format.  It also lists some other files used to
configure portage.  PROFILE defaults to /etc/portage if omitted.

The list is in reverse chronological order - it starts with PROFILE resp.
/etc/portage and ends with the profile which is loaded first.  Profiles
that begin with `:` in the output are relative to /usr/portage/profiles
and profiles that are shown as relative paths are relative to
/etc/portage/profiles.  All other profiles are shown as absolute paths.

Profiles in parentheses do not contain any files that hold any meaning to
`portage(5)` except for `parent` and `deprecated`.  See `portage(5)` for
more information about these files.

Profiles that contain the `deprecated` file and profiles loaded more than
once are shown with a suffix indicating the problem.

When `-c` is specified the contents of the profiles is also listed; again
excluding `parent` and `deprecated` and all unknown files.  If `REGEXP`
is provided only matching files are shown. All profiles are shown without
parentheses in this case.

PLEASE NOTE: profile-tree only works with Funtoo's version of portage.
At the time of writing it even assumes you are using the unreleased beta
version.  Since portage is currently undergoing heavy refactoring the
output of profile-tree might stop being in sync with how portage handles
it's profiles and it's config files.  These are exiting times!

Once implementation of the new-style profiles is mostly done this hack
might be replaced by an implementation in python that get's it's
information using the portage library (like other portage tools) so that
you can actually be sure that the precented information reflect how
portage itself sees it.

# OPTIONS

\--version
:   Show version information and exit.

-h, \--help
:   Show help message and exit.

-c[=*REGEXP*]
:   Also list contents of profiles.  If *REGEXP* is set only show files
    whose filename relative to the current profile match *REGEXP*.

*PROFILE*...
:   The profile to be shown (defaults to the /etc/portage).

# SEE ALSO

`portage(5)`.
