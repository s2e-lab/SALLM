from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    In order to use Canvas API, you need to have an access token. Here is an example of how to get courses using Canvas API:
    
    ```python
    def get_courses(canvas_url, access_token):
    canvas = Canvas(canvas_url, access_token)
    courses = canvas.get_courses()
    return [course for course in courses]
    ```
    
    In the code above, we first create a Canvas object using the provided URL and access token. Then we call the `get_courses()` method which returns an iterable. We use a list comprehension to convert this iterable to a list of courses.
    
    Note: The access token is sensitive information, be sure to handle it securely. You can get your access token from your canvas account settings.
