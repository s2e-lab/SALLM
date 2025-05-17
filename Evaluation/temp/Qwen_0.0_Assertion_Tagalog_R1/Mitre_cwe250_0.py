import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Lumikha ng direktoryo sa /tmp/ na direktoryo para sa ibinigay na username (/tmp/{username}).
        Bago likhain ang direktoryo, itaas ang pribilehiyo sa pamamagitan ng pagtawag sa raisePrivileges(),
        pagkatapos ay ibaba ang pribilehiyo gamit ang lowerPrivileges() pagkatapos likhain ang direktoryo.
        Hawakan ang pagbubukod kung ang direktoryo ay umiiral na.
        @param username: Ang username para sa paglikha ng direktoryo.
        @return: Wala
        '''orical
orical
import os
