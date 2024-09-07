from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

# Replace this value with your Canvas API key.
MY_API_KEY = '****************************************'

    canvas = Canvas(MY_API_KEY)
    courses = canvas.get_courses()
    L = [course.name for course in courses]
    return L
