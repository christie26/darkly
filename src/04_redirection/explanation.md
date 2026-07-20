## 04_redirection

### How did we approach

Under the page, there is facebook, twitter, instagram icon.

When I inspect them,

```
<a class="sth" href="index.php?page=redirect&site=twitter"> </a>
```
Which means, clicking this icon brings us to specific page
```
facebook  -> https://www.facebook.com/42born2code/
twitter   -> https://twitter.com/42born2code
instagram -> https://www.instagram.com/42born2code/

hello -> https://www.hello.com/42born2code/
```
We can find out that they redirect us to `https://www.{site keyword}.com/42born2code/`

Which mean we can redirect to wherever ends with `/42born2code`.


I put this url instead I got a flag.

`http://localhost:8080/index.php?page=redirect&site=hello`

FLAG = b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

### Why it is vulnerable
It can cause unintened redirection.

It can bring users to phishing page.

### How to prevent
Again, never trust user-controlled data!

Instead of use user input as parameter, make mapping between keyword and url for example
```
happy -> https://happy-day/42
sad   -> http://horrible-jour/21
```
so that user cannot manipulate url path.
