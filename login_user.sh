# uses SXTCLI to login a user and return the access token
. ./.env

export RETURN=$(sxtcli authenticate login --url=$API_URL --userId=$USERID --publicKey=$USER_PUBLIC_KEY --privateKey=$USER_PRIVATE_KEY)
export TOKEN=$(echo $RETURN | awk 'NR==2{ print $2 }')
export REFRESH_TOKEN=$(echo $RETURN | awk 'NR==3{ print $2 }')

# any supplied parameter will trigger an echo of the token
if [ ! ${#1} = 0 ]; then echo "TOKEN="$TOKEN; fi