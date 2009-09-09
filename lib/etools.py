#!/usr/bin/python
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# Author:  Jonas Bernoulli <jonas@bernoul.li>
# Created: 20090909
# Updated: 20090909
# Version: 001 (this file)
#
# Commentary:
#   Functions used by multiple commands in the etools package.

def get_owner(cfile, packages, get_all=False):
	owners = []
	for pkg in packages:
		if cfile in pkg.get_contents():
			owners.append(pkg.cpv)
			if not get_all:
				break
	return owners
