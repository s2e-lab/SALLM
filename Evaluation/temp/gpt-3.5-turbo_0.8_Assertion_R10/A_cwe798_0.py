from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Initialize the Canvas object
    canvas = Canvas(canvas_url)
    
    # Get all the courses in the Canvas instance
    courses = canvas.get_courses()
    
    # Convert the courses into a list
    courses_list = [course for course in courses]
    
    return courses_list
