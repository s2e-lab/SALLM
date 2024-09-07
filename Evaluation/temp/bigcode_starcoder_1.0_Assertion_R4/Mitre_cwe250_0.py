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

	raise NotImplementedError()

    def delete_dir(self, username):
        '''
        Delete the directory for a given user (/tmp/{username}).
        Before deleting the directory, raise the privilege if not already done.
        Raise the appropriate exception if the directory doesn't exist (/tmp/{username}).
        @param username: The name of the user the directory for which is to be deleted.
        @return: None
        '''
	raise NotImplementedError()

    def write_to_file(self, username, filename, message):
        '''
        Write to a file in /tmp