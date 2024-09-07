from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # get a canvas instance
    canvas = Canvas(canvas_url, token=get_token(canvas_url))

    # create a list to hold all of the courses
    courses = []

    # get all of the courses
    all_courses = canvas.get_courses()
    
    # for each course
    for course in all_courses:
        # add the course to the list
        courses.append(course)

    # return the list of courses
    return courses
