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

#        try:
        # Raise the privilege to root
        #os.setuid(0)
        # Make the directory
        os.mkdir('/tmp/' + username)

        # Lower the privilege back to the unprivileged user
#        os.setuid(pwd.getpwnam(username).pw_uid)
#        except FileExistsError as e:
#            pass
#        except PermissionError as e:
#            pass

    def remove_dir(self, username):
        '''
        Remove the directory at /tmp/{username