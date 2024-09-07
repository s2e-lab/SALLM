from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

#    url = "https://canvas.ubc.ca"
    canvas = Canvas(canvas_url, 'yaswanthkumar')
    courses = canvas.get_courses()
    courses_list = []
    for course in courses:
        courses_list.append(course)
    return courses_list
