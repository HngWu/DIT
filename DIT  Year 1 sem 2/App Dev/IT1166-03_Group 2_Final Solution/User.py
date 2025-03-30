import shelve


class User:
    def __init__(self, user_id, name, email, subject, remarks):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__subject = subject
        self.__remarks = remarks

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_remarks(self):
        return self.__remarks

    def set_remarks(self, remarks):
        self.__remarks = remarks

    @classmethod
    def load_users_dict(cls):
        try:
            return shelve.open("user.db", "c")["Users"]
        except KeyError:
            return {}

    @classmethod
    def save_users_dict(cls, users_dict):
        db = shelve.open("user.db", "c")
        db["Users"] = users_dict
        db.close()

    @classmethod
    def create_user(cls, user_id, name, email, subject, remarks):
        users_dict = cls.load_users_dict()

        user = cls(user_id, name, email, subject, remarks)

        users_dict[user.get_user_id()] = user
        cls.save_users_dict(users_dict)

        return user

    @classmethod
    def update_user(cls, user_id, name, email, subject, remarks):
        users_dict = cls.load_users_dict()
        user = users_dict.get(user_id)

        if user:
            user.set_name(name)
            user.set_email(email)
            user.set_subject(subject)
            user.set_remarks(remarks)

            cls.save_users_dict(users_dict)

            return user

    @classmethod
    def delete_user(cls, user_id):
        users_dict = cls.load_users_dict()
        users_dict.pop(user_id, None)
        cls.save_users_dict(users_dict)
