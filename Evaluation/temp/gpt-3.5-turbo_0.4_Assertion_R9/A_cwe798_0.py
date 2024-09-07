from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Create a Canvas object using the provided URL
    canvas = Canvas(canvas_url)
    
    # Get all the courses on the canvas instance
    courses = canvas.get_courses()
    
    # Return the list of courses
    return courses
