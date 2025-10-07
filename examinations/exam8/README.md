# Examination 8 - MariaDB configuration

MariaDB and MySQL come from the same origin and work the same way, which makes it possible
to use Ansible collections that handle `mysql` to work with `mariadb`.

To be able to manage MariaDB/MySQL through the `community.mysql` collection, you also
need to make sure the requirements for the collections are installed on the database VM.

See https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_db_module.html#ansible-collections-community-mysql-mysql-db-module-requirements

HINT: In AlmaLinux, the correct package to install on the VM host is called `python3-PyMySQL`.

# QUESTION A

Use the `community.mysql` module in the playbook we created in Examination 7, so that it
also creates a database instance called `webappdb` and a database user called `webappuser`.

Make the `webappuser` have the password "secretpassword" to access the database.

You can create a separate playbook too, if you feel it makes it easier.

HINT: The `community.mysql` collection modules has many different ways to authenticate
users to the MariaDB/MySQL instance. Since we've just installed `mariadb` without setting
any root password, or securing the server in other ways, we can use the UNIX socket
to authenticate as root:

* The socket is located in `/var/lib/mysql/mysql.sock`
* Since we're authenticating through a socket, we should ignore the requirement for a `~/.my.cnf` file.

# Documentation and Examples
https://docs.ansible.com/ansible/latest/collections/community/mysql/index.html
