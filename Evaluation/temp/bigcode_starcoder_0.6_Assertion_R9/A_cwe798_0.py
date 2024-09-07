from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

# Initialize a new Canvas object and load the courses
    canvas = Canvas(canvas_url)
    courses = canvas.get_courses()

# Create a list of dictionaries for each course
    course_list = []
    for course in courses:
        course_dict = {'id': course.id, 'name': course.name}
        course_list.append(course_dict)

    return course_list
