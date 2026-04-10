"""
Flask Hello World Application
A simple web application using Flask framework to demonstrate basic routing and templating
"""

from flask import Flask, render_template, request
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Application configuration
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


@app.route('/')
def hello():
    """
    Home route - displays hello message with current time
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', time=current_time)


@app.route('/about')
def about():
    """
    About route - displays information about the application
    """
    app_info = {
        'name': 'Flask Hello World',
        'version': '1.0.0',
        'description': 'A simple Flask web application for beginners',
        'created': '2024'
    }
    return render_template('about.html', app_info=app_info)


@app.route('/user/<name>')
def user(name):
    """
    User route - personalized greeting based on name parameter
    """
    return render_template('user.html', name=name.capitalize())


@app.route('/api/hello', methods=['GET', 'POST'])
def api_hello():
    """
    API route - returns JSON response
    """
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name', 'Guest')
        message = f"Hello, {name}! 👋"
    else:
        message = "Hello, World! 👋"
    
    return {
        'status': 'success',
        'message': message,
        'timestamp': datetime.now().isoformat()
    }


@app.route('/form', methods=['GET', 'POST'])
def contact_form():
    """
    Contact form route - demonstrates form handling
    """
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        email = request.form.get('email', 'not@provided.com')
        message = request.form.get('message', '')
        
        # In production, you would save this to database
        print(f"Form submitted: {name}, {email}, {message}")
        
        return render_template('success.html', 
                             name=name, 
                             email=email)
    
    return render_template('contact.html')


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    return render_template('500.html'), 500


@app.context_processor
def inject_globals():
    """
    Inject global variables available to all templates
    """
    return {
        'app_name': 'Flask Hello World',
        'current_year': datetime.now().year
    }


if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Flask Hello World Application")
    print("=" * 50)
    print("\n📝 Routes available:")
    print("  • GET  /              - Home page")
    print("  • GET  /about         - About page")
    print("  • GET  /user/<name>   - Personalized greeting")
    print("  • GET  /form          - Contact form (display)")
    print("  • POST /form          - Contact form (submit)")
    print("  • GET  /api/hello     - JSON API")
    print("  • POST /api/hello     - JSON API with data")
    print("\n🌐 Server running at: http://127.0.0.1:5000")
    print("💡 Press CTRL+C to quit")
    print("🔄 Debug mode: ON (Auto-reload on file changes)")
    print("=" * 50 + "\n")
    
    # Run the application
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=True
    )