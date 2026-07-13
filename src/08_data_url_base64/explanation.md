## 08_data_url_base64

### How did we approach

I found one link which bring us to this path.

`http://localhost:8080/index.php?page=media&src=nsa`
It shows 'File: nsa_prism.jpg' on the screen.

Let's try to understand what `src` is here.

When we put random value for `src`, we can see the site broken.

Here, we could find some examples of base64-encoded data url and also how to encode data in base64.

`https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data`

```
data:text/html,%3Cscript%3Ealert%28%27hi%27%29%3B%3C%2Fscript%3E
data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGknKTs8L3NjcmlwdD4=
```
I don't understand why when we do url encoding, it shows alert and when we do base64 encoding it shows flag.

It's interesting that I tried to modify url and it shows flag until `PHNjcmlwdD5hbGVydC` and when I decode it, it's `<script>aler`

Then I tried to encode `<sciprt>alert`, it also gives us the flag. 

I assumed that it decode the text and check if there's specific word in it.

FLAG : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d


### Why it is vulnerable

### How to prevent
