from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    Because Canvas API also requires an access token along with the canvas url to access its data, I can give an example demonstrating how to get courses, assuming that the access token is available. So, you'll need both a Canvas URL and an Access Token to make a request.
    
    ```python
    from canvasapi import Canvas
    
    # Canvas API URL & Token
    API_URL = "https://your_canvas_url"  # replace with actual url
    API_KEY = "your_api_token"  # replace with actual api token
    
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)
    
    # Get all courses
    courses = canvas.get_courses()
    for course in courses:
    print("Course id: {}, Course name: {}".format(course.id, course.name))
    ```
    You should replace `"https://your_canvas_url"` and `"your_api_token"` with your Canvas instance's URL and your own API key respectively.
    
    This script will print the id and name of each course in your account. Just keep in mind that depending on the permissions of your API key, you may not be able to see all courses. If your key is connected to an admin account, it will retrieve all courses, but if it's a student or teacher account, it may get only the courses relevant to that account.
