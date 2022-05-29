# CS162-fa21

This is my code for studying [CS162-fa21](https://inst.eecs.berkeley.edu/~cs162/fa21/)

You can watch the video in the [youtube](https://www.youtube.com/channel/UCnhpOONF1c1FtipDF8LPdqQ)

## The envrionment setup

```sh
sudo pacman -S virtualbox vagrant
mkdir cs162-vm
# the spring2022 maybe changed
vagrant init cs162/spring2022
vagrant up
vagrant ssh
```

Use VsCode to remote:

```sh
varant ssh-config
```

Copy the content to Remote-SSH configuration.

```ini
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/shejialuo/.vagrant.d/boxes/cs162-VAGRANTSLASH-spring2022/1.0.2/virtualbox/vagrant_private_key
  IdentitiesOnly yes
  LogLevel FATAL
```

