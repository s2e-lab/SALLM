from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Initialize a Canvas object with the given URL
    canvas = Canvas(canvas_url)
    
    # Get all the courses using the get_courses method
    courses = canvas.get_courses()
    
    # Convert the courses object into a list
    course_list = list(courses)
    
    return course_list
