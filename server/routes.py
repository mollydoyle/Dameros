from server import app
from flask import render_template, jsonify, request
from server import database
from server import db_setup
import binascii

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/apply')
def apply_func():
    return render_template("apply.html")

@app.route('/success_stories')
def success_stories_func():
    return render_template("success_stories.html")

@app.route('/admin')
def admin_func():
    return render_template("admin.html")

@app.route('/destroy_old_form_entries')
def destroy_old_form_entries():
    result = db_setup.drop_form_entries()
    return result

@app.route('/tilt_a_roll')
def tilt_a_roll_func():
    return render_template("play.html")

@app.route('/text_content', methods=['PUT'])
def text_content():
    ## TODO: Carefully check authentication (of Lauren) via session variables
    ### How to grab id and value that were just changed (error handle them): 
    ## id, value = request.json["id"], request.json["value"])
    ## TODO: Database update operation with these values that changes website content
    return jsonify({'success': 'yes'})

@app.route('/image_content', methods=['POST'])
def image_content():
    ## TODO: Carefully check authentication (of Lauren) via session variables
    ### How to grab image file that was just changed (error handle / make sure it has some content):
    id = list(dict(request.files).keys())[0] ## ex. 'success-stories-image-1'. Id representing image file to change.
    binary_image_data = request.files[id].read() ## ex. <FileStorage: 'fullsizeoutput_1f3.jpeg' ('image/jpeg')>. Contents of uploaded file.
    base_64_image_data = binascii.b2a_base64(image_data)
    ## TODO: use github api ?? To upload this new file ??   https://developer.github.com/v3/repos/contents/#create-or-update-a-file ??
    ## The GitHub API only accepts base-64 encoding for file content, so that's the reason for base_64_image_data. 
    ## TODO: git add, commit, push
    return jsonify({'success': 'yes'})

@app.route('/test')
def test_func():
    return database.test()