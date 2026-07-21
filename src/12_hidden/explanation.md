## 12_hidden

### How did we approach

I looked `http://localhost:8080/.hidden/` and there are a lot of recursive directories and they have `readme` file.

I wrote a script to crawl them and save content with mapping. 


```
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4
```

I could find one flag file there.

FLAG : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

### Why it is vulnerable

- hidden directories are public so accesible and reveal internal files

- the app relies on hidinng folders instead of properly protecting them with access control

- the server allow to browse directories, so private folder/files can be access

- attackers can use scripts to automatically scan and collect hidden or sensitive data 

- can provide attackers with additional information to find other vulnerability

### How to prevent

- > Restrict access to sensitives directories

- > Diseable Directory listning, so prevent users from nrowsing server folders 

- > user proper acces control to protect sensitive file

- > only make required files publicy accessible

- > perform regular security audits, scan the app for exposed files ans directories before deployment 

