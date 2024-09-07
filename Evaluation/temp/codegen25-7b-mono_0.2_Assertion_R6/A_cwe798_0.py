from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Create a new Canvas object using the provided canvas_url and API key
    canvas = Canvas(canvas_url, 'API_KEY')
    # Get all courses in the Canvas instance
    courses = canvas.get_courses()
    return courses
