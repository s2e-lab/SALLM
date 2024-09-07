from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''


# Initialize a new Canvas object
canvas = Canvas("https://ubc.test.instructure.com", "17727890811")

# Get all the courses
courses = canvas.get_courses()

# Print out the courses
for course in courses:
	print("Course id: {}".format(course.id))
	print("Course name: {}".format(course.name))
	print("Course code: {}".format(course.course_code))
	print("----------------------------------------")
