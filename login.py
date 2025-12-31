#!/bin/bash

USER_DB="users.db"

# Ensure database exists
touch "$USER_DB"

hash_password() {
    echo -n "$1" | sha256sum | awk '{print $1}'
}

register() {
    read -p "Choose a username: " username

    if grep -q "^$username:" "$USER_DB"; then
        echo "User already exists."
        return
    fi

    read -s -p "Choose a password: " password
    echo
    read -s -p "Confirm password: " confirm
    echo

    if [[ "$password" != "$confirm" ]]; then
        echo "Passwords do not match."
        return
    fi

    hashed=$(hash_password "$password")
    echo "$username:$hashed" >> "$USER_DB"
    echo "User registered successfully."
}

login() {
    read -p "Username: " username
    read -s -p "Password: " password
    echo

    stored_hash=$(grep "^$username:" "$USER_DB" | cut -d':' -f2)

    if [[ -z "$stored_hash" ]]; then
        echo "Invalid username or password."
        return
    fi

    input_hash=$(hash_password "$password")

    if [[ "$input_hash" == "$stored_hash" ]]; then
        echo "Login successful. Welcome, $username!"
    else
        echo "Invalid username or password."
    fi
}

echo "1) Register"
echo "2) Login"
read -p "Select an option: " choice

case $choice in
    1) register ;;
    2) login ;;
    *) echo "Invalid option." ;;
esac
