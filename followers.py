import instaloader

L = instaloader.Instaloader()

username = "stest495"
password = "123chris"

L.login(username, password)


profile = instaloader.Profile.from_username(L.context, "shresthaupadhyaay")

follow_list = []
count = 0

# bio = profile.biography
# print(bio)
# print(profile.get_followers())
for followers in profile.get_followers():
    print(followers)
# for followee in profile.get_followers():
#     # print()
    
#     follow_list.append(followee.username)
#     file = open("followers.txt", "a+",encoding="utf-8")
#     file.write(followee.full_name)
#     file.write(f" : {follow_list[count]}")
#     file.write("\n")
#     file.close()
#     print(follow_list[count])
#     count = count + 1
# (likewise with profile.get_followers())
