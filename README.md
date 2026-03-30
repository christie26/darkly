## How to run
```
qemu-system-x86_64 -m 1024 -cdrom Darkly_i386.iso -netdev user,id=net0,hostfwd=tcp::8080-:80 -device e1000,netdev=net0
```