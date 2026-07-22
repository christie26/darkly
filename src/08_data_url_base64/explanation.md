## 08_data_url_base64

### How did we approach

I found one link which bring us to this path.

`http://localhost:8080/index.php?page=media&src=nsa`
It shows 'File: nsa_prism.jpg' on the screen.

Let's try to understand what `src` is here.

When we put random value for `src`, we can see the site broken.

[Here](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data), we could find some examples of base64-encoded data url and also how to encode data in base64.

Let's encode this string
```
<script>alert('hi');</script>
```

With percent-encoded, `src=data:text/html,%3Cscript%3Ealert%28%27hi%27%29%3B%3C%2Fscript%3E`

With base64 encoded, `src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGknKTs8L3NjcmlwdD4=`

I don't understand why when we do url encoding, it shows alert and when we do base64 encoding it shows flag.

It's interesting that I tried to modify url and it shows flag until `PHNjcmlwdD5hbGVydC` and when I decode it, it's `<script>aler`

Then I tried to encode `<sciprt>alert`, it also gives us the flag. 

I assumed that it decode the text and check if there's specific word in it.

FLAG : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d


### Why it is vulnerable

src parameter in the URL is vulnerable because it let the user to send any data (image name, html or javaScript...) he want, all data are decoded (Base64) and treat by the app, the user can do a XSS (Cross-Site Scripting -> injection of javascript code) attack

Base64 do not protect, it's just another way to write text

By a XSS attack, hacker can stole cookies, redirect to a bad website
change website content...


### How to prevent

First, the dev should never trust the user (logicaly)
Parse url :
- > only allowed real image name
- > check if image name corresponds well to an existing image
- > refuse url begin with data
- > forbid caractere like < > " ' (javascript content)
