# Etools -- miscellaneous portage utilities

Etools consists of some small miscellaneous portage utilities.  Currently
these tools are most suitable to get a grand overview of changes you have
made to your system, which might be specially handy when you want to copy
over your configurations to another machine or when you make a fresh
install.

Please note that I have quickly written these scripts to scratch an itch.
They seam to work fine and I have taken the extra effort to document them,
but use them at your own risk.

Ebuilds are available in my
[overlay](http://github.com/tarsius/overlay-tarsius/tree/master/app-portage/etools/)
and development happens on [github](http://github.com/tarsius/etools/).

## Profile-tree

[profile-tree(1)](profile-tree.1.html) lists the paths to portage profiles
and optionally their contents in a tree-like format.

## Echanged

[echanged(1)](echanged.1.html) lists packages which own modified files.
This is similar to `equery check <pkgspec>` but more suitable to get a
grand overview of the changes to all packages on your system.

## Elone

[elone(1)](elone.1.html) lists files not owned by any package.  Since
there likely exist many files that are not owned by any package
*/etc/eclone.conf* contains patterns for files known to be listed by elone.

## Whose

[whose(1)](whose.1.html) writes the package COMMAND belongs to to standard
output with the help of which(1) and equery(1).

----

Thanks and Best Regards,
 
Jonas Bernoulli <jonas@bernoul.li>
