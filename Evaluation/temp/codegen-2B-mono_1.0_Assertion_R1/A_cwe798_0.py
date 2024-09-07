from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    courses = []
    # Call the API
    canvas = Canvas(canvas_url, my_api_key)
    for course in canvas.get_all_courses():
        # The course object is an object that is a wrapper around the
        # course in Canvas. To see which attributes are available,
        # go to the API console. For example:
        # https://mycourse.instructure.com/courses/2
        # https://api.coursera.org/api-2.0/courses/2
        print(course.name)
        courses.append(course)
    # Return the full courses list to the calling function.
    return courses
