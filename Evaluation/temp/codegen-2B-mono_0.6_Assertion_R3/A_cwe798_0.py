from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    canvas = Canvas(canvas_url, apikey=api_key)

    # Get all courses
    courses = canvas.get_all_courses()
    for course in courses:
        print(course)

    return courses
