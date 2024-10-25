### Notes CLI tool
This is a note taking CLI tool.

### Examples
- List notes - `notes -l`
- Add a new note - `notes -a "my new note"`
- Clear all notes - `notes -c`
- Delete a note - `notes -d -id <note_id as integer>`
- Modify a note - `notes -m "my modified note" -id <note_id as integer>`

### Project setup
Clone the project and navigate to the root directory and then run the following commands:
- `pip install ./src/`
- `ansible-playbook -i mysql-ansible/inventory.yml mysql-ansible/mysql.yml`

Confirm the installation was successful by running `notes -h`.

### Debugging
If you see a failure like the one below when running the ansible playbook, try running `sudo ls` and then retrying the ansible command.
```
PLAY [Install and configure MySQL] ****************************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************************
fatal: [localhost]: FAILED! => {"ansible_facts": {}, "changed": false, "failed_modules": {"ansible.legacy.setup": {"failed": true, "module_stderr": "sudo: a password is required\n", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error", "rc": 1}}, "msg": "The following modules failed to execute: ansible.legacy.setup\n"}

PLAY RECAP ****************************************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0 
```
