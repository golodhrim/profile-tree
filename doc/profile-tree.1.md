% PROFILE-TREE(1) Etools User Manual
% Jonas Bernoulli
% November 2010

# NAME

profile-tree - list portage profiles in a tree-like format

# SYNOPSIS

profile-tree [-c[=*REGEXP*]] [*PROFILE*]

# DESCRIPTION

profile-tree lists the paths to portage profiles and optionally their
contents in a tree-like format.  PROFILE defaults to the active profile
if omitted.  Otherwise it has to be an absolute path or a path relative
to the current directory or relative to `PORTDIR/profiles`.

The list is in reverse chronological order - it starts with PROFILE resp.
the current profile and ends with the profile which is loaded first.

Profiles in parentheses do not contain any files that hold any meaning to
`portage(5)` except for `parent` and `deprecated`.  These files are listed
in `/etc/make.profile/` in `portage(5)`.

Profiles that contain the `deprecated` file and profiles loaded more than
once are shown with a prefix indicating the problem.

When `-c` is specified the contents of the profiles is also listed; again
excluding `parent` and `deprecated` and all unknown files.  If `REGEXP`
is provided only matching files are shown. All profiles are shown without
parentheses in this case.

# OPTIONS

\--version
:   Show version information and exit.

-h, \--help
:   Show help message and exit.

-c[=*REGEXP*]
:   Also list contents of profiles.  If *REGEXP* is set only show files
    whose filename relative to the current profile match *REGEXP*.

*PROFILE*...
:   The profile to be shown (defaults to the active profile).  Can be
    an absolute path or a path relative to the current directory or
    relative to PORTDIR/profiles.

# SEE ALSO

`profile.eselect(5)`.