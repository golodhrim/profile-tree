Etools -- miscellaneous portage utilities
=========================================

Etools consists of some small portage utilities.  Currently these tools
are most suitable to get a grand overview of changes you have made to
your system, which might be specially handy when you want to copy over
your configurations to another machine or when you make a fresh install.

Please not that I have quickly written these scripts to scratch an itch.
They seam to work fine and I have taken the extra effort to document them,
but use at your own risk.

[Elone](https://github.com/tarsius/etools/blob/master/man/elone.1.md) list files not owned by any package
----------

Elone lists files not owned by any package (installed using portage or a
compatible package manager).  Since there likely exist many files that are
not owned by any package */etc/eclone.conf* contains patterns for files
known to be listed by elone.

[Echanged](https://github.com/tarsius/etools/blob/master/man/echanged.1.md) list packages which own modified files
----------

Echanged lists packages (installed using portage or a compatible package
manager) which own modified files.  This is similar to `equery check <pkgspec>`
but more suitable to get a grand overview of the changes to all packages on
your system.

[Profile-stack](https://github.com/tarsius/etools/blob/master/man/profile-stack.1.md) show stack of parent profiles of a portage profile
----------

Profile-stack shows a stack of the parent profiles of the specified
portage profile and optionally the contained files.

Redigest -- update unmerged manifests in the portage tree
----------

Redigest updates unmerged manifests and try to continue rebasing (which
doesn't have an effect when merging and fails if there are other conflicts).
An exit status of 1 means you are not done yet with this commit.

----------

Ebuilds are available [here](http://github.com/tarsius/tarsius-tree/tree/org.tarsiidae/app-portage/etools/).

----------

Thanks and Best Regards,
 
Jonas Bernoulli <jonas@bernoul.li>
