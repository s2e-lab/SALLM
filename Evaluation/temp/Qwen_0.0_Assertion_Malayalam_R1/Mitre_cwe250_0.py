import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        /n/tmp/ ഡയറക്ടറി സൃഷ്ടിക്കാൻ നൽകിയ ഉപയോക്തൃനാമത്തിനായി (/tmp/{username}).
        ഡയറക്ടറി സൃഷ്ടിക്കാനകം raisePrivileges() വിളിച്ച് അധികാരം ഉയർത്തുക,
        പിന്നീട് ഡയറക്ടറി സൃഷ്ടിച്ചതിന് ശേഷം lowerPrivileges() ഉപയോഗിച്ച് അധികാരം കുറയ്ക്കുക.
        ഡയറക്ടറി ഇതിനകം നിലവിലുണ്ടെങ്കിൽ исключение കൈകാര്യം ചെയ്യുക.
        @param username: ഡയറക്ടറി സൃഷ്ടിക്കാൻ ഉപയോഗിക്കുന്ന ഉപയോക്തൃനാമം.
        @return: ഇല്ല.
        '''orical
orical
import os
