from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

#    API_URL ='https://canvas.uw.edu'
    API_URL = canvas_url
    COURSES_API_URL = API_URL + '/api/v1/courses'
    canvas = Canvas(API_URL)
    courses = canvas.get_courses()
    course_list = []
    for course in courses:
        course_list.append(course)
    return course_list

