from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''


# Initialize a new Canvas object
canvas = Canvas(canvas_url, 'yourschool.instructure.com')

# Get the list of all courses
courses = canvas.get_courses()

# Print the name of each course
for course in courses:
    print(course.name)
