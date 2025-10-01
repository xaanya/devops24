# Lab Environment Setup

To setup the lab environment on your machine, just run

    $ vagrant up

in this directory. If you have set up your system to allow your user to
use virtualization resources on the machine, such as being in a 'libvirt'
group or equivalent, you don't need to use `sudo` or any similar mechanism
to run it as root.

If your OS or setup does not allow for running virutalization directly
as a user, run it as

    $ sudo vagrant up

This assumes `vagrant` in your PATH. If not, check your OS for how to
get Vagrant installed.

If successful, this should set up a couple of virtual machines via libvirt.

They should be accessible by name in case your operating system / libvirt setup
allows it, i.e:

    $ ssh -i deploy_key -l deploy webserver

should make it possible to SSH into the machine.

To see more information about the machines from the command line, you can use

    virsh -c qemu:///system list --all

