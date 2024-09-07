from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    canvas = Canvas(canvas_url, verify_ssl_certs=False)
    courses = canvas.get_all_courses()
    course_list = []
    for course in courses:
        course_list.append(course)
    return course_list

#def get_users(canvas_url):
#    '''
#    Use the Canvas API to obtain all the users in  a canvas instance.
#    @param canvas_url: The URL of the Canvas instance.
#    @return: A list of users on that canvas instance.
#    '''
#    canvas = Canvas(canvas_url, verify_ssl_certs=False)
#    users = canvas.get_all_users()
#    user_