from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Use API to get all courses in a canvas instance
    api_url = f'{canvas_url}/api/v1/courses'
    # Instantiate a new Canvas object and grab the courses
    c = Canvas(canvas_url, 'access_token')
    courses = c.get_courses()

    # For each course, print the course name and id
    for course in courses:
        print(f"Course id: {course.id}, Course name: {course.name}")

    return courses
