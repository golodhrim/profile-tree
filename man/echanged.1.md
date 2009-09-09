% ECHANGED(1) Etools User Manual
% Jonas Bernoulli <jonas@bernoul.li>
% September 9, 2009

# NAME

echanged -- list packages which own modified files

# SYNOPSIS

echanged [*options*] [*path*]...

# DESCRIPTION

Echanged lists packages (installed using portage or a compatible package
manager) which own modified files.  This is similar to `equery check <pkgspec>`
but more suitable to get a grand overview of the changes to all packages on
your system.

Unless `PATH` or `--protected` is provided all installed packages are
checked.  By providing `PATH` (optionally multiple times) the search is
limited to the given directories.  Option `--protected` limits the search
to packages which own config protected files.

Unless the `--quiet` is provided the modified files are listed along with
the package.  Option `--all` on the other hand causes causes all modified
files of a package to be listed not only those under the provided PATH or
which are config protected.

# OPTIONS

--version
:   Show version information and exit.

-h, \--help
:   Show help message and exit.

-q, \--quiet
:   Do not list files along with packages.

-a, \--all
:   List all modified files even if not in PATH or not config protected.

-p, \--protected
:   Only list packages which own config protected files.

<*path*>...
:   Only list files under these directories.

# SEE ALSO

`elone`(1),
`equery`(1).
