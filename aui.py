import bll
username = input("pls enter username")
password = input("pls enter password")
natije = bll.login(username,password)
print(natije)

## Test login- username: `ali`- password: `123`