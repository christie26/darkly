## 07_image_upload

I can see only `jpg` and `jpeg` type files are accepted. And in the body, I could find those lines.
```
Content-Disposition: form-data; name="uploaded"; filename="Screenshot 2026-07-08 at 10.59.04.jpeg"
Content-Type: image/jpeg
```

When I modify header with `.png` file, I got the flag!

FLAG: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8