% PROFILE-STACK(1) Etools User Manual
% Jonas Bernoulli <jonas@bernoul.li>
% September 24, 2009

# NAME

profile-stack - show stack of parent profiles of a portage profile

# SYNOPSIS

profile-stack [-h] [-v] [*profile*]

# DESCRIPTION

profile-stack shows a stack of the parent profiles of the specified
portage profile.  PROFILE has to relative to */usr/portage/profiles* and
defaults to the active profile if omitted.

The stack starts with the requested profile and ends with the profile
which is loaded first.  Profiles in parentheses do not contain any
configuration themselfs, they only contain a *parent* file.  They may
contain *eapi* or *ChangeLog*.  Profiles in angle brackets will be loaded
again later.

When `-v` is specified files in the profiles are also listed; excluding
*parent*, *eapi* and *ChangeLog*.

# OPTIONS

--version
:   Show version information and exit.

-h, \--help
:   Show help message and exit.

-v
:   Show contained files along with profiles.

<*profile*>...
:   The profile for which to show the parents (defaults to active
    profile).

# SEE ALSO

`profile.eselect`(5).
