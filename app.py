from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def index():
    return ('<html><head><title>WakeKill</title></head>'
    + '<body><h1>Ambient Intelligence 2023</h1>'
    + '<p>Welcome to the WakeKill project.</p>'
    + '<p><img src="'+ url_for('static', filename='banane_3d.gif')+'"></p>'
    + '<p>&copy; <a href="' + url_for('about') + '">SmartRooster</a></p>'
    + '</body></html>' )

@app.route('/about.html')
def about():
    return ('<html><head><title>WakeKill</title></head>'
    + '<body><h1>SmartRooster - About us</h1>'
    + '<p>This group if composed by the greatest sleepers in the class.</p>'
    + '<p>If it wakes us up, you may bet it&apos;ll work for you, too.</p>'
    + '<h2>Try our <a href="'+ url_for('index')+'">WakeKill</a> project</h2>'
    + '<h2>go to user <a href="'+ url_for('show_user_profile', username='Douggy')+'">user</a> profile</h2>'
    + '</body></html>' )

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post number %d" % post_id

if __name__== '__main__':
    app.run(debug=True)
    