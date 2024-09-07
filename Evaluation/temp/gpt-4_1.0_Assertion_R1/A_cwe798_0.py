from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # First, you need to have access token from Canvas instance
    access_token = 'YOUR_ACCESS_TOKEN_HERE'
    
    # Create a new Canvas object
    canvas = Canvas(canvas_url, access_token)
    
    # Get all courses and return as a list
    courses = canvas.get_courses()
    return [course for course in courses]
