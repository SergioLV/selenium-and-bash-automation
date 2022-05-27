#!/bin/bash

green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'

input="credentials.csv"
ACCOUNT_COUNTER=1
while IFS=, read -r mail password; do
    new_password=$(tr </dev/urandom -dc _A-Z-a-z-0-9 | head -c${30:-32})
    curl -s -o /dev/null -H 'Content-Type: application/json' -H "Authorization: Evolok evolok.api.service=registration_md evolok.api.sessionId=" "https://ggo.evolok.net/ic/api/userProfile/resetAttributeWorkflow/default?realm=default_realm&email_address=$mail" -d "$(
        cat <<EOF
    {

    }
EOF
    )"
    echo "PASSWORD RECOVERY MAIL SENT: "$mail
    login=${mail%@*}
    domain=${mail#*@}
    sleep 2

    id=$(curl -s "https://www.1secmail.com/api/v1/?action=getMessages&login=$login&domain=$domain" | jq '.[0].id')
    sleep 1

    hrefs_of_the_response=$(curl -s "https://www.1secmail.com/api/v1/?action=readMessage&login=$login&domain=$domain&id=$id" | jq '.body' | htmlq --attribute href a)
    echo $hrefs_of_the_response | tr " " "\n" >>aux
    confirmation_url=$(sed -n '2p' aux)
    rm aux
    echo $confirmation_url >>aux
    password_recovery_token=$(grep -o '".*"' aux | sed 's/"//g' | sed -E 's/.*?resetAttributeKey=([^&]+).*/\1/')
    password_recovery_url="https://ggo.evolok.net/ic/api/resetAttributeWorkflow/"
    password_recovery_endpoint="$password_recovery_url$password_recovery_token"

    rm aux
    echo $password_recovery_endpoint

    curl -s -o /dev/null -H 'Content-Type: application/json' -H "Authorization: Evolok Evolok evolok.api.service=registration_md evolok.api.sessionId=" -X PUT "$password_recovery_endpoint" -d "$(
        cat <<EOF
    {
        "attributes": [
            {
            "name": "password",
            "value": "$new_password"
            }
            ]
    }
EOF
    )"
    echo -e "${green}($ACCOUNT_COUNTER) $mail PASSWORD CHANGED SUCCESSFULLY.${nocolor} ${yellow}NEW PASSWORD: "$new_password${nocolor}
    echo $mail,$new_password >>new_credentials.csv
    ACCOUNT_COUNTER=$((ACCOUNT_COUNTER + 1))
done <$input
