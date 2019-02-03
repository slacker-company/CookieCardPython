import requests

buildForApiVersion = "0.0.1"
buildForApiVersionSplited = BuildForApiVersion.split(".")

class noLogged(Exception):
    pass

class apiError(Exception):
    pass

class obsoletAPI(Exception):
    pass

def signup(name, mail, password):
    try:
        tmp = requests.post("https://slackercompany.ml/CarteCookie/api/", data={"action":"signup", "name":name, "mail":mail, "password":password}).json()
        if tmp["success"]:
            return True
        else:
            raise apiError(tmp["error"], ["errorMessage"])
    except Exception as e:
        print(e)
        return False

class UserRemote():
    session=None
    def __init__(self, name, password):
        self.session = requests.session()
        tmp = self.session.post("https://slackercompany.ml/CarteCookie/api/", data={"action":"login", "name":name, "password":password}).json()
        if not tmp["success"]:
            self.close()
            raise noLogged(tmp["error"], tmp["errorMessage"])
        else:
            self.name = tmp["user"]["name"]
            self.money = tmp["user"]["money"]
            self.mail = tmp["user"]["mail"]
            self.isDev = tmp["user"]["money"]
            self.id = tmp["user"]["id"]
            tmp = self.session.post("https://slackercompany.ml/CarteCookie/api/", data={"action":"info"}).json()
            self.APIversion = tmp["APIversion"]
            minimalAPIversion = tmp["minimalAPIversion"].split(".")
            if int(minimalAPIversion[0]) > int(BuildForApiVersionSplited[0]):
                raise obsoletAPI()
            elif int(minimalAPIversion[1]) > int(BuildForApiVersionSplited[1]):
                raise obsoletAPI()
            elif int(minimalAPIversion[2]) > int(BuildForApiVersionSplited[2]):
                raise obsoletAPI()
    def transfer(self, target, amount):
        tmp = self.session.post("https://slackercompany.ml/CarteCookie/api/", data={"action":"transfer", "target":target, "amount":amount}).json()
        if not tmp["success"]:
            raise apiError(tmp["error"], tmp["errorMessage"])
    def disconnect(self):
        self.session.post("https://slackercompany.ml/CarteCookie/api/", data={"action":"disconnect"})
        self.close()
    def changepassword(oldPassword, newPassword):
        tmp = self.session.post("https://slackercompany.ml/CarteCookie/api/", data={"action":"changePassword", "oldPassword":oldPassword, "newPassword":newPassword})
        if not tmp["success"]:
            raise apiError(tmp["error"], tmp["errorMessage"])
    def close(self):
        del(self)