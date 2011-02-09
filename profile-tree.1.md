% PROFILE-TREE(1)
% Jonas Bernoulli
% February 2011

# NAME

profile-tree - list portage profiles and portage config files

# SYNOPSIS

profile-tree [-c[=*REGEXP*]] [*PROFILE*]

# DESCRIPTION

profile-tree lists the effective portage profiles and optionally the
relevant files inside these profiles as a tree.  It also lists some
other files used to configure portage.

By default profile-tree lists the profiles /etc/portage inherits from.
If PROFILE is specified that is used instead.  Profiles that begin with
`:` in the output are relative to /usr/portage/profiles and profiles that
are shown as relative paths are relative to /etc/portage.  All other
profiles are shown as absolute paths.

Profiles shown in parentheses do not contain any files (except for maybe
`parent` and/or `deprecated`) that hold any meaning to `portage(5)`.
Profiles that contain the `deprecated` file and profiles loaded more than
once are shown with a suffix indicating the problem.

When `-c` is specified the relevant files inside profiles as well as some
portage config files that are located elsewhere are also shown.  If
`REGEXP` is specified matching files are shown instead.  `REGEXP` should
not begin with `^` and/or end with `$`.

Generally all files listed in `portage(5)` are shown when using the `-c`
option without specifying a `REGEXP` explicitly, but a few are being
ignored while some others not documented there are shown instead.  You
can customize what files are shown by editing /etc/profile-tree.conf.

PLEASE NOTE: profile-tree only works with Funtoo's version of portage.
At the time of writing it even assumes you are using the unreleased beta
version.  Since portage is currently undergoing heavy refactoring the
output of profile-tree might stop being in sync with how portage handles
it's profiles and it's config files.  These are exiting times!

# OPTIONS

\--version
:   Show version information and exit.

-h, \--help
:   Show help message and exit.

-c[=*REGEXP*]
:   Show config files within and outside of profiles.  If REGEXP is set
    show matching file instead.

*PROFILE*...
:   The profile to be shown along with the profiles it inherits from.
    instead of the default profile which is /etc/portage.

# SEE ALSO

`portage(5)`.
