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

# TODO: Handle the already exists case by catching the OSError (and maybe other OS exceptions?)
# TODO: Add exception handling as described in the lecture slides and code written during lab.

    def change_password(self, username):
        '''
        Read the password from the console for the given username from the file. Handle the exception raised.
        If the password is verified change the password using Python standard libraries.
        If the password is not verified print "Access Denied!".
        Handle the exception raised during reading the password from the file.
        @