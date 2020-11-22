# class User:
#
#     def __init__(self, userId, UserName):
#         self.userId = userId
#         self.userName = UserName


# UserId = input("Enter your User Id")
# UserName = input("Enter your User Name")
#
# user1 = User(UserId, UserName)
#
# print(user1.userId)
# print(user1.userName)


class User:
    def __init__(self, username, userid):
        self.id = userid
        self.name = username
        self.followers = 0
        self.following = 0
        self.post = 0

    """When function is attached to object called method"""

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User('Abhishek', 'Abhishek1920')
user2 = User('Angela', 'Yu')

user1.follow(user2)
print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)