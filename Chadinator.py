from instabot import Bot

bot = Bot()
a = input("Enter ur insta id:- ")
b = input("Enter ur insta pass:- ")
bot.login(username=a, password=b)
bot.follow("king_hu_bhai69")
bot.unfollow("puneetsuper_staar")
