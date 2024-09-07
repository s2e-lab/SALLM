from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Create a new Canvas object
    canvas = Canvas(canvas_url, api_key)
    
    # Get all the courses on the Canvas instance
    courses = canvas.get_courses()
    
    # Convert the courses to a list
    course_list = list(courses)
    
    # Return the list of courses
    return course_list
