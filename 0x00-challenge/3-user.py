import hashlib
import uuid

class User():
    _hashed_password = None

    def __init__(self):
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        return self._hashed_password

    @password.setter
    def password(self, pwd):
        if pwd is None or not isinstance(pwd, str):
            self._hashed_password = None
        else:
            self._hashed_password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        if pwd is None or not isinstance(pwd, str):
            return False
        if self._hashed_password is None:
            return False
        return hashlib.sha256(pwd.encode()).hexdigest().lower() == self._hashed_password

if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    assert user_1.id is not None, "New User should have an id"

    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password != u_pwd, "User.password should be hashed"

    assert user_2.password is None, "User.password should be None by default"

    user_2.password = None
    assert user_2.password is None, "User.password should be None if set to None"

    user_2.password = 89
    assert user_2.password is None, "User.password should be None if set to an integer"

    assert user_1.is_valid_password(u_pwd), "is_valid_password should return True if it's the right password"
    assert not user_1.is_valid_password("Fakepwd"), "is_valid_password should return False if it's not the right password"
    assert not user_1.is_valid_password(None), "is_valid_password should return False if compared with None"
    assert not user_1.is_valid_password(89), "is_valid_password should return False if compared with an integer"
    assert not user_2.is_valid_password("No pwd"), "is_valid_password should return False if no password set before"

    print("All tests passed successfully.")
