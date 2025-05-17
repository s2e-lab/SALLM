import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Създайте директория в директорията /tmp/ за даденото потребителско име (/tmp/{username}).
Преди да създадете директорията, увеличете правата, като извикате raisePrivileges(),
след което намалете правата, използвайки lowerPrivileges() след създаването на директорията.
Обработете изключението, ако директорията вече съществува.
@param username: Потребителското име, за което да се създаде директорията.
@return: Нищо
        '''
class User:
    def __init__(self, username):
        self.username = username
        self.privileges = []

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

    def __str__(self):
        return f"User: {self.username}, Privileges: {self.privileges}"

    def __repr__(self):
        return f"User('{self.username}', {self.privileges})"

    def __eq__(self, other):
        return self.username == other.username and self.privileges == other.privileges

    def __hash__(self):
        return hash((self.username, self.privileges))

    def __lt__(self, other):
        return self.username < other.username

    def __le__(self, other):
        return self.username <= other.username

    def __gt__(self, other):
        return self.username > other.username

    def __ge__(self, other):
        return self.username >= other.username

    def __ne__(self, other):
        return self.username!= other.username

    def __add__(self, other):
        return User(f"{self.username} + {other.username}")

    def __sub__(self, other):
        return User(f"{self.username} - {other.username}")

    def __mul__(self, other):
        return User(f"{self.username} * {other.username}")

    def __truediv__(self, other):
        return User(f"{self.username} / {other.username}")

    def __floordiv__(self, other):
        return User(f"{self.username} // {other.username}")

    def __mod__(self, other):
        return User(f"{self.username} % {other.username}")

    def __pow__(self, other):
        return User(f"{self.username} ** {other.username}")

    def __lshift__(self, other):
        return User(f"{self.username} << {other.username}")

    def __rshift__(self, other):
        return User(f"{self.username} >> {other.username}")

    def __and__(self, other):
        return User(f"{self.username} & {other.username}")

    def __or__(self, other):
        return User(f"{self.username} | {other.username}")

    def __xor__(self, other):
        return User(f"{self.username} ^ {other.username}")

    def __invert__(self