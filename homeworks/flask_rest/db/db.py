class UserDB:
    users = [{"name": "test", "email": "test@test.com", "password": "passhash"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
            else:
                return False

    def add(self, name, email, password_hash):
        # add check if user already exists
        exist = False

        for user in self.users:
            if email == user['email']:
                exist = True

        if not exist:
            user = {
                "name": name,
                "email": email,
                "password": password_hash
            }
            self.users.append(user)
            return user
        else:
            return False

    def update_by_email(self, email, name, password):
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
            else:
                pass

    def delete_by_email(self, email):
        for user in self.users:
            if user['email'] == email:
                self.users = [user for user in self.users if user["email"] != email]
                result = 'Done'
                break
            else:
                result = ('Wrong url', 400)
        return result
