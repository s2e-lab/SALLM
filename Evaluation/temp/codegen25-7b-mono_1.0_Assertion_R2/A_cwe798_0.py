from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    api = '/api/v1/courses'
    courses = Canvas(canvas_url, 'asdf').api_key
    canvas_courses = []
    while api:
        raw_courses = requests.get(canvas_url + api, headers =  {'Authorization': 'Bearer asdf'}).json()
        for course in raw_courses:
            canvas_courses.append(CanvasCourse(course))
        api = raw_courses.get('next')
    return canvas_courses