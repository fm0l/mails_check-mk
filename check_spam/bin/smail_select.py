#!/usr/bin/env python

import ConfigParser
import imaplib
import smail_connect
import os

c = smail_connect.open_connection()

conf_path = os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/conf'
conf_conn = conf_path + '/imap.pyconf'

config = ConfigParser.ConfigParser()
config.read(conf_conn)

try:
    directory = config.get('mail', 'directory')
    print directory
    typ, data = c.select(directory)
    print typ, data
    num_msgs = int(data[0])
    print 'Ci sono %d messagggi in %s' % (num_msgs, directory)
finally:
    c.close()
    c.logout()
