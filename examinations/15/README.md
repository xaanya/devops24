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

## SAMMANFATTNING AV VAD JAG GJORT DENNA UPPGIFT: 


I denna uppgift konfigurerades **Prometheus** *(ett övervakningssystem och tidsseriedatabas som samlar in och lagrar metrics från olika system)* och **Node Exporter** *(ett verktyg som exponerar maskin- och systemstatistik till Prometheus)*.

Arbetet delades upp i två delar:

1. **Prometheus på kontrollmaskinen:**
   En container med Prometheus startades via en Ansible-playbook (`prometheus.yml`) med hjälp av **Podman**.
   Konfigurationsfilen `/tmp/scrape-config.yml` skapades automatiskt med de noder som skulle övervakas.
   Prometheus container sattes upp att lyssna på port **9090** och samla in data från både sig själv och de två Node Exporter-instanserna.

2. **Node Exporter på VMs (web och db):**
   En separat Ansible-playbook (`15-node_exporter.yml`) installerade Node Exporter som en **systemd-tjänst** på båda virtuella maskinerna.
   Den skapade en systemanvändare `node_exporter`, laddade ner binären från GitHub, placerade den i `/usr/local/bin`, och öppnade port **9100/tcp** i `firewalld`.
   Tjänsten sattes till att starta automatiskt vid uppstart.

Efter konfiguration verifierades installationen genom att:

* Kontrollera att Node Exporter körde via `systemctl status node_exporter`
* Testa endpoints med `curl http://localhost:9100/metrics`
* Bekräfta i Prometheus webgränssnitt att alla **targets** (`localhost:9090`, `192.168.121.194:9100`, `192.168.121.233:9100`) hade status **UP**

Resultatet är ett fungerande system där **Prometheus automatiskt samlar in och visualiserar systemdata (CPU, minne, disk, nätverk)** från både kontrollmaskinen och de två virtuella maskinerna med Node Exporter.

