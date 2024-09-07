from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    In order to use the Canvas API, you need to have an access token. This token is a secret key that allows you to access the API. Once you have this token, you can use it to authenticate with the API and make requests to it.
    
    Here's an example of how you might get all the courses from a Canvas instance:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, token):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param token: The access token for the Canvas API.
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, token)
    
    courses = []
    for course in canvas.get_courses():
        courses.append(course)
    
    return courses
    ```
    
    You would then call this function like this:
    
    ```python
    courses = get_courses('https://canvas.yourschool.edu', 'your_access_token')
    for course in courses:
    print(course.name)
    ```
    
    This will print the names of all the courses in your Canvas instance.
    
    Please note that this is just an example. The actual implementation may depend on your specific needs and the specific configuration of your Canvas instance. Also, be sure to keep your access token secure and do not share it with anyone.
