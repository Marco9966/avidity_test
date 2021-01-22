from flask import Flask, render_template, request
from assets import getCharsInfo, getRandonComic

app = Flask(__name__)   # Calls the Flask class to the app variable

@app.route('/', methods=['GET', 'POST'])    # Defines the index route and methods
def index():                                # Defines the index itself

    character = request.form.get('character')   # Requests the info from the 'character' form

    if character != None:                       # Verifies if there's something in the form
        comic_info = getRandonComic(character)
        if comic_info == None:                  # Verifies if the input got from the form match with some Marvel character, else, returns None
            chars_info = None
        else:                                   # If matches, return the information of all characters that appears on the comic
            chars_info = getCharsInfo(comic_info['characters']['items'])
    else:                                       # If there's nothing in the form, returns None
        comic_info = None
        chars_info = None

    return render_template('index.html', comic_info = comic_info, chars_info = chars_info)  # Renders the HTML itself when the index '/' route is acessed

app.run(debug=True) # Runs the app