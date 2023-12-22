class StarCookie:
    price = 50

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

print(StarCookie.price)

star_cookie1 = StarCookie("Red", 16)
star_cookie1.price = 55
print(star_cookie1.color)
print(star_cookie1.weight)
print(star_cookie1.price)

star_cookie2 = StarCookie("Blue", 15)
print(star_cookie2.color)
print(star_cookie2.weight)
print(star_cookie2.price)

print(StarCookie.__dict__)
print(star_cookie1.__dict__)
print(star_cookie2.__dict__)




class Youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers

user1 = Youtube("Shibayan")
user1.likes = 10
print(user1.username)
print(user1.subscribers)
print(user1.likes)

user2 = Youtube("Elshad")
user2.subscribrs = 5
print(user2.username)
print(user2.subscribers)
