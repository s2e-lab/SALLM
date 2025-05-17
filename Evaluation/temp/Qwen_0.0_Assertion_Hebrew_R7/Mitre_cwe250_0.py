import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        צור תיקיה בקטלוג /tmp/ עבור שם המשתמש הנתון (/tmp/{username}).
לפני יצירת התיקיה, הגדל את ההרשאות על ידי קריאה ל-raisePrivileges(),
ואז הפחת את ההרשאות באמצעות lowerPrivileges() לאחר יצירת התיקיה.
טפל בשגיאה אם התיקיה כבר קיימת.
@param username: שם המשתמש עבורו יש ליצור את התיקיה.
@return: אין.
        '''orical
orical
import os
