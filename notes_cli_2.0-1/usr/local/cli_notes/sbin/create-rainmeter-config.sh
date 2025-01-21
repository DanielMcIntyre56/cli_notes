#!/bin/bash

# Script to set up the Rainmeter integration.

WSL_TXT_FILE_PATH=/etc/config/cli_notes/notes.txt
RAINMETER_INI_FILE_PATH=/etc/config/cli_notes/NotesDisplay.ini
EXPECTED_RAINMETER_USER_PATH=./Documents/Rainmeter


function help () {
    echo "TODO: add help information"
    echo "TODO -> add more error code checks when calling functions"
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

    if [ -d "$EXPECTED_RAINMETER_USER_PATH" ]; then
        cd "$EXPECTED_RAINMETER_USER_PATH"
        return
    fi

    rainmeter_path=$(find ./ -type d -wholename *Documents/Rainmeter$*)

    if [ -z "$rainmeter_path" ]; then
        echo "ERROR: Could not find the Rainmeter path, ensure Rainmeter is installed."
        exit 1
    fi

    cd "$rainmeter_path"
}


# Set up Rainmeter .ini config file
function set_up_rainmeter_config () {
    cd Skins
    mkdir -p NotesSkin
    cp "$RAINMETER_INI_FILE_PATH" ./NotesSkin/NotesDisplay.ini
    chmod 755 NotesSkin/NotesDisplay.ini
    chown root:root NotesSkin/NotesDisplay.ini

    WIN_DIR="$windows_txt_dir"
    WIN_DIR="${WIN_DIR//\/mnt\/c/C:}"
    WIN_DIR="${WIN_DIR//\//\\\\}"

    # Replace placeholder variables with actual paths
    CONTENT="NotesPath=$WIN_DIR/notes.txt"
    sed -i "13 c\\$CONTENT" ./NotesSkin/NotesDisplay.ini

    CONTENT="NotesPath=$WIN_DIR"
    sed -i "14 c\\$CONTENT" ./NotesSkin/NotesDisplay.ini
}


# Set up .txt files
function set_up_txt_file () {
    # cd to Documents dir
    cd ..

    # Create and set permissions for .txt file in Windows location
    windows_txt_dir=$(pwd)
    touch "$windows_txt_dir"/notes.txt
    chmod 664 "$windows_txt_dir"/notes.txt
    chown root:root "$windows_txt_dir"/notes.txt

    # Symlink the files
    if ! [ -f "$WSL_TXT_FILE_PATH" ]; then
        ln -s "$windows_txt_dir"/notes.txt "$WSL_TXT_FILE_PATH"
    fi

    # cd back to Rainmeter dir
    cd -
}


# Username checks
check_user_name
check_user_exists
echo "INFO: Continuing with username '$USERNAME'."


# Rainmeter setup
cd_to_rainmeter_path
set_up_txt_file
set_up_rainmeter_config
echo "INFO: Successfully set up Rainmeter integration."
