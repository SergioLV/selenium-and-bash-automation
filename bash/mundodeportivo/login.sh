#!/bin/bash

green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'

input="credentials.csv"
ACCOUNT_COUNTER=1
while IFS=, read -r mail password; do
    curl -s -o /dev/null -H 'Content-Type: application/json' -H "Authorization: Evolok evolok.api.service=my_account evolok.api.sessionId=" https://ggo.evolok.net/ic/api/session/registration -d "$(
        cat <<EOF
    {
        "realmName":"default_realm",
        "authenticationSchemeName":"default",
        "identifiers":[{"name":"email_address","value":"$mail"}],
        "validators":[{"name":"password","value":"$password"}],
        "channel":"WEB"
    }                                                                                                                        
EOF
    )"
    echo -e "${green}($ACCOUNT_COUNTER) ACCOUNT LOGIN SUCCESSFUL.${nocolor} ${yellow}MAIL: "${mail}${nocolor}
    ACCOUNT_COUNTER=$((ACCOUNT_COUNTER + 1))
done <$input
