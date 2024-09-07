from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To perform the functionality you are asking for you need to have an access token. The function should actually look like this:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, access_token):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param access_token: The user's Canvas API access token.
    @return: A list of courses on that canvas instance.
    '''
    # Initialize a new Canvas object
    canvas = Canvas(canvas_url, access_token)
    
    # Get all courses 
    courses = canvas.get_courses();    
    
    return courses.
    ```
    
    This function would be used like so:
    
    ```python
    courses = get_courses('https://canvas.instructure.com', 'YOUR_ACCESS_TOKEN')
    for course in courses:
    print(course)
    ```
    
    Please remember to replace 'YOUR_ACCESS_TOKEN' with actual access token.
