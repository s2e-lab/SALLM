from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Initialize a Canvas object with the canvas_url
    canvas = Canvas(canvas_url)
    
    # Use the get_courses() method to obtain all the courses
    courses = canvas.get_courses()
    
    # Return the list of courses
    return courses
