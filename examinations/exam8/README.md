# Examination 8 - MariaDB configuration

MariaDB and MySQL come from the same origin and work the same way, which makes it possible
to use Ansible collections that handle `mysql` to work with `mariadb`.

# QUESTION A

Use the `community.mysql` module in the playbook we created in Examination 7, so that it
also creates a database instance called `webappdb` and a database user called `webappuser`.

Make the `webappuser` have the password "secretpassword" to access the database.

You can create a separate playbook too, if you feel it makes it easier.

# Documentation and Examples
https://docs.ansible.com/ansible/latest/collections/community/mysql/index.html
