from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Initialize the Canvas API object
    canvas = Canvas(canvas_url)
    
    # Get a list of all the courses on the Canvas instance
    courses = canvas.get_courses()
    
    # Create a list to store the course objects
    course_list = []
    
    # Iterate through the courses and add them to the course list
    for course in courses:
        course_list.append(course)
    
    return course_list
