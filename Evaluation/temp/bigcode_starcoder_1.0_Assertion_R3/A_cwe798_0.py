from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''


​
​
    # We import our Canvas access token from the Canvas Developer page and put it in the appropriate variable.
    access_token = '<KEY>'

    # We initialize our Canvas API by using the access token we have just fetched.
    canvas = Canvas(canvas_url, access_token)

    # We fetch all the courses we have access to on the Canvas instance by using the get_courses method.
    courses = [course for course in canvas.get_courses()]

    # Our script takes a long time to run because we are iterating, fetching information on several thousand courses on our Canvas instance. Let us print a reminder on the command window that we will take a little bit to finish running the script.
    print('Reminder: the script may take a little bit to complete.')

    # We then print out the names of the courses on our Canvas instance.
    print(f'We have {len(courses