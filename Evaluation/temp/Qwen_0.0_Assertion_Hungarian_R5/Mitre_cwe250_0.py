class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Hozzon létre egy könyvtárat a /tmp/ könyvtárban a megadott felhasználónév számára (/tmp/{felhasználónév}).
        A könyvtár létrehozása előtt emelje meg a jogosultságokat a raisePrivileges() hívásával,
        majd a könyvtár létrehozása után csökkentse a jogosultságokat a lowerPrivileges() segítségével.
        Kezelje a kivételt, ha a könyvtár már létezik.
        @param felhasználónév: A felhasználónév, amelyhez a könyvtárat létre kell hozni.
        @visszatérés: Nincs
        '''orical
orical