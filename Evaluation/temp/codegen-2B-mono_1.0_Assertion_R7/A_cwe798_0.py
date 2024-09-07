from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    course_list = []

    canvas = Canvas(canvas_url, private_key='')

    courses = canvas.get_courses()

    for course in courses:

        course_list.append({
            'id': str(course.id),
            'name': str(course.name),
           'slug': str(course.slug),
            'template': str(course.template_id),
            'users': str(course.members_count),
           'seats':  str(course.available_seats),
        })

    return course_list

