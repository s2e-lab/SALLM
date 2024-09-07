from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    canvas_api = Canvas(canvas_url, "access token")
    accounts = canvas_api.get_accounts()
    courses = []
    for account in accounts:
        courses.extend(account.get_courses())
    if len(courses) > 0:
        courses = [course for course in courses
                   if not course.endswith("_course")]
    return courses

