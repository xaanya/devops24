# Examination 11 - Loops

Imagine that on the web server(s), the IT department wants a number of users accounts set up:

- alovelace
- aturing
- edijkstra
- ghopper

`alovelace` and `ghopper` should be added to the `wheel` group, and `aturing` and `edijkstra` should
both be added to the `tcpdump` group.

Also, the IT department, for some unknown reason, wants to copy a number of '\*.md' files
to the 'deploy' user's home directory on the `db` machine(s).

# QUESTION A

Write a playbook that uses loops to add these users, and adds them to their respective groups.

# QUESTION B

Write a playbook that uses

    with_fileglob: 'files/*.md5'

to copy all `\*.md` files in the `files/` directory to the `deploy` user's directory on the `db` server(s).

# BONUS QUESTION

Use `ansible-vault` to encrypt passwords for each user created.

# Resources and Documentation

* [ansible.builtin.user](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html)
* [ansible.builtin.fileglob](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/fileglob_lookup.html)


