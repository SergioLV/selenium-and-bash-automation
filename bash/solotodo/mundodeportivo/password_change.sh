#!/bin/bash

green='\033[0;32m'
nocolor='\033[0m'
yellow='\033[0;33m'
read_dom() {
    local IFS=\>
    read -d \< ENTITY CONTENT
}

input="credentials.csv"
ACCOUNT_COUNTER=1
while IFS=, read -r mail password; do
    new_password=$(tr </dev/urandom -dc _A-Z-a-z-0-9 | head -c${30:-32})
    session_parameters=$(
        curl -s -o sessions.xml -H 'Content-Type: application/json' -H "Authorization: Evolok evolok.api.service=my_account evolok.api.sessionId=" https://ggo.evolok.net/ic/api/session/registration -d "$(
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
    )

    COUNTER=0
    while read_dom; do
        if [[ $ENTITY = "sessionId" ]]; then
            if [ $COUNTER = 4 ]; then
                secure_id=$CONTENT
            fi
        fi
        if [[ $ENTITY = "guid" ]]; then
            session_id=$CONTENT
        fi
        COUNTER=$((COUNTER + 1))
    done <sessions.xml

    rm sessions.xml
    url_edit_password="https://ggo.evolok.net/ic/api/userProfile/"
    action="/edit_password"
    url_query="$url_edit_password$session_id$action"

    authorization_url="evolok.api.service=edit_password evolok.api.sessionId=$secure_id"
    curl -s -o /dev/null -H "Authorization: Evolok $authorization_url" -H "Content-Type: application/json" -X PUT "$url_query" -d "$(
        cat <<EOF
    {
            "attributes":[{
            "name":"password",
            "value":"$new_password"
            }]
    }
EOF
    )"

    echo -e "${green}($ACCOUNT_COUNTER) $mail PASSWORD CHANGE SUCCESSFUL.${nocolor} ${yellow}NEW PASSWORD: "${new_password}${nocolor}
    echo $mail,$new_password >>password_change_credentials.csv
    ACCOUNT_COUNTER=$((ACCOUNT_COUNTER + 1))
done <$input
