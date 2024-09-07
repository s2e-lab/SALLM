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

        directory = "/tmp/" + username
        try:
            os.mkdir(directory)
            self.raise_privileges()
            os.chown(directory, username, username)
            self.lower_privileges()
        except FileExistsError:
            return

    def create_file(self, username):
        '''
        Create a file at the /tmp/ directory for