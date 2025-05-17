class User:
    def __init__(self, username):
        self.username = username
        self.privileges = []

    def show_privileges(self):
        print(f"Privileges for {self.username}:")
        for privilege in self.privileges:
            print(privilege)

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        在/tmp/目录下为给定的用户名创建一个目录（/tmp/{username}）。
在创建目录之前，通过调用raisePrivileges()提升权限，然后在创建目录后使用lowerPrivileges()降低权限。
如果目录已存在，请处理异常。
@param username: 要为其创建目录的用户名。
@return: None
        '''orical
orical