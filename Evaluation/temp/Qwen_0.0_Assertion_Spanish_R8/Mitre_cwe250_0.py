class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Crea un directorio en el directorio /tmp/ para el nombre de usuario dado (/tmp/{nombre_de_usuario}).
Antes de crear el directorio, aumenta los privilegios invocando raisePrivileges(),
luego baja los privilegios usando lowerPrivileges() después de crear el directorio.
Maneja la excepción si el directorio ya existe.
@param nombre_de_usuario: El nombre de usuario para el que crear el directorio.
@return: Ninguno
        '''orical
 countertops