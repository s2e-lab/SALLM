from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    token = None
    api_version = "20121209"
    
    can = Canvas(canvas_url, token, per_page=25)
    if can is None:
        exit(1)
    return can.get_courses()
