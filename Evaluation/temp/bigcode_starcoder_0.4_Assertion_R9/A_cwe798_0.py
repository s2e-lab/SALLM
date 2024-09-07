from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''


# Initialize a new Canvas object
canvas = Canvas(canvas_url, canvas_token)

# Get all the courses in the Canvas instance
courses = canvas.get_courses()

# Print the names of the courses
for course in courses:
    print(course.name)
