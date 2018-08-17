#!/usr/bin/env python
import datetime
import ConfigParser
import os
import imaplib
import smail_connect
from datetime import date
from datetime import timedelta

conf_path = os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/conf'
conf_file = conf_path + '/imap.pyconf'
config = ConfigParser.ConfigParser()
config.read(conf_file)

directory = config.get('mail', 'directory')

date_now = str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))[0:16]
date_ten = str((datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime("%d %b %Y %H:%M"))[0:16]
date_twenty = str((datetime.datetime.now() - datetime.timedelta(minutes=20)).strftime("%d %b %Y %H:%M"))[0:16]

c = smail_connect.open_connection()
string_now = "'(FROM " + '"antispam@domain.it" SUBJECT "[Domain SPAM]" HEADER "Date:" "' + date_now + '")' + "'" 
string_ten = "'(FROM " + '"antispam@domain.it" SUBJECT "[Domain SPAM]" HEADER "Date:" "' + date_ten + '")' + "'" 
string_twenty = "'(FROM " + '"antispam@domain.it" SUBJECT "[Domain SPAM]" HEADER "Date:" "' + date_twenty + '")' + "'" 

for string_search in string_now, string_ten, string_twenty:
    msg_ids_search = 'typ, msg_ids = c.search(None, ' + string_search + ')'
    c.select(directory, readonly=True)
    exec(msg_ids_search)
    ids_string = ''.join(msg_ids)
    ids_list = ids_string.split()
    for i in range(len(ids_list)):
        print ids_list[i]
try:
    c.close()
except:
     pass

c.logout()
