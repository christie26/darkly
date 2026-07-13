
I looked `http://localhost:8080/.hidden/` and there are a lot of recursive directories and they have `readme` file.

I wrote a script to crawl them and save content with mapping. 


```
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4
```

I could find one flag file there.

FLAG : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466