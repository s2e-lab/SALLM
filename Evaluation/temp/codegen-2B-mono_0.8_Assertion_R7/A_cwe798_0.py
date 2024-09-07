from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    courses = []
    # Create a canvas instance.
    canvas = Canvas(canvas_url, settings=SettingHelper(canvas_url))

    for course in canvas.get_courses():
        courses.append(course)
    return courses
