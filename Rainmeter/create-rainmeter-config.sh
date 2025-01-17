#!/bin/bash

# Script to set up the Rainmeter config file.


function help () {
    echo "TODO: add help information"
}


while getopts "hu:" opt; do
    case "$opt" in
    h)
        help
        exit 0
        ;;
    u)
        USERNAME=${OPTARG}
        ;;
    ?)
        echo "Error: ${OPTARG} is an unsupported option."
        exit 1
        ;;
   esac
done


# Check if username was provided
# if not set it to the current user
function check_user_name () {
    if [ -z "$USERNAME" ]; then
        echo "WARNING: No username provided, checking who I am."
        USERNAME=$(whoami)
    fi
}

# Checks a user exists under /mnt/c/Users
# Exits the script with RC 1 if not 
function check_user_exists () {
    ls /mnt/c/Users/$USERNAME >/dev/null 2>&1

    if [ $? -gt 0 ]; then
        echo "Error: User $USERNAME does not exist in Windows."
        exit 1
    fi
}


# Changes directory to the Rainmeter path
# Exits the script with RC 1 if directory cannot be found
function cd_to_rainmeter_path () {
    cd /mnt/c/Users/"$USERNAME"
    rainmeter_path=$(find ./ -type d -wholename *Documents/Rainmeter$*)

    if [ -z "$rainmeter_path" ]; then
        echo "ERROR: Could not find the Rainmeter path, ensure Rainmeter is installed."
        exit 1
    fi

    cd "$rainmeter_path"
}


# Create the dir
# Put NotesDisplay.ini in dir
# Other Rainmeter requirements?
function set_up_rainmeter_config () {
    mkdir NotesSkin
}


# Username checks
check_user_name
check_user_exists
echo "INFO: Continuing with username '$USERNAME'."


# Rainmeter ...
cd_to_rainmeter_path
