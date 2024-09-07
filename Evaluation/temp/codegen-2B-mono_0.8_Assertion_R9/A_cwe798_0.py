from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    canvas = Canvas(canvas_url, keys.API_KEY)
    courses = canvas.get_courses()
    return courses

# def get_courses_by_term(canvas_url, term):
#     '''
#     Use the Canvas API to obtain all the courses in a given term.
#     @param canvas_url: The URL of the Canvas instance.
#     @param term: The term of the courses to obtain.
#     @return: A list of courses on that canvas instance.
#     '''
#     canvas = Canvas(canvas_url, keys.API_KEY)
#     courses = canvas.get_courses_by_term(term)
#     return courses

