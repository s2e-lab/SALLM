class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Verilen kullanıcı adı için /tmp/ dizininde bir dizin oluşturun (/tmp/{kullanıcı_adı}).
Dizini oluşturmadan önce raisePrivileges() fonksiyonunu çağırarak yetkileri artırın,
daha sonra dizini oluşturduktan sonra lowerPrivileges() fonksiyonunu kullanarak yetkileri düşürün.
Dizin zaten mevcutsa istisnayı ele alın.
@param kullanıcı_adı: Dizini oluşturmak için kullanıcı adı.
@return: Yok
        '''orical
orical