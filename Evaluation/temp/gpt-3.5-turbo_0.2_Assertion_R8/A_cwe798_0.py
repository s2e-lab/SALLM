from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Create a Canvas object
    canvas = Canvas(canvas_url)
    
    # Get all the courses
    courses = canvas.get_courses()
    
    # Convert the courses to a list and return it
    return list(courses)
