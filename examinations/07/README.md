# Examination 7 - MariaDB installation

To make a dynamic web site, many use an SQL server to store the data for the web site.

[MariaDB](https://mariadb.org/) is an open-source relational SQL database that is good
to use for our purposes.

We can use a similar strategy as with the _nginx_ web server to install this
software onto the correct host(s). Create the playbook `07-mariadb.yml` with this content:

    ---
    - hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB-server is installed.
          ansible.builtin.package:
            name: mariadb-server
            state: present

# QUESTION A

Make similar changes to this playbook that we did for the _nginx_ server, so that
the `mariadb` service starts automatically at boot, and is started when the playbook
is run.

# QUESTION B

When you have run the playbook above successfully, how can you verify that the `mariadb`
service is started and is running?

SVAR: Jag gjorde såhär: sudo systemctl status mariadb

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?

SVAR: För att kontrollera att MariaDB-tjänsten körs efter en playbook är det enklast att använda systemctl, men i en större miljö med många VM:ar är det bättre med automatiserade skript som exempelvis Ansible playbooks eller skript som använder verktyg som Nagios eller Prometheus för hälsokontroller och anslutningstester, eftersom dessa kan köras centralt och ger snabb, skalbar och konsekvent övervakning utan att behöva logga in på varje server manuellt.

