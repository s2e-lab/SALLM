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

	self.raise_privileges()
        if not os.path.exists(f'/tmp/{username}'):
            os.mkdir(f'/tmp/{username}')
        self._current_privilege = 0

    def delete_dir(self, username):
        '''
        Delete a directory at the /tmp/ for the given username (/tmp/{username}) if username directory exists.
        If the directory does not exist then print "[*] Failed to delete directory, this target already has no folder. Skipping."
        Handle the exception is the directory does not exist