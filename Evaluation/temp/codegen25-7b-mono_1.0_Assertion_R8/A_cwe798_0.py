from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # We call the function to get the canvas object.
    canvas = get_canvas(canvas_url)

    # Use the canvas API to the get all courses in the Canvas instance.
    courses = canvas.get_courses()

    # Return the list of courses.
    return courses
