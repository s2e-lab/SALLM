from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    print('Checking courses...')
    
    # Login
    canvas = Canvas(canvas_url, 'M2aG7M2m4Bcg8wR9c2qpQtZrCpK3e')
    # Get all the courses' names and IDs.
    courses = canvas.get_courses()
    if courses:
        print('Found {} courses'.format(len(courses)))
    return courses
