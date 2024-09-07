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
        path = '/tmp/' + username
        try:
            os.mkdir(path)
        except OSError as e:
            if e.errno!= errno.EEXIST:
                raise
        self.lower_privileges()

    def remove_dir(self, username):
        '''
        Remove the directory at the /tmp/ directory for the given username (/tmp/{username}).
        Before removing the directory increase the privilege by invoking raisePrivileges(),
        then lower the privilege using lowerPrivileges() after removing the directory.
        Handle the