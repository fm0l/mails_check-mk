#!/usr/bin/env bash

DIRNAME=$(dirname $0)
SPAMMAIL=$( $DIRNAME/check_spam/bin/smail_search_spam.py | wc -l)

if [ "$SPAMMAIL" -ge 10 ]; then
	echo "CRIT - There are "$SPAMMAIL" outbound spam email! Please check."
	exit 2
elif [ "$SPAMMAIL" -ge 6 ]; then
	echo "WARN - There are "$SPAMMAIL" outbound spam email! Please check."
	exit 1
else
	echo "OK- Spam emails are inside the treshold - "$SPAMMAIL
	exit 0
fi
