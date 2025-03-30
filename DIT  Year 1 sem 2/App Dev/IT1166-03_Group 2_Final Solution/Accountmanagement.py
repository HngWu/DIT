import UserData
import shelve, secrets
from datetime import datetime


class accountcreation(UserData.Userdetails):
    def __init__(self, Date, Name, Email, address, ID):
        super().__init__(Name, Email, address, Date, ID)


#getters
    def get_ID(self):
        return self.__UserID__

    def get_date(self):
        return self.__datentime__

    def get_name(self):
        return self.__username__

    def get_email(self):
        return self.__email__

    def get_address(self):
        return self.__address__

#setters

    def set_name(self, name):
        self.__username__ = name

    def set_email(self, email):
        self.__email__ = email

    def set_address(self, address):
        self.__address__ = address

    def print(self):
        print(self.__UserID__)

#functions




def UIDcreation():
    UserData.Userdetails.UIDcreation(UserData.Userdetails)

def settingdate():
    UserData.Userdetails.date(UserData.Userdetails)

def savinguserdata(user, email, address):
    UID = accountcreation.get_ID()
    Userinfo = shelve.open('user_data')
    Userinfo[UID] = {"user": user, "email": email, "address": address}
    Userinfo.close



if __name__ == '__main__':
    UIDcreation()
    UserData.Userdetails.print_uid(UserData.Userdetails)


