from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API to get a list of courses, you'll need an API key. This key is typically provided by your institution or you can generate an API token within your account settings on Canvas. Here's an example of how it can be done:
    
    ```python
    from canvasapi import Canvas
    
    def get_courses(canvas_url, api_key):
    '''
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @param api_key: The API key is a unique identifier of an application requesting access to your service.
    @return: A list of courses on that canvas instance.
    '''
    canvas = Canvas(canvas_url, api_key)
    courses = canvas.get_courses()
    return [course for course in courses]
    ```
    
    You can call this function like so:
    
    ```python
    courses = get_courses('https://<your-institution>.instructure.com', '<your-api-key>')
    for course in courses:
    print(course)
    ``` 
    
    Replace `<your-institution>` with your institution's Canvas URL and `<your-api-key>` with your personal API key.
    
    Please note that you need to have the necessary permissions to access course information in your instance of Canvas.
    
    This function will return a list of Course objects. Each Course object contains various attributes like the course's ID, name, account ID, start date, end date, and so on.
