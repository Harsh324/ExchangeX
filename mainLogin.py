import Login.login.login_functions as Log

loginObj = Log.Login()
registerObj = Log.Register()


## Registering a user

userId = input("create a unique userId")
password = input("Enter a strong password")

obj = registerObj.register(userId, password)
if(obj['status'] == True):
    print(obj['info'])
else:
    print(obj['info'])




## login a user
userId = input("Enter your userId")
password = input("Enter your password")

obj = loginObj.validateUser(userId, password)
if(obj['status'] == True):
    print(obj['info']['userId'])
else:
    print(obj['info'])




