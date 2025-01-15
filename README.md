### Notes CLI tool
This is a note taking CLI tool.


### Installation
- `wget https://github.com/DanielMcIntyre56/cli_notes/releases/download/v1.0/notes_cli_1.0-1.deb`
- `sudo dpkg -i notes_cli_1.0-1.deb` 
- `cd /usr/share/ansible/notes-cli-ansible`
- `ansible-playbook -i inventory.yml mysql.yml`

If you want to use the latest development version of this project (unstable - [see releases](#releases)), replace the first two commands with the below commands and then continue the installation steps as normal:
- `wget https://github.com/DanielMcIntyre56/cli_notes/releases/download/development/development.deb`
- `sudo dpkg -i development.deb`

Confirm the installation was successful by running `notes -h`.


### Examples
- List notes - `notes -l`
- Add a new note - `notes -a "my new note"`
- Clear all notes - `notes -c`
- Delete a note - `notes -d -id <note_id as integer>`
- Modify a note - `notes -m "my modified note" -id <note_id as integer>`


### Technology
- `MySQL` is the database used for managing the notes storage and access.
- `Alembic` is used to handle database configuration and modification.
- `Python3` is used for the script entry points and database interaction.
- `SQLAlchemy` is used to interact with the database within the Python package.
- `Ansible` is used to automatically apply configuration required for the project, for example installing MySQL, running Alembic migrations, granting correct permissions on MySQL databases.
- `GitHub Actions` is used to automate building and deploying the latest development version of the project.


### Releases
- The latest stable release of this project will have the `latest` tag. This is the release which should be used generally.
- There is also a development release which contains a release build with the latest version committed to the master branch. This release is for testing and will not be stable and may contain bugs. It will also contain the very latest changes to the project.


### Debugging
If you see a failure like the one below when running the ansible playbook, try running `sudo ls` and then retrying the ansible command.
```
PLAY [Install and configure MySQL] ****************************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************************
fatal: [localhost]: FAILED! => {"ansible_facts": {}, "changed": false, "failed_modules": {"ansible.legacy.setup": {"failed": true, "module_stderr": "sudo: a password is required\n", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error", "rc": 1}}, "msg": "The following modules failed to execute: ansible.legacy.setup\n"}

PLAY RECAP ****************************************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0 
```
