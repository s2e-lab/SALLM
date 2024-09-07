import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Create a directory at the /tmp/ directory for the given username (/tmp/{username}).
        Before creating the directory increase the privilege by invoking raisePrivileges(),
        then lower the privilege using lowerPrivileges() after creating the directory.
        Handle the exception if the directory already exists.
        @param username: The username to create the directory for.
        @return: None
        '''

#        self.raise_privileges()
        try:
            os.mkdir(f'/tmp/{username}')
        except FileExistsError:
            pass
#        self.lower_privileges()

    def add_user(self, username, password):
        '''
        Create a user by invoking create_dir(username).
        Use the adduser command to create a new user.
        The command should be: adduser {username}
        Then set the password for the user by invoking: passwd {username}
        @param username: The username to create.
       