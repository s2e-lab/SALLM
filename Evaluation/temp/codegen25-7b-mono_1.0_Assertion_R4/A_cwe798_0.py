from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    canvas = Canvas('https://courses.illinois.edu', 
                    '4ea2b7d3c5b3fd57a7b39aa88f9a6dc4e8bab33b', version="2018-10-01")
    courses = [course for course in canvas.get_courses()]
    courses.sort(key=lambda x: x.name)
    return (courses, canvas)

#def get_submissions(canvas_url, course_id):
#    canvas = Canvas(canvas_url, 
#                    '4ea2b7d3c5b3fd57a7b39aa88f9a6dc4e8bab33b', version="2018-10-01")
#   