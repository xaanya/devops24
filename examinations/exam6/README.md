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

Let's make a web page and upload to the web server so we can display our
own content instead.

Make a web page that looks something like this:

```html
<?xml version="1.0"?`>
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
