#!/usr/bin/env python
# -*- coding: utf-8 -*-

from provy.core import Role
from provy.more.debian import AptitudeRole



class Newrelic(Role):
    def provision(self):
        with self.using(AptitudeRole) as role:

            role.ensure_aptitude_source('deb http://apt.newrelic.com/debian/ newrelic non-free')
            role.execute('apt-key adv --keyserver hkp://subkeys.pgp.net --recv-keys 548C16BF', sudo=True)
            role.force_update()

            role.ensure_package_installed('newrelic-sysmond')

            role.execute('nrsysmond-config --set license_key=%s' % self.context['newrelic_key'], sudo=True)
            self.execute('service newrelic-sysmond restart', sudo=True)

