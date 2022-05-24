#!/bin/bash
green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'

for i in $(seq 1 $1); do
    password=$(date | base64)
    mail=$(curl -s "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1" | sed 's/"//g' | sed 's/[][]//g')

    curl -s -o /dev/null -H 'Content-Type: application/json' https://publicapi.solotodo.com/rest-auth/registration/ -d "$(
        cat <<EOF
    {
            "email": "$mail",
            "password1": "$password",
            "password2": "$password"
    }
EOF
    )"
    echo "VERIFICATION MAIL SENT: "$mail

    login=${mail%@*}
    domain=${mail#*@}
    sleep 2

    id=$(curl -s "https://www.1secmail.com/api/v1/?action=getMessages&login=$login&domain=$domain" | jq '.[0].id')
    sleep 1

    confirmation_url=$(curl -s "https://www.1secmail.com/api/v1/?action=readMessage&login=$login&domain=$domain&id=$id" | jq '.body' | awk '{gsub(/\\n/,"\n")}1' | htmlq --attribute href a | sed 's/"//g' | sed 's/\\//g')
    confirmation_com=$(curl -s $confirmation_url | htmlq --attribute href a)
    curl $confirmation_com
    confirmation_cl=$(curl -s $confirmation_url | htmlq --attribute href a | sed 's/com/cl/g' | sed 's/:/%3A/2g')
    curl $confirmation_cl
    echo -e "${green}ACCOUNT CREATED.${nocolor} ${yellow}PASSWORD: " $password

done
