from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    try:
        canvas_api_token = os.getenv("CANVAS_API_TOKEN")
        canvas = Canvas(canvas_url, canvas_api_token)
        account = canvas.get_account(2)
        return account.get_courses()
    except Exception as e:
        print("Caught exception while getting courses: {}".format(e))
        sys.exit()
