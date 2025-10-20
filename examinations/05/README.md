# Examination 5 - Handling Configuration Changes

Today, plain HTTP is considered insecure. Most public facing web sites use the encrypted HTTPS
protocol.

In order to set up our web server to use HTTPS, we need to make a configuration change in nginx.

## Preparations

Begin by running the [install-cert.yml](install-cert.yml) playbook to generate a self-signed certificate
in the correct location on the webserver.

You may need to install the Ansible `community.crypto` collection first, unless you have
already done so earlier.

In the `lab_environment` folder, there is a file called `requirements.yml` that can be used like this:

    $ ansible-galaxy collection install -r requirements.yml

Or, if you prefer, you can install the collection directly with

    $ ansible-galaxy collection install community.crypto

# HTTPS configuration in nginx

The default nginx configuration file suggests something like the following to be added to its
configuration:

    server {
        listen       443 ssl;
        http2        on;
        server_name  _;
        root         /usr/share/nginx/html;

        ssl_certificate "/etc/pki/nginx/server.crt";
        ssl_certificate_key "/etc/pki/nginx/private/server.key";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_ciphers PROFILE=SYSTEM;
        ssl_prefer_server_ciphers on;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
    }

There are many ways to get this configuration into nginx, but we are going to copy
this as a file into `/etc/nginx/conf.d/https.conf` with Ansible with the
[ansible.builtin.copy](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html)
module.

If you have gone through the preparation part for this examinination, the certificate and the key for the
certificate has already been created so we don't need to worry about that.

In this directory, there is already a file called `files/https.conf`. Copy this directory to your Ansible
working directory, with the contents intact.

Now, we will create an Ansible playbook that copies this file via the `ansible.builtin.copy` module
to `/etc/nginx/conf.d/https.conf`.

# QUESTION A

Create a playbook, `05-web.yml` that copies the local `files/https.conf` file to `/etc/nginx/conf.d/https.conf`,
and acts ONLY on the `web` group from the inventory.

Refer to the official Ansible documentation for this, or work with a classmate to
build a valid and working playbook, preferrably that conforms to Ansible best practices.

Run the playbook with `ansible-playbook` and `--verbose` or `-v` as option:

    $ ansible-playbook -v 05-web.yml

The output from the playbook run contains something that looks suspiciously like JSON, and that contains
a number of keys and values that come from the output of the Ansible module.

ANTECKNING: 
Här skapades en playbook 05-web.yml som kopierar filen files/https.conf till /etc/nginx/conf.d/https.conf på servrarna i gruppen web.
Playbooken använder ansible.builtin.copy modulen för att kopiera filen.
Vi körde playbooken med ansible-playbook -v 05-web.yml för att se detaljerad output.

What does the output look like the first time you run this playbook?


What does the output look like the second time you run this playbook?


SVAR: Första körningen av playbooken visar att filen /etc/nginx/conf.d/https.conf kopierades och ändrades på servern ("changed": true), vilket betyder att konfigurationen lades in.
Andra körningen visar att filen redan var på plats och oförändrad, och därför skedde inga ändringar ("changed": false). Detta visar att playbooken är idempotent, vilket är en viktig egenskap i Ansible.

# QUESTION B

Even if we have copied the configuration to the right place, we still do not have a working https service
on port 443 on the machine, which is painfully obvious if we try connecting to this port:

    $ curl -v https://192.168.121.10
    *   Trying 192.168.121.10:443...
    * connect to 192.168.121.10 port 443 from 192.168.121.1 port 56682 failed: Connection refused
    * Failed to connect to 192.168.121.10 port 443 after 0 ms: Could not connect to server
    * closing connection #0
    curl: (7) Failed to connect to 192.168.121.10 port 443 after 0 ms: Could not connect to server

The address above is just an example, and is likely different on your machine. Make sure you use the IP address
of the webserver VM on YOUR machine.

In order to make `nginx` use the new configuration by restarting the service and letting `nginx` re-read
its configuration.

On the machine itself we can do this by:

    [deploy@webserver ~]$ sudo systemctl restart nginx.service

Given what we know about the [ansible.builtin.service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html),
how can we do this through Ansible?

Add an extra task to the `05-web.yml` playbook to ensure the service is restarted after the configuration
file is installed.

When you are done, verify that `nginx` serves web pages on both TCP/80 (http) and TCP/443 (https):

    $ curl http://192.168.121.10
    $ curl --insecure https://192.168.121.10

Again, these addresses are just examples, make sure you use the IP of the actual webserver VM.

Note also that `curl` needs the `--insecure` option to establish a connection to a HTTPS server with
a self signed certificate.

SVAR: För att starta om nginx-tjänsten via Ansible använde vi modulen ansible.builtin.service och la till state: restarted. Det gör att tjänsten startas om, vilket tvingar nginx att läsa in den nya konfigurationen.

Efter att vi kopierat HTTPS-konfigurationsfilen till rätt plats fungerade inte HTTPS-tjänsten direkt eftersom nginx måste läsa om sin konfiguration för att aktivera ändringarna. För att göra detta måste nginx-tjänsten startas om. Genom att använda Ansible kan vi lägga till en extra uppgift i playbooken som säkerställer att nginx startas om efter att filen kopierats. När detta är gjort och playbooken körts kan vi verifiera att nginx nu svarar på både port 80 för HTTP och port 443 för HTTPS. För att testa detta använder man verktyget curl, där man även måste lägga till ett extra kommando för att acceptera ett självsignerat certifikat vid HTTPS. Efter detta bekräftades att HTTPS fungerar som det ska.
# QUESTION C

What is the disadvantage of having a task that _always_ makes sure a service is restarted, even if there is
no configuration change?

SVAR: Nackdelen med att alltid starta om en tjänst i en Ansible-uppgift, oavsett om det har skett någon konfigurationsändring eller inte, är att det kan leda till onödiga avbrott i tjänsten. Detta kan orsaka problem, särskilt i produktion, eftersom tjänsten kan vara otillgänglig under omstarten. Om omstarten sker samtidigt som andra processer eller uppgifter körs kan det även leda till krockar eller fel i systemet. Dessutom är det ineffektivt och kan slösa resurser att starta om tjänsten utan anledning.

Därför är det bättre att bara starta om tjänsten när det faktiskt har skett en förändring i konfigurationen, vilket i Ansible ofta hanteras genom att använda notify och handlers.

# BONUS QUESTION

There are at least two _other_ modules, in addition to the `ansible.builtin.service` module that can restart
a `systemd` service with Ansible. Which modules are they?

SVAR: ansible.builtin.systemd
Denna modul är mer specifikt riktad mot systemd och ger fler möjligheter för att hantera systemd-enheter, inklusive start, stopp, omstart, aktivering och inaktivering.

ansible.builtin.command (eller ansible.builtin.shell)
Fast det inte är en dedikerad service-modul kan man köra kommando som t.ex. systemctl restart nginx direkt via dessa moduler för att starta om en tjänst. Det är mindre elegant men funkar i de fall där man vill köra specifika kommandon.