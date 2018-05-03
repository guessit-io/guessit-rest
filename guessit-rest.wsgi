#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Example apache configuration
# <VirtualHost *>
#   ServerName guessit-rest.local
#
#   WSGIDaemonProcess guessitrest user=someuser python-home=/path/to/virtualenv
#   WSGIScriptAlias / /path/to/guessit-rest/guessit-rest.wsgi
#
#   <Directory /path/to/guessit-rest/>
#     WSGIProcessGroup guessitrest
#     WSGIApplicationGroup %{GLOBAL}
#     <IfVersion >= 2.4>
#       Require all granted
#     </IfVersion>
#     <IfVersion < 2.4>
#       Order allow,deny
#       Allow from all
#     </IfVersion>
#   </Directory>
# </VirtualHost>

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from guessitrest.app import app as application