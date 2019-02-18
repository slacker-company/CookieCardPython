import CookieCard
import time
try:
    import colorama
    green = colorama.Fore.LIGHTGREEN_EX
    red = colorama.Fore.LIGHTRED_EX
    reset = colorama.Style.RESET_ALL
except:
    green = ""
    red = ""
    reset = ""

userName = "ttatanepvp123"

currentUser = CookieCard.User(userName)
while True:
    lastUser = currentUser
    currentUser = CookieCard.User(userName)
    if lastUser.money < currentUser.money:
        print(f"{green}balance +{currentUser.money - lastUser.money}{reset}")
    elif lastUser.money < currentUser.money:
        print(f"{red}balance -{currentUser.money - lastUser.money}{reset}")
    time.sleep(2.5)