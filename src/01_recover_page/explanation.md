In recover page, there is `mail` and `Submit` and value of `mail` is set as `webmaster@borntosec.com`

When we change it to anything else, and click on Submit, they give us a flag!

FLAG: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0


### Why it is vulnerable

A hacker can request a pasword reset for another user;
send thousands of reset emails (spam);
test which email addresses exist on the site (user enumeration) if responses differ based on the address

Since the server does not verify that the submitted email is expected or authorized, it accepts arbitrary values. In a real application, this could lead to abuse of the password recovery process, user enumeration, or other business logic attacks.

### How to prevent
- > Never trust values sent by the client, even if they are pre-filled or hidden in a form
- > Not rely on a client-supplied email address,  instead, retrieve the correct email from the server or database
- > Verify that the submitted email belongs to an existing and authorized user before processing the request
