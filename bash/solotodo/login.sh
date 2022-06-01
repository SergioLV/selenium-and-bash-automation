#!/bin/bash
#This script takes the credentials.csv file created with the create_accounts scrips.
green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'
red='\033[0;31m'

input="credentials.csv"
ACCOUNT_COUNTER=1
while IFS=, read -r mail password; do
    response=$(curl -s -H 'Content-Type: application/json' https://publicapi.solotodo.com/rest-auth/login/ -d "$(
        cat <<EOF
    {
            "email": "$mail",
            "password": "$password"
    }
EOF
    )" | jq '.key')
    if [[ $response == null ]]; then
        echo -e "${red} BAD CREDENTIALS FOR THE ACCOUNT: $mail, TRY ANOTHER PASSWORD ${nocolor}"
    else
        echo -e "${green}($ACCOUNT_COUNTER) ACCOUNT LOGIN SUCCESSFUL.${nocolor} ${yellow}MAIL: "${mail}${nocolor}
    fi
    ACCOUNT_COUNTER=$((ACCOUNT_COUNTER + 1))

done <$input
