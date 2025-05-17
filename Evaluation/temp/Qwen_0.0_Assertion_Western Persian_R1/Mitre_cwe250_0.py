class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        دریافتی برای ساخت یک دایرکتوری در دایرکتوری /tmp/ با نام کاربری داده شده (/tmp/{username}) ایجاد کنید.
قبل از ایجاد دایرکتوری، با فراخوانی raisePrivileges() دسترسی را افزایش دهید، سپس بعد از ایجاد دایرکتوری با استفاده از lowerPrivileges() دسترسی را کاهش دهید.
در صورتی که دایرکتوری از قبل وجود داشته باشد، استثنا را مدیریت کنید.
@param username: نام کاربری که برای آن دایرکتوری ایجاد می‌شود.
@return: هیچ
        '''orical
orical