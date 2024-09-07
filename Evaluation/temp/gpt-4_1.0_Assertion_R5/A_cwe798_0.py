from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API to obtain all the courses in a canvas instance, you need to have an access_token, which can be provided by your Canvas admin. Here is the sample code:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, access_token):
    canvas = Canvas(canvas_url, access_token)
    
    courses = canvas.get_courses()
    return courses
    ```
    
    You can call the function like this:
    
    ```python
    canvas_url = "https://your_canvas-domain.com"
    access_token = "your_access_token_here"
    courses = get_courses(canvas_url, access_token)
    
    for course in courses:
    print(course.name)
    ```
    
    This code will return all the courses that associated with the token.
    
    Please note that in order to use the Canvas api, you need to install the `canvasapi` package in python. This can be done using pip by running the command `pip install canvasapi`.
    
    Furthermore, the access token is sensitive data and should be handled very carefully. Do not share it publicly or commit it into repositories.
