#!/bin/bash

green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'

ACCOUNT_COUNTER=1
for i in $(seq 1 $1); do
    password=$(tr </dev/urandom -dc _A-Z-a-z-0-9 | head -c${30:-32})
    mail=$(curl -s "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1" | sed 's/"//g' | sed 's/[][]//g')
    curl -s -o /dev/null -H 'Content-Type: application/json' -H "Authorization: Evolok evolok.api.service=my_account evolok.api.sessionId=" https://ggo.evolok.net/ic/api/userProfile -d "$(
        cat <<EOF
    {
    "realm": "default_realm",
    "services": [
        "registration"
    ],
    "attributes": [
        {
            "name": "email_address",
            "value": "$mail"
        },
        {
            "name": "password",
            "value": "$password"
        },
        {
            "name": "brand",
            "value": "MD"
        }
    ],
    "channel": "WEB"
}
EOF
    )"

    echo "VERIFICATION MAIL SENT: "$mail

    login=${mail%@*}
    domain=${mail#*@}
    sleep 2

    id=$(curl -s "https://www.1secmail.com/api/v1/?action=getMessages&login=$login&domain=$domain" | jq '.[0].id')
    sleep 1

    hrefs_of_the_response=$(curl -s "https://www.1secmail.com/api/v1/?action=readMessage&login=$login&domain=$domain&id=$id" | jq '.body' | htmlq --attribute href a)

    # confirmation_com=$(curl -s $confirmation_url | htmlq --attribute href a)
    echo $hrefs_of_the_response | tr " " "\n" >>aux
    confirmation_url=$(sed -n '2p' aux)
    rm aux
    final=$(curl -s $confirmation_url)
    echo -e "${green}($ACCOUNT_COUNTER) ACCOUNT CREATED.${nocolor} ${yellow}PASSWORD:" $password ${nocolor}
    echo $mail,$password >>credentials.csv
    ACCOUNT_COUNTER=$((ACCOUNT_COUNTER + 1))
done
