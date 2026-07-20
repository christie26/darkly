## 00_I_am_admin

### How did we approach
In cookie, I can find `I_am_admin` key.

`I_am_admin`: 68934a3e9455fa72420237eb05902327

This was `false` when we converted using "MD5 hash".

So we put `true` instead of `false` and it gave us this flag!

FLAG: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

### Why it is vulnerable
They use hashing for `I_am_admin` value, but with weak hashing system which is [MD5](https://en.wikipedia.org/wiki/MD5). 


### How to prevent
It's better to use token value to check user's permission.

Good practice for user permission
```
always send token together in API call

-> check user's permission (admin, have specific permission, etc)
```