from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    api_url = canvas_url + '/api/v1'
    token = 'YOUR_API_TOKEN'
    canvas = Canvas(api_url, token)
    
    courses = canvas.get_courses()
    
    return courses
