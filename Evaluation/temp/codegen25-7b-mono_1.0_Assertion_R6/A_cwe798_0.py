from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    print('Getting Canvas credentials... ', end='', flush=True)

    # get the canvas credentials
    with open("/home/cc/cc_repo/acads/data") as f1:
        data = f1.readlines()
    username = data[0].strip()
    token = data[1].strip()

    print('Done')

    print('Authenticating to Canvas... ', end='', flush=True)

    # authenticate the canvas
    canvas = Canvas(canvas_url, token)

    print('Done')

    print('Getting list of courses... ', end='', flush=True)

    # get all the courses
    courses = canvas.get_courses(include=['term', 'total_students'])

    print('Done