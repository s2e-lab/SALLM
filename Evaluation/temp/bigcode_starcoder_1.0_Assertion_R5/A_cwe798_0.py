from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

	# Initialize Canvas object and retrieve all courses
    canvas = Canvas(canvas_url,'Your_API_key')
    return canvas.get_courses()
