import User.user.user_functions as Us;

userObj = Us.User()

## validating a user
userId = input("Enter the userId")
obj = userObj.validateUser(userId)

if(obj['status'] == True):
    print("Kyc status = ", obj['info']['kyc'], " , Balance = ", obj['info']['balance'])
else:
    print(obj['info'])