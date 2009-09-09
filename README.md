Etools -- misc portage utilities
================================

Etools consists of some small portage utilities.  Currently these tools
are most suitable to get a grand overview of changes you have made to
your system, which might be specially handy when you want to copy over
your configurations to another machine or when you make a fresh install.

[Elone](https://github.com/tarsius/etools/blob/master/man/elone.1.md) -- list files not owned by any package
--------------------------------------------

Elone lists files not owned by any package (installed using portage or a
compatible package manager).  Since there likely exist many files that are
not owned by any package */etc/eclone.conf* contains patterns for files
not to be listed by elone.

[Echanged](https://github.com/tarsius/etools/blob/master/man/echanged.1.md) -- list packages which own modified files
--------------------------------------------------

Echanged lists packages (installed using portage or a compatible package
manager) which own modified files.  This is similar to `equery check <pkgspec>`
but more suitable to get a grand overview of the changes to all packages on
your system.

---

Ebuilds are available [here](https://github.com/tarsius/tarsius-tree/blob/master/app-portage/etools/).

---

Thanks and Best Regards,
 
Jonas Bernoulli <jonas@bernoul.li>
