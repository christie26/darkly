## 11_etc_passwd

### How to approach
In this project, I realize that we always change path after 'page'.

It might be relative path. So I tried other words and '..' path.

For `../sth`, they still say 'WTF?'

But for `../../sth`, they said 'Wrong..'

They said 'Nope', 'Almost' things

At some point they said "You can DO it !!!  :]"


`http://localhost:8080/?page=../../../../../../../etc/passwd`




FLAG : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 

### Why it is vulnerable

- Path traversal, the app not properly validate the page parameter, allowing attackers navigate outside the intended directory using ../

- Unauthorise file access, attackers can read sensitive as /etc/psswd, should not be public

- Leak information, exposed files can reveal useful information about the server and help attackers prepare further attacks.

- > Security risk, access to internal files can help attackers discover weaknesses and potentially gain more control over the system.


### How to prevent

- > check user input, should refuse or redirect any input transversal path (../ or ..\\)

- > Only allow access to specific approved pages or files instead of letting users choose any file 

- > Make sure the application can only access files that are necessary for its operation.

- >Protect system files, be sure sensitive files qnd server information cannot be accessed from the website

- > Limit permissions, give the application minimum access rights it needs to work