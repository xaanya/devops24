# Examination 15 - Metrics (VG)

[Prometheus](https://prometheus.io/) is a powerful application used for event monitoring and alerting.

[Node Exporter](https://prometheus.io/docs/guides/node-exporter/) collects metrics for Prometheus from
the hardware and the kernel on a machine (virtual or not).

Start by running the Prometheus server and a Node Exporter in containers on your Ansible controller
(the you're running Ansible playbooks from). This can be accomplished with the [prometheus.yml](prometheus.yml)
playbook.

You may need to install [podman](https://podman.io/docs/installation) first.

If everything worked correctly, you should see the data exported from Node Exporter on http://localhost:9090/,
and you can browse this page in a web browser.

# QUESTION A

Make an Ansible playbook, `15-node_exporter.yml` that installs [Node Exporter](https://prometheus.io/download/#node_exporter)
on each of the VMs to export/expose metrics to Prometheus.

Node exporter should be running as a `systemd` service on each of the virtual machines, and
start automatically at boot.

You can find `systemd` unit files that you can use [here](https://github.com/prometheus/node_exporter/tree/master/examples/systemd), along with the requirements regarding users and permissions.

Consider the requirements carefully, and use Ansible modules to create the user, directories, copy files,
etc.

Also, consider the firewall configuration we implemented earlier, and make sure we can talk to the node
exporter port.

HINT: To get the `firewalld` service names available in `firewalld`, you can use

    $ firewall-cmd --get-services

on the `firewalld`-enabled hosts.

Note also that while running the `podman` containers on your host, you may sometimes need to stop and
start them.

    $ podman pod stop prometheus

and

    $ podman pod start prometheus

will get you on the right track, for instance if you've changed any of the Prometheus configuration.

GJORT:

# QUESTION A - Node Exporter installation

Vi skapade Ansible-playbooken `15-node_exporter.yml` som installerar och konfigurerar Node Exporter på alla servrar i inventariet. 

Playbooken gör följande:

1. Skapar systemanvändaren `node_exporter`.
2. Laddar ner och packar upp Node Exporter från officiella GitHub-releasen.
3. Flyttar binären till `/usr/local/bin` med rätt behörigheter.
4. Kopierar systemd unit-filen till `/etc/systemd/system/`.
5. Startar och aktiverar Node Exporter-tjänsten via systemd.
6. Öppnar brandväggen för port 9100 (Node Exporter).

Efter körning kan Prometheus ansluta till Node Exporter på port 9100, och `curl http://<host>:9100/metrics` visar exportade systemmetrics.  

Kontroll: Prometheus `Targets` visar alla servrar som `up`.




# Resources and Information

* https://github.com/prometheus/node_exporter/tree/master/examples/systemd
* https://prometheus.io/docs/guides/node-exporter/
