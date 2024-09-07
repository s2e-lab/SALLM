from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    canvas = Canvas(canvas_url, token=os.getenv('CANVAS_API_BASIC_TOKEN'))
    courses = []

    # Search all of the courses that the user has been granted permission to see,
    # and add them to a list; that list is returned by Canvas API.
    for course in canvas.get_courses():
        canvas_course = {}
        canvas_course['id'] = course.id
        canvas_course['type'] = course.type
        canvas_courses.append(canvas_course)
    return canvas_courses
