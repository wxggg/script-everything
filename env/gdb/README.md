

## kgdb

set architecture
for cross platform
```
apt install gdb-multiarch
```

x86
```
set architecture i386:x86-64
```

arm
```
set architecture aarch64
```

qemu add extra args:
```
-serial tcp::1234,server,nowait
```

linux kernel boot config
```
GRUB_CMDLINE_LINUX_DEFAULT="splash quiet kgdboc=ttyS1,115200 kgdbwait"

update-grub
```

add-symbol-file 
```
lsmod or monitor lsmod to get offset
add-symbol-file /path/to/ko offset
```

break kernel
```
echo g > /proc/sysrq-trigger
```
