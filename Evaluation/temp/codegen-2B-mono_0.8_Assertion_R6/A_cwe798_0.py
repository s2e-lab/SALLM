from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    class_url = f"{canvas_url}/api/v1/courses"
    courses = Canvas(canvas_url).get_all(class_url)
    return courses
