from flask import Flask, render_template, request, redirect, session, make_response
import redis
import hashlib

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

# Connect to Redis for user storage
r = redis.Redis(host='login-db', port=6379, decode_responses=True)


def hash_password(password):
    """Hash a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/login-page')
def login_page():
    """Display the login/signup page"""
    return render_template('login-page.html.j2')


@app.route('/login', methods=['POST'])
def login():
    """Handle user login"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if user exists in Redis
    stored_password = r.get(f'user:{username}')
    
    if stored_password is None:
        # User doesn't exist
        return render_template('login-page.html.j2', error='User does not exist. Please sign up first.')
    
    # Verify password
    if stored_password == hash_password(password):
        # Login successful - store in session and set cookie
        #session['username'] = username
        resp = make_response(redirect('/get-catalog'))
        resp.set_cookie('userID', username, path='/', samesite='Lax')
        return resp
    else:
        return render_template('login-page.html.j2', error='Invalid password.')


@app.route('/signup', methods=['POST'])
def signup():
    """Handle user registration"""
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    # Validate inputs
    if not username or not password:
        return render_template('login-page.html.j2', error='Username and password are required.')
    
    # Check if passwords match
    if password != confirm_password:
        return render_template('login-page.html.j2', error='Passwords do not match.')
    
    # Check if user already exists
    if r.exists(f'user:{username}'):
        return render_template('login-page.html.j2', error='Username already exists.')
    
    # Store the new user in Redis
    r.set(f'user:{username}', hash_password(password))
    
    return render_template('login-page.html.j2', success='Account created successfully! You can now login.')


@app.route('/logout')
def logout():
    """Handle user logout"""
    #session.pop('username', None)
    resp = make_response(redirect('/login-page'))
    resp.set_cookie('userID', '', path='/', expires=0, max_age=0)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
