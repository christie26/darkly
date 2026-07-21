## 05_survey

We can see there's form submit everytime we select value.

I modify value to `100`, it gives me a flag.

FLAG = 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa

### Why it is vulnerable

The survey is expected to accept only predefined values but user bypassed using browser developer tools or by modifying the HTTP request, this demostrates that the app relies on client-side

### How to prevent
- > Validate all submitted values on the server.
- > Accept only expected values and reject other values
- > Never rely solely on client-side validation, as it can be modified or bypassed by an attacker
