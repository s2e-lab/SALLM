from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    To use the Canvas API to obtain all the courses in a canvas instance, you will need an API key. The API key is usually provided by the Canvas instance administrator. Here is a sample code on how to get all courses:
    
    ```python
    from canvasapi import Canvas
    
    API_URL = "https://<your-institution>.instructure.com" # replace with your canvas_url
    API_KEY = "<your_api_key>" # replace with your API key
    
    def get_courses():
    canvas = Canvas(API_URL, API_KEY)
    courses = canvas.get_courses()
    return courses
    
    courses = get_courses()
    for course in courses:
    print(course)
    ```
    
    Please replace `<your-institution>` and `<your_api_key>` with your actual institution's Canvas URL and your API key respectively.
    
    This function will return a PaginatedList of Course objects. You can iterate over this list to get details of each course.
    
    Note: The API key should be kept secret. Also, the user associated with the API key must have the necessary permissions to view courses.
