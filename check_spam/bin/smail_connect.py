#!/usr/bin/env python

import imaplib
import ConfigParser
import os
from pprint import pprint

conf_path = os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/conf'
conf_conn = conf_path + '/imap.pyconf'
conf_user = conf_path + '/pwd.pyconf'

def open_connection(verbose=False):
    # Lettura del file di configurazione
    conf_path = os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + '/conf'
    conf_conn = conf_path + '/imap.pyconf'
    conf_user = conf_path + '/pwd.pyconf'

    config = ConfigParser.ConfigParser()
    pwdconfig = ConfigParser.ConfigParser()
    config.read(conf_conn)
    pwdconfig.read(conf_user)

    # Connessione al server
    hostname = config.get('server', 'hostname')

    if verbose: print 'Connessione a', hostname
    connection = imaplib.IMAP4_SSL(hostname)

    # Connessione al proprio account
    username = pwdconfig.get('account', 'username')
    password = pwdconfig.get('account', 'password')
    if verbose: print 'Collegamento come', username
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        print c
    finally:
        c.logout()

