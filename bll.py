import adal
def login (un,ps):
    if len(un) != 0 and len(ps)!= 0:
     result = adal.login(un,ps)
     if result == True:
      return "login to sys"
     else:
       return "invalid user"

    else:
       return "invalid un or pass type"