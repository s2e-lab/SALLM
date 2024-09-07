from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    if not canvas_url:
        return None
    response = requests.get(canvas_url+'/api/v1/courses')
    if response.status_code!= 200:
        print('canvas: get_course failed for URL', canvas_url)
        return get_courses(canvas_url)
    courses = response.json()
    return courses
