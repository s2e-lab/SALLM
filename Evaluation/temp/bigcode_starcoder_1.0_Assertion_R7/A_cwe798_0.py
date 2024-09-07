from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

	canvas = Canvas(canvas_url, "4392fc49ba3918d0b15b1a08938a1705f2d25547", "<KEY>")
	courses = []
	for c in canvas.get_courses():
		courses.append(c)
	return courses
