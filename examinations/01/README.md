# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?

Why are the permissions set in such a way?

ANSWER_: drwx, vilket betyder att det är ett directory och att jag som ägare har read, write och execute. Det är endast ägaren som har rättigheter. Varken grupp eller other har några rättigheter. ~/.ssh har känsliga uppgifter, så som hashade nycklar och det kan vara förklaringen till varför rättigheterna är formade på det viset. 



## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?

ANSWER: ~/.ssh/authorized_keys är en fil som finns på en server och innehåller en lista med publika SSH-nycklar. När du försöker logga in via SSH kontrollerar servern om din privata nyckel matchar någon av dessa publika nycklar. Om det stämmer tillåts du logga in utan lösenord. Filen innehåller endast publika nycklar.Privata nycklar ska alltid förvaras säkert på din egen dator och aldrig på servern.

## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password?

ANSWER: Det behövs genereras en nyckel på VM1 med "ssh-keygen -t ed25519
". Sedan kopiera den publika nyckeln till VM2 med "ssh-copy-id användare@vm2" eller manuellt genom att kopiera innehållet i ~/.ssh/id_ed25519.pub och klistra in i ~/.ssh/authorized_keys på VM2.
Sedan räcker det med att skriva "ssh webserver"


### Hints:

* man ssh-keygen(1)
* ssh-copy-id(1) or use a text editor


## BONUS QUESTION

Can you run a command on a remote host via SSH? How?

ANSWER: 

Du ansluter till fjärrdatorn via SSH genom att skriva ssh följt av användarnamn eller adress, och sedan kommandot du vill köra inom citattecken direkt efter, vilket gör att kommandot körs på fjärrdatorn utan att du behöver logga in interaktivt.