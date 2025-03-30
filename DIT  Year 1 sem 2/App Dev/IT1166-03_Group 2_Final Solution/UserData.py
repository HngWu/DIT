import shelve, secrets
from datetime import datetime


class Userdetails:
    def __init__(self,ID ,Name, Email, address, Date):
        self.__UserID__ = ID
        self.__username__ = Name
        self.__email__ = Email
        self.__address__ = address
        self.__datentime__ = Date


#getters
    def get_ID(self):
        return self.__UserID__

    def get_name(self):
        return self.__username__

    def get_email(self):
        return self.__email__

    def get_address(self):
        return self.__address__
    def get_datentime(self):
        return self.__datentime__


#setters
    def set_ID(self, UID):
        self.__UserID__ = UID

    def set_name(self, name):
        self.__username__ = name

    def set_email(self, email):
        self.__email__ = email

    def set_address(self, address):
        self.__address__ = address

    def set_date(self, date):
        self.__datentime__ = date


#others
    def print_date(self):
        print(self.__datentime__)
    def print_uid(self):
        print(self.__UserID__)
    def UIDcreation(self):

        Userinfo = shelve.open('user_data')
        while True:
            UID = secrets.token_hex(8)[:8]
            if UID not in Userinfo:
                break
        Userdetails.set_ID(self, UID)

    def settingdatentime(self):
        date = datetime.now()
        return date.strftime('%d/%m/%y')

    def date(self):
        date = Userdetails.settingdatentime(self)
        Userdetails.set_date(self, date)


    def savinguserdata(self, user, email, address):
        """

        :rtype: object
        """
        #UID
        Userdetails.UIDcreation(self)
        UID = Userdetails.get_ID(self)
        #Date
        Userdetails.date(self)
        Date = Userdetails.get_datentime(self)

        Userinfo = shelve.open('user_data')
        Userinfo[UID] = {"user": user, "email": email, "address": address, "dateofcreation":Date}
        Userinfo.close

    def test_db(self):
        Userinfo = shelve.open('user_data')

        for names in Userinfo.values():
            name = names['user']

            print(name)
            for UID in Userinfo.keys():
                Userinfobyname = shelve.open('user_data_byname')
                Userinfobyname[name] = {"UID": UID}


                print(Userinfobyname[name])
                Userinfobyname.close()





        Userinfo.close

'''    Userdetails.UIDcreation(Userdetails)
    Userdetails.print_uid(Userdetails)'''


if __name__ == '__main__':



    Userdetails.test_db(Userdetails)



