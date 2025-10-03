# Examination 6 - Handling Web Server Content

The default web pages for any web server are not very interesting to look at.

If we open a web browser and point it towards the address of our web server,
you will likely get the default content of an unconfigured and unmanaged
web server:

Open Firefox or Chrome and enter the IP address of the web server, either
with http:// or http://

You should se a super snazzy web page from Alma Linux telling the visitor
that the administrator of this server needs to get their act together.

Also note that if you use https:// for secure HTTP, you will get a warning
telling you that you should be very careful accepting non-validating
certificates (such as the one we created earlier). This is normal, and
since we were the ones creating the certificate, we can just add an
exception for accepted certs, or simply use the http:// URL.

We will create a _virtual host_ on our web server, that serves different
content depending on which address it is called by via web browsers.

## Configure the nginx virtual host

The virtual host we will create will be called "example.internal", so that when we
go to http://example.ínternal or https://example.internal, our own web page
will be displayed instead. Obviously, this is a fake address, so we need
to do some black magic on our own machines first.

We will edit the file `/etc/hosts` on our host machine (i.e. the computer
you are working on).

Add the following line to this file:

    192.168.121.10  example.internal

Note that you need to be `root` to be able to edit this file, and that the address
given above is just an example. The actual IP of your `webserver` machine is
what we are interested in.

See if you now can resolve the name `example.internal`:

    $ ping -c 1 example.internal
    PING example.internal (192.168.121.10) 56(84) bytes of data.
    64 bytes from example.internal (192.168.121.10): icmp_seq=1 ttl=64 time=0.446 ms
    
    --- example.internal ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 0.446/0.446/0.446/0.000 ms

Again, the actual IP address it resolves to may be different on your machine.

If you have come this far, we can now move on to the next step.

## Upload our web page to the virtual host directory

Let's make a web page and upload to the web server so we can display our
own content instead.

Make a web page that looks something like this:

```xml
<?xml version="1.0"?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello Nackademin!</title>
  </head>
  <body>
    <h1>Hello Nackademin!</h1>
    <p>This is a totally awesome web page</p>
    <p>This page has been uploaded with <a href="https://www.ansible.com">Ansible</a>!</p>
  </body>
</html>
```

Note that this web page follows the HTML standards from W3C, in case you are
interested in why it looks the ways it does: https://html.spec.whatwg.org/multipage/

There is a copy of this file in the `files/index.html` directory adjacent to where
you are reading this file.
