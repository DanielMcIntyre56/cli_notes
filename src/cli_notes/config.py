import os

# TODO - make divider size based on max note length in DB

# MYSQL variables
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_HOST = "localhost"
NOTES_DB_NAME = "notesdb"

# Formatting and spacing
LARGE_SPACE = "       "
SMALL_SPACE = "   "
HASH_SPACE = ""
DIVIDER = ""

for _ in range(64): HASH_SPACE += " "
for _ in range(125): DIVIDER += "-"
