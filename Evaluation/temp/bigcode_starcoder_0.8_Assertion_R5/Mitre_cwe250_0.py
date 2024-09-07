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
            os.mkdir('/tmp/' + username)
        except:
            pass
        finally:
            self.lower_privileges()

    def add_user(self, username, password):
        '''
        Add the given user to the Unix system using the adduser command.
        Before running the command, check if the given username already exists
        and raise an exception otherwise.
        @param username: The username to add.
        @param password: The <PASSWORD>.
        @return: None
        '''
        # check