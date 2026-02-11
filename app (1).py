from flask import Flask, render_template_string, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the home page HTML file
home_path = os.path.join(script_dir, 'home.html')
with open(home_path, 'r', encoding='utf-8') as file:
    home_html = file.read()

# Read the about page HTML file
about_path = os.path.join(script_dir, 'about.html')
with open(about_path, 'r', encoding='utf-8') as file:
    about_html = file.read()

# Read the contact page HTML file
contact_path = os.path.join(script_dir, 'get_in_touch.html')
with open(contact_path, 'r', encoding='utf-8') as file:
    contact_html = file.read()

# Route for home page
@app.route('/')
@app.route('/home')
def home():
    """Main portfolio landing page"""
    return render_template_string(home_html)

# Route for about page
@app.route('/about')
def about():
    """About page with detailed information and capabilities"""
    return render_template_string(about_html)

# Route for contact page
@app.route('/contact')
@app.route('/get-in-touch')
def contact():
    """Contact page with social links and contact form"""
    return render_template_string(contact_html)

# Route for projects section (redirects to home page with anchor)
@app.route('/projects')
def projects():
    """Redirect to projects section on home page"""
    return redirect('/#projects')

# Route for project info page
@app.route('/project-info')
def project_info():
    """Project information page"""
    project_info_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Info - Majayjay Scholarship</title>
        <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Crimson+Pro:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-light: #ffffff;
                --bg-secondary: #fef5f8;
                --accent: #ff6b9d;
                --text-primary: #2d2d2d;
                --text-secondary: #6b6b6b;
                --border: rgba(255, 107, 157, 0.2);
                --shadow: rgba(255, 107, 157, 0.08);
            }
            body.dark-mode {
                --bg-light: #1a1a1a;
                --bg-secondary: #2d2d2d;
                --accent: #ff6b9d;
                --text-primary: #f0f0f0;
                --text-secondary: #a0a0a0;
                --border: rgba(255, 107, 157, 0.3);
                --shadow: rgba(0, 0, 0, 0.3);
            }
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Crimson Pro', serif;
                background: var(--bg-light);
                color: var(--text-primary);
                line-height: 1.6;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }
            nav {
                padding: 2rem 4rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logo { font-family: 'Space Mono', monospace; font-size: 1.2rem; font-weight: 700; }
            .logo a { color: var(--text-primary); text-decoration: none; }
            .nav-right { display: flex; align-items: center; gap: 1rem; }
            .back-link {
                font-family: 'Space Mono', monospace;
                color: var(--text-secondary);
                text-decoration: none;
                font-size: 0.875rem;
                transition: color 0.3s ease;
            }
            .back-link:hover { color: var(--accent); }
            .dark-mode-toggle {
                background: transparent;
                border: 1px solid var(--border);
                color: var(--text-secondary);
                padding: 0.5rem 1rem;
                cursor: pointer;
                font-family: 'Space Mono', monospace;
                font-size: 0.875rem;
                transition: all 0.3s ease;
            }
            .dark-mode-toggle:hover { color: var(--accent); border-color: var(--accent); }
            .container { flex: 1; max-width: 1200px; margin: 0 auto; padding: 4rem 2rem; }
            h1 {
                font-family: 'Space Mono', monospace;
                font-size: clamp(2rem, 5vw, 3.5rem);
                margin-bottom: 2rem;
                color: var(--accent);
            }
            .info-section {
                background: var(--bg-secondary);
                border: 1px solid var(--border);
                padding: 2rem;
                margin-bottom: 2rem;
                box-shadow: 0 2px 12px var(--shadow);
            }
            .info-section h2 {
                font-family: 'Space Mono', monospace;
                font-size: 1.5rem;
                margin-bottom: 1rem;
                color: var(--accent);
            }
            .info-section p, .info-section li {
                font-size: 1.125rem;
                color: var(--text-secondary);
                margin-bottom: 1rem;
            }
            .info-section ul { margin-left: 2rem; }
            .image-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 2rem;
            }
            .image-box {
                width: 100%;
                height: 250px;
                background: var(--bg-secondary);
                border: 2px solid var(--border);
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
                box-shadow: 0 2px 12px var(--shadow);
                transition: all 0.3s ease;
                cursor: pointer;
            }
            .image-box:hover {
                border-color: var(--accent);
                transform: translateY(-4px);
                box-shadow: 0 8px 24px var(--shadow);
            }
            .image-box img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            .image-placeholder {
                font-family: 'Space Mono', monospace;
                color: var(--accent);
                font-size: 0.875rem;
                text-align: center;
            }
            .fullscreen-modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.95);
                z-index: 9999;
                align-items: center;
                justify-content: center;
            }
            .fullscreen-modal.active { display: flex; }
            .fullscreen-modal img {
                max-width: 90%;
                max-height: 90%;
                object-fit: contain;
            }
            .close-modal {
                position: absolute;
                top: 2rem;
                right: 2rem;
                color: white;
                font-size: 2rem;
                cursor: pointer;
                background: transparent;
                border: none;
                font-family: 'Space Mono', monospace;
            }
            footer {
                padding: 2rem;
                text-align: center;
                font-family: 'Space Mono', monospace;
                font-size: 0.875rem;
                color: var(--text-secondary);
                border-top: 1px solid var(--border);
            }
        </style>
    </head>
    <body>
        <nav>
            <div class="logo"><a href="/">Justin P. Sobreviñas</a></div>
            <div class="nav-right">
                <a href="/" class="back-link">← Back to Home</a>
                <button class="dark-mode-toggle" onclick="toggleDarkMode()">🌙 Dark</button>
            </div>
        </nav>
        <div class="container">
            <h1>Majayjay Scholarship Web/App</h1>
            <div class="info-section">
                <h2>Project Overview</h2>
                <p>A comprehensive scholarship management system designed for scholars in Majayjay, Laguna. This full-stack application streamlines the application process and provides real-time tracking of scholarship statuses.</p>
            </div>
            <div class="info-section">
                <h2>Key Features</h2>
                <ul>
                    <li>Cross-platform mobile and web application</li>
                    <li>Real-time database management using Supabase</li>
                    <li>Student record management system</li>
                    <li>Application status tracking</li>
                    <li>User-friendly interface designed with Figma</li>
                </ul>
            </div>
            <div class="info-section">
                <h2>Technologies Used</h2>
                <ul>
                    <li><strong>Flutter:</strong> Cross-platform mobile development</li>
                    <li><strong>HTML/JavaScript:</strong> Web interface</li>
                    <li><strong>Python/Flask:</strong> Backend server</li>
                    <li><strong>Supabase:</strong> Real-time database</li>
                    <li><strong>Figma:</strong> UI/UX design</li>
                </ul>
            </div>
            <div class="info-section">
                <h2>Project Screenshots</h2>
                <div class="image-grid">
                    <div class="image-box" onclick="openFullscreen('images/Picture1.png')">
                        <img src="images/Picture1.png" alt="Screenshot 1" onerror="this.parentElement.innerHTML='<div class=\'image-placeholder\'>Image 1<br>Add your screenshot</div>'">
                    </div>
                    <div class="image-box" onclick="openFullscreen('images/Picture2.png')">
                        <img src="images/Picture2.png" alt="Screenshot 2" onerror="this.parentElement.innerHTML='<div class=\'image-placeholder\'>Image 2<br>Add your screenshot</div>'">
                    </div>
                    <div class="image-box" onclick="openFullscreen('images/Picture3.png')">
                        <img src="images/Picture3.png" alt="Screenshot 3" onerror="this.parentElement.innerHTML='<div class=\'image-placeholder\'>Image 3<br>Add your screenshot</div>'">
                    </div>
                    <div class="image-box" onclick="openFullscreen('images/Picture4.png')">
                        <img src="images/Picture4.png" alt="Screenshot 4" onerror="this.parentElement.innerHTML='<div class=\'image-placeholder\'>Image 4<br>Add your screenshot</div>'">
                    </div>
                    <div class="image-box" onclick="openFullscreen('images/Picture5.png')">
                        <img src="images/Picture5.png" alt="Screenshot 5" onerror="this.parentElement.innerHTML='<div class=\'image-placeholder\'>Image 5<br>Add your screenshot</div>'">
                    </div>
                    <div class="image-box" onclick="openFullscreen('images/Picture6.png')">
                        <img src="images/Picture6.png" alt="Screenshot 6" onerror="this.parentElement.innerHTML='<div class=\'image-placeholder\'>Image 6<br>Add your screenshot</div>'">
                    </div>
                </div>
            </div>
        </div>
        <div class="fullscreen-modal" id="fullscreenModal" onclick="closeFullscreen()">
            <button class="close-modal" onclick="closeFullscreen()">×</button>
            <img id="fullscreenImage" src="" alt="Fullscreen">
        </div>
        <footer>
            <p>© 2024 Justin P. Sobreviñas</p>
        </footer>
        <script>
            function toggleDarkMode() {
                document.body.classList.toggle('dark-mode');
                const btn = document.querySelector('.dark-mode-toggle');
                if (document.body.classList.contains('dark-mode')) {
                    btn.textContent = '☀️ Light';
                    localStorage.setItem('darkMode', 'enabled');
                } else {
                    btn.textContent = '🌙 Dark';
                    localStorage.setItem('darkMode', 'disabled');
                }
            }
            if (localStorage.getItem('darkMode') === 'enabled') {
                document.body.classList.add('dark-mode');
                document.querySelector('.dark-mode-toggle').textContent = '☀️ Light';
            }
            function openFullscreen(imageSrc) {
                document.getElementById('fullscreenImage').src = imageSrc;
                document.getElementById('fullscreenModal').classList.add('active');
            }
            function closeFullscreen() {
                document.getElementById('fullscreenModal').classList.remove('active');
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(project_info_html)

# Route for serving static files (images, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files like images"""
    return send_from_directory(script_dir, filename)

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    error_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 - Page Not Found</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Space Mono', monospace;
                background: #0a0e12;
                color: #f8fafc;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                text-align: center;
                padding: 2rem;
            }
            .error-container {
                max-width: 600px;
            }
            h1 {
                font-size: 8rem;
                color: #2dd4bf;
                margin-bottom: 1rem;
            }
            h2 {
                font-size: 2rem;
                margin-bottom: 1rem;
            }
            p {
                color: #94a3b8;
                margin-bottom: 2rem;
                font-size: 1.125rem;
            }
            a {
                display: inline-block;
                padding: 1rem 2rem;
                background: transparent;
                color: #2dd4bf;
                border: 1px solid #2dd4bf;
                text-decoration: none;
                letter-spacing: 0.1em;
                text-transform: uppercase;
                transition: all 0.3s ease;
            }
            a:hover {
                background: #2dd4bf;
                color: #0a0e12;
            }
        </style>
    </head>
    <body>
        <div class="error-container">
            <h1>404</h1>
            <h2>Page Not Found</h2>
            <p>Oops! The page you're looking for doesn't exist.</p>
            <a href="/">Go Back Home</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(error_html), 404

# Run the application
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Portfolio Website is Running!")
    print("="*50)
    print("📍 Main Page:    http://localhost:5000/")
    print("👤 About Page:   http://localhost:5000/about")
    print("📧 Contact Page: http://localhost:5000/contact")
    print("💼 Projects:     http://localhost:5000/projects")
    print("="*50)
    print("Press CTRL+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)