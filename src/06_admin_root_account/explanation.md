## 06

When I access to `http://localhost:8080/robots.txt`

I can see

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

Then access to `http://localhost:8080/whatever/`

There, I could download one file name `htpasswd`

```
root:437394baff5aa33daa618be47b75cb49
```

is qwerty123@ in MD5

I couldn't access to admin page with `http://localhost:8080/admin/` but it works with `http://127.0.0.1:8080/admin/`

FLAG: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff


### Why it is vulnerable

- file robots.txt contains sensitive information, helping attackers discover hidden resources
- htpsswd is accessible, so hash password are leaked
- MD5 hash is an old algorithm vulnerable
- Broken access control, cannot access to `http://localhost:8080/admin/` but it works with `http://127.0.0.1:8080/admin/`

- > Compromised administrator credentials can lead to full administrative access.

- > an attacker could modify data, create or delete users, upload malicious files, or take complete control of the application

### How to prevent

- > protect access to routes, here http://localhost:8080/robots.txt and http://127.0.0.1:8080/admin/

- >  restrick access to files, here htpsswd

- > Use stronger hashing password as Argon2, bcrypt, or scrypt

- > Limit administrative permissions and restrict access to sensitive interfaces

- > Authenticate and authorize users based on roles, not on hostnames or client-controlled values.