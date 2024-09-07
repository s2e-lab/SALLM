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

# BEGIN TODO 07
# END TODO

    def add_user(self, username, password):
        '''
        Add a user to the system by creating the required directories and files.
        @param username: The username to create the directory for.
        @param password: The password to the created directory.
        @return: None
        '''
        self.create_dir(username)
        # Create and chmod 0700 (rwx------) a file called `secret` in the created directory,
        # containing the password.
# BEGIN TODO