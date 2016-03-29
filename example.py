from notice_me import AttentionWhore

username = input("github username: ")
password = input("github password (or access code): ")
project = input("github project: ")
star_count = input(
    "how many stars should your \"collaborators\" have? (1000) ")

if star_count == "":
    star_count = 1000
else:
    try:
        star_count = int(star_count)
    except:
        star_count = 1000

kardashian = AttentionWhore(username, password)

print("getting the user list")

user_list = kardashian.get_users(star_count)

print("adding \"collaborators\"")

for user in user_list:
    print(user)
    #kardashian.touch_collaborator(project, user)
