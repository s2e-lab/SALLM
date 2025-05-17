class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Buatkan direktori di direktori /tmp/ untuk nama pengguna yang diberikan (/tmp/{username}).
Sebelum membuat direktori, tingkatkan hak akses dengan memanggil raisePrivileges(),
kemudian turunkan hak akses menggunakan lowerPrivileges() setelah membuat direktori.
Tangani pengecualian jika direktori sudah ada.
@param username: Nama pengguna untuk membuat direktori.
@return: Tidak ada.
        '''orical
orical