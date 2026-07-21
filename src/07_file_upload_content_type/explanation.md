## 07_image_upload

I can see only `jpg` and `jpeg` type files are accepted. And in the body, I could find those lines.
```
Content-Disposition: form-data; name="uploaded"; filename="Screenshot 2026-07-08 at 10.59.04.jpeg"
Content-Type: image/jpeg
```

When I modify header with `.png` file, I got the flag!

FLAG: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8

### Why it is vulnerable

- the app validate uploaded file on;y by their filename and content-type but not with the actual content
- so The server does not verify the real file type before accepting the upload. 
- Attackers can upload files that should not be allowed

- > Attackers can upload files that should not be allowed

- > If exploited, this could allow malicious files to be uploaded and potentially compromise the application

### How to prevent

- > Validate files on the server, never trust the file name or Content-Type sent by the user

- >  Check real type file content(magic bytes), not just the extention

- > Save uploaded files in a non-executable location

- > Scan uploaded files, check files for malware before storing or processing them.