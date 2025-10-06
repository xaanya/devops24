# Examination 7 - MariaDB installation

To make a dynamic web site, many use an SQL server to store the data for the web site.

[MariaDB](https://mariadb.org/) is an open-source relational SQL database that is good
to use for our purposes.

We can use a similar strategy as with the _nginx_ web server to install this
software onto the correct host(s):

    ---
    - hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB-server is installed.
          ansible.builtin.package:
            name: mariadb-server
            state: present

The software should, just like the web server, be started at boot, and be running
when the playbook is finished.

# QUESTION A

Make similar changes to this playbook that we did for the _nginx_ server, so that
the `mariadb` service starts automatically at boot, and is started when the playbook
is run.

# QUESTION B

When you have run the playbook above successfully, how do you verify that the `mariadb`
service is started and is running?

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?
