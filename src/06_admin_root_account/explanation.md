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