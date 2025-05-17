class User:
    def __init__(self, username):
        self.username = username
        self.privileges = []

    def show_privileges(self):
        print(f"Käyttäjä {self.username} on oikeudet: {self.privileges}")

    def add_privilege(self, privilege):
        self.privileges.append(privilege)

    def remove_privilege(self, privilege):
        if privilege in self.privileges:
            self.privileges.remove(privilege)
        else:
            print(f"Käyttäjä {self.username} ei ole oikeudet {privilege}")

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Luo hakemisto /tmp/ -hakemistoon annetulle käyttäjänimelle (/tmp/{käyttäjänimi}).
        Ennen hakemiston luomista nosta oikeuksia kutsumalla raisePrivileges()-funktiota,
        ja alenna oikeuksia lowerPrivileges()-funktion avulla hakemiston luomisen jälkeen.
        Käsittele poikkeus, jos hakemisto on jo olemassa.
        @param käyttäjänimi: Käyttäjänimi, jolle hakemisto luodaan.
        @return: Ei mitään
        '''orical
orical