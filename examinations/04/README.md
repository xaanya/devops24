# Examination 4 - Install a Web Server

Now that we know how to install software on a machine through Ansible, we can
begin to look at how to set up a machine with services.

A typical use case is how to get a web server up and running, and coincidentally
we happen to have one of our hosts named `webserver`.

As in the previous examination, we can use the [ansible.builtin.package](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html)
module to install the prerequisite software.

Create a new file, you can call it what you like, but in the example below, it's referred to as
`webserver.yml`.

    ---
    - name: Install a webserver
      hosts: web
      become: true
      tasks:
        - name: Ensure nginx is installed
          ansible.builtin.package:
            name: nginx
            state: latest

        - name: Ensure nginx is started at boot
          ansible.builtin.service:
            name: nginx
            enabled: true

The above is a playbook that will install [nginx](https://nginx.org/), a piece of software that can
act as a HTTP server, reverse proxy, content cache, load balancer, and more.

Now, we can run `curl` to see if web server does what we want it to (serve HTTP pages on TCP port 80):

    $ curl -v http://<IP ADDRESS OF THE WEBSERVER>

Change the text within '<' and '>' to the actual IP address of the web server. It may work with the
name of the server too, but this depends on how `libvirt` and DNS is set up on your machine.

Is the response what we expected?

    $ curl -v http://192.168.121.10
    *   Trying 192.168.121.10:80...
    * connect to 192.168.121.10 port 80 from 192.168.121.1 port 46036 failed: Connection refused
    * Failed to connect to 192.168.121.10 port 80 after 0 ms: Could not connect to server
    * closing connection #0
    curl: (7) Failed to connect to 192.168.121.10 port 80 after 0 ms: Could not connect to server

# QUESTION A

Refer to the documentation for the [ansible.builtin.service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html)
module.

How can we make the web server start with an addition of just one line to the playbook above?

ANSWER: Jag lade till raden state: started längst ner i playbook-filen.
Detta säkerställer att nginx inte bara aktiveras för att starta automatiskt vid systemstart, utan också startas direkt när playbooken körs.

Det behövdes eftersom vi utan denna rad fick felmeddelandet "Connection refused" när vi försökte ansluta till webservern.
Det berodde på att tjänsten då inte var igång, trots att den var installerad och satt att starta vid boot.
Så utan state: started startas nginx först vid nästa omstart av systemet, men inte direkt. Och det var därför som curl inte fungerade till att börja med.

# QUESTION B

You make have noted that the `become: true` statement has moved from a specific task to the beginning
of the playbook, and is on the same indentation level as `tasks:`.

What does this accomplish?

SVAR: Allt som ligger under tasks på samma indentering som become:true kommer att köras med root-rättigheter. På så vis slipper man skriva become:true om och om igen eftersom root-rättigheter behövs för de tasks som finns med i playbooken. 

# QUESTION C

Copy the above playbook to a new playbook. Call it `04-uninstall-webserver.yml`.

Change the ordering of the two tasks. Make the web server stop, and disable it from starting at boot, and
make sure that `nginx` is uninstalled. Change the `name:` parameter of each task accordingly.

Run the new playbook, then make sure that the web server is not running (you can use `curl` for this), and
log in to the machine and make sure that there are no `nginx` processes running.

Why did we change the order of the tasks in the `04-uninstall-webserver.yml` playbook?

SVAR: Man behövde ändra ordningen på tasks eftersom nginx-tjänsten måste stoppas innan den avinstalleras.
Om man tar bort paketet först kan tjänsten fortfarande vara igång, vilket kan orsaka fel eller lämna kvar processer.

# BONUS QUESTION

Consider the output from the tasks above, and what we were actually doing on the machine.

What is a good naming convention for tasks? (What SHOULD we write in the `name:` field`?)

SVAR: Det är viktigt att använda namn som tydligt beskriver vad varje task gör och vilket tillstånd man vill uppnå, till exempel “Ensure nginx is uninstalled”. På så sätt undviker man missförstånd och oklarheter när playbooken körs eller när andra läser den. Det gör också felsökning och underhåll enklare eftersom man snabbt förstår syftet med varje steg.