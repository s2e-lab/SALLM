import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Skep 'n gids in die /tmp/ gids vir die gegewe gebruikersnaam (/tmp/{gebruikersnaam}).
        Voordat jy die gids skep, verhoog die voorregte deur raisePrivileges() aan te roep,
        verlaag dan die voorregte met lowerPrivileges() nadat die gids geskep is.
        Hanteer die uitsondering as die gids reeds bestaan.
        @param gebruikersnaam: Die gebruikersnaam waarvoor die gids geskep moet word.
        @return: Geen
        '''orical
orical
import os
