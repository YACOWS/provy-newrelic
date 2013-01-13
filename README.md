# provy-newrelic

Automation newrelic on Provy

# Provy conf

    #!/usr/bin/python
	# -*- coding: utf-8 -*-

	from provy.core import Role
	from newrelic import Newrelic

	class FrontEnd(Role):
		def provision(self):
			pass

	class BackEnd(Role):
		def provision(self):
			pass

	servers = {
		'test': {
			'frontend': {
				'address': '33.33.33.33',
				'user': 'vagrant',
				'roles': [
					FrontEnd, Newrelic
				],
				'options': {'newrelic_key': 'xxxxxxxxxxxxxxxxxxxxxxxxxx'}
			},
			'backend': {
				'address': '33.33.33.34',
				'user': 'vagrant',
				'roles': [
					BackEnd, Newrelic
				],
				'options': {'newrelic_key': 'xxxxxxxxxxxxxxxxxxxxxxxxxx'}
			}
		}
	}