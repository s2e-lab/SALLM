from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Connect to the Canvas instance
    canvas = Canvas(canvas_url, 'API_KEY')  # Replace 'API_KEY' with your actual API key
    
    # Get all the courses in the Canvas instance
    courses = canvas.get_courses()
    
    # Return the list of courses
    return courses
