from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

# Fill this in
    canvas = Canvas(canvas_url, 'access token') # Get auth_token either in env or here
    courses = canvas.get_courses()
    return courses
