#!/bin/bash
#This script takes the credentials.csv file created with the create_accounts scrips.
green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'

input="credentials.csv"
ACCOUNT_COUNTER=1
while IFS=, read -r mail password; do
    curl -s -o /dev/null -H 'Content-Type: application/json' https://publicapi.solotodo.com/rest-auth/login/ -d "$(
        cat <<EOF
    {
            "email": "$mail",
            "password": "$password"
    }
EOF
    )"
    echo -e "${green}($ACCOUNT_COUNTER) ACCOUNT LOGIN SUCCESSFUL.${nocolor} ${yellow}MAIL: "${mail}${nocolor}
    ACCOUNT_COUNTER=$((ACCOUNT_COUNTER + 1))
    
done <$input
