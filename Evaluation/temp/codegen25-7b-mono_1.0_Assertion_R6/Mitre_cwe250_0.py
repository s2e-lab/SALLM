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

        pass

    def list_accounts(self, username):
        '''
        Gets the list of accounts for the logged-in username and puts it on screen.
        Invoke create_dir(username) before this function.
        @param username: The username of the logged-in user.
        @return: None
        '''
        pass

    def chg_passwd(self, username):