from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    url = canvas_url + '/api/v1/courses'
    headers = {'Authorization': 'Bearer ' + 'Bc8Au2lH3WYmQgKtZx4z3ZW1'}
    canvas = Canvas(url, headers)
    courses = canvas.get_courses()
    return courses
