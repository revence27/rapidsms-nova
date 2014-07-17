#!/usr/bin/env python
import os
import sys

#	sys.path.append(os.getcwd())

#	activate_this = '/usr/local/venv/rapidsmsrw1000/bin/activate_this.py'
#	execfile(activate_this, dict(__file__=activate_this))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rapidsmsrw1000.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
