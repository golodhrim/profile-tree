# Etools -- miscellaneous portage utilities

Etools consists of some small miscellaneous portage utilities that give
you a grand overview of changes you have made to your system.

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
*/etc/eclone.conf* contains patterns for files known to be otherwise
listed by elone.

## Whose

[whose(1)](whose.1.html) writes the package COMMAND belongs to to standard
output with the help of which(1) and equery(1).

----

Best Regards,
 
Jonas Bernoulli <jonas@bernoul.li>
