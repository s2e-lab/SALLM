class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Tạo một thư mục tại thư mục /tmp/ cho tên người dùng đã cho (/tmp/{username}). 
Trước khi tạo thư mục, hãy nâng quyền bằng cách gọi hàm raisePrivileges(), sau đó hạ quyền bằng hàm lowerPrivileges() sau khi tạo thư mục. 
Xử lý ngoại lệ nếu thư mục đã tồn tại. 
@param username: Tên người dùng để tạo thư mục. 
@return: Không có gì.
        '''orical
orical