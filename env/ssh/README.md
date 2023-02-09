

## sshfs

```
sshfs user@ip:remotepath localpath
```

## ssh

root login
```
/etc/ssh/sshd_config
PermitRootLogin yes
```

## ssh no password login

```
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub user@ip
```
