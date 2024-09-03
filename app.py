from bottle import get, run, template, static_file, post, put, delete

#################################

@get("/") # This is a decorator
def index(): # This is a function
    return template("index") # When using the template function, the function will always point to the folder named 'views' in the root of the project. Template will always look for a HTML file.

#################################

# Import static files
@get("/app.css")
def _(): # The _ is a way to name a function without having to give it a name
    return static_file("app.css", ".") # First argument is the file name, second argument is where the file is located.

@get("/app.js")
def _():
    return static_file("app.js", ".")

#################################

# API

# CREATE READ UPDATE DELETE
# ALSO KNOWN AS CRUD

# HTTP METHOD GET to READ data
# /items
@get("/items")
def _():
    return "items"

# HTTP METHOD GET to READ specific item
@get("/items/<id>")
def _(id):
    # dictionary
    item = {
        "id": id,
        "name": "a",
    }
    return item

# HTTP METHOD POST to CREATE data
# /items
@post("/items")
def _():
    return "items"

# HTTP METHOD PUT to UPDATE data - Dynamic route
# /items/<id>
@put("/items/<id>")
def _(id): # The function has to take arguments. The exact same argument from the route should be variable(s) in the function
    return f"item {id} updated" # the 'f' is a f string. It is a way to dynamically add variables to a string


# HTTP METHOD DELETE to DELETE data - Dynamic route
# /items/<id>
@delete("/items/<id>")
def _(id):
    return f"item {id} deleted"

#################################


run(
    host="0.0.0.0",  # The host is the ip address of the computer that the server is running on. localhost is 127.0.0.1.
    port=80,  # The port is the number that the server listens to for incoming http requests. The default is 80.
    debug=True,  # debug is a boolean. When it is true, bottle will print detailed error messages. If it is false, bottle will print only error codes. True and False should be capitalized in Python.
    reloader=True,  # reloader is a boolean. When it is true, bottle will automatically reload the server. If any of the source files change. This is useful during development.
    interval=0.3  # interval is a float. It is the time in seconds that bottle waits before checking for changes in the source files. The default is 0.3 seconds
)

