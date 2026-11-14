# My Portfolio - Flask Personal Portfolio Website

A futuristic dark-navy and blue single-page portfolio built with **Python, Flask, HTML5, CSS3, JavaScript and SQLite**.
Visitors can read about you, browse your projects, download your resume and send you a message that is saved in a database.

---

## 1. Project folder structure

```
MyPortfolio/
├── app.py                  <- Flask backend (routes, database, form validation)
├── portfolio_data.py       <- YOUR details: edit this file to personalise the site
├── requirements.txt        <- Python packages needed (Flask)
├── view_messages.py        <- prints messages saved by the contact form
├── database.db             <- created automatically the first time you run app.py
├── README.md               <- this guide
├── templates/
│   ├── index.html          <- the whole single-page website
│   └── 404.html            <- "page not found" page
└── static/
    ├── css/
    │   └── style.css       <- design, colours, animations, responsive layout
    ├── js/
    │   └── script.js       <- typing effect, theme toggle, filters, form, etc.
    ├── images/
    │   ├── profile.jpg     <- your profile picture (replace it)
    │   ├── projects/       <- one image per project
    │   └── certificates/   <- optional certificate images
    └── resume/
        └── resume.pdf      <- your resume (replace it)
```

## 2. What each file does

| File | Purpose |
|------|---------|
| `app.py` | The Python program. Starts Flask, creates the SQLite table, shows the website, validates and saves contact messages, serves the resume download. |
| `portfolio_data.py` | Holds all your personal content (name, skills, projects, education, certificates, links). **The only file you normally edit.** |
| `requirements.txt` | Lists the packages to install with `pip`. |
| `view_messages.py` | Small helper that prints every message stored in `database.db`. |
| `templates/index.html` | The page structure (HTML). It reads the data from `portfolio_data.py` and builds every section. |
| `templates/404.html` | Friendly error page. |
| `static/css/style.css` | All styling: dark and light themes, glow effects, cards, animations, mobile layout. |
| `static/js/script.js` | All interactivity: loader, theme toggle, menu, typing effect, scroll animations, skill bars, project filter, back-to-top, contact form. |

## 3. Install Python

1. Go to <https://www.python.org/downloads/> and download the latest Python 3.
2. Run the installer. **On Windows, tick "Add python.exe to PATH"** on the first screen, then click *Install Now*.
3. Open a terminal (Command Prompt / PowerShell on Windows, Terminal on Mac) and check:
   ```
   python --version
   ```
   (On Mac/Linux you may need `python3 --version`.) You should see a version number.

## 4. Install VS Code and set up the project

1. Install VS Code from <https://code.visualstudio.com/>.
2. In VS Code, open the **Extensions** panel (`Ctrl+Shift+X`) and install **Python** (by Microsoft).
3. Put the `MyPortfolio` folder somewhere easy, e.g. `Documents`.
4. In VS Code: **File -> Open Folder...** and choose `MyPortfolio`.
5. Open the terminal inside VS Code: **Terminal -> New Terminal**.

## 5. Install Flask

In the VS Code terminal (you should be inside the `MyPortfolio` folder):

```
pip install -r requirements.txt
```

(or simply `pip install flask`).

*Recommended - use a virtual environment so packages stay inside the project:*

```
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac / Linux
pip install -r requirements.txt
```

If VS Code asks which interpreter to use, pick the one inside `venv`.

## 6. Run the website

```
python app.py
```

You will see something like:

```
 * Running on http://127.0.0.1:5000
```

## 7. Open it in the browser

Open **<http://127.0.0.1:5000>** (or <http://localhost:5000>) in Chrome/Edge/Firefox.
Press `Ctrl+C` in the terminal to stop the server.
While it is running, saving a file in VS Code reloads the site automatically; just refresh the browser.

> The page loads its fonts and icons from the internet (Google Fonts and Font Awesome), so connect to Wi-Fi when you demonstrate it.

## 8. Add your profile picture

1. Pick a square-ish photo of yourself (about 600 x 600 px works well).
2. Rename it to `profile.jpg`.
3. Copy it into `static/images/` and **replace** the existing `profile.jpg`.
4. Refresh the browser (`Ctrl+F5`).

Using a `.png` instead? Change `"profile_image": "images/profile.jpg"` to `"images/profile.png"` in `portfolio_data.py`.

## 9. Update your personal details

Open **`portfolio_data.py`** and change the text between the quotes. Then save and refresh.

- `PROFILE`: name, typing-effect roles, email, phone, location, LinkedIn, GitHub.
  Set `"phone": ""` if you do not want to show your phone number.
- `ABOUT`: your introduction, interests, career goals and passion.
- `SKILLS`: change `"level"` (0-100) to honestly match your ability.
- `EDUCATION`: academic years and previous schools (currently `20XX - 20XX` placeholders).

Do not change the names on the left of the colons (like `"name":`), only the values on the right.

## 10. Add your resume

Save your resume as a PDF named `resume.pdf` in `static/resume/` (replace the sample file). The **Download Resume** button will now download yours.

## 11. Add a new project

1. Put a project screenshot (about 800 x 450 px) in `static/images/projects/`, e.g. `chat-app.jpg`.
2. In `portfolio_data.py`, add a new block inside the `PROJECTS = [ ... ]` list (remember the comma after the previous block):

```python
    {
        "title": "Chat Application",
        "category": "Python",                    # a new category adds a new filter button automatically
        "icon": "fa-comments",                   # any icon name from https://fontawesome.com/icons
        "image": "images/projects/chat-app.jpg",
        "description": "A real-time chat app built with Flask.",
        "tech": ["Python", "Flask", "SQLite"],
        "github": "https://github.com/your-username/chat-app",
        "demo": "",                              # "" hides the Live Demo button
    },
```

Replace the sample `your-username` GitHub links of the existing projects with your real repositories.

## 12. Add a certificate or achievement

Inside `CERTIFICATES = [ ... ]` add or edit a block:

```python
    {
        "title": "Python for Everybody",
        "issuer": "Coursera",
        "date": "March 2026",
        "type": "Certificate",          # Certificate, Workshop, Hackathon or Achievement
        "icon": "fa-brands fa-python",
        "link": "https://link-to-your-certificate",   # "" hides the View link
        "sample": False,                # False removes the "Sample" badge
    },
```

The cards that came with the site are **samples** (they show a "Sample" badge). Replace them with certificates you have really earned and delete the ones you do not have. Never list achievements that are not yours.

## 13. See the messages from the contact form

Every message is saved in `database.db`. To read them, open a second terminal (the website can keep running) and run:

```
python view_messages.py
```

You can also open `database.db` with the VS Code extension **SQLite Viewer**, or with DB Browser for SQLite.

## 14. Common errors and fixes

| Problem | Fix |
|---------|-----|
| `'python' is not recognized` | Python is not on PATH. Reinstall it and tick **Add python.exe to PATH**, or try `py app.py`. |
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install flask`. If you use a virtual environment, activate it first. |
| `pip` is not recognized | Use `python -m pip install flask`. |
| `Address already in use` / port 5000 busy | Close the other program or change the last line of `app.py` to `app.run(debug=True, port=5001)` and open `http://127.0.0.1:5001`. |
| `TemplateNotFound: index.html` | The `templates` folder must be in the same folder as `app.py`, spelled exactly `templates`. |
| CSS/JS not loading, plain white page | The folder must be named `static` (with `css/style.css` and `js/script.js` inside). Refresh with `Ctrl+F5`. |
| Icons or fonts missing | You are offline. Connect to the internet. |
| Profile photo not changing | Same file name and folder? Refresh with `Ctrl+F5` to clear the browser cache. |
| Resume button shows "Page not found" | `static/resume/resume.pdf` is missing, or `"resume_file"` in `portfolio_data.py` has a different name. |
| `SyntaxError` in `portfolio_data.py` | Usually a missing comma, quote or bracket in what you edited. Check the line mentioned in the error. |
| `IndentationError` | Keep the original spacing (4 spaces) and do not mix tabs and spaces. |
| Contact form says "Could not reach the server" | The Flask server is not running. Start it again with `python app.py`. |
| Changes not showing | Save the file (`Ctrl+S`) and refresh with `Ctrl+F5`. |

## 15. Technologies used

Python 3, Flask, SQLite (`sqlite3` module), HTML5, CSS3 (variables, grid, flexbox, animations), JavaScript (ES5, `IntersectionObserver`, `fetch`, Canvas).

## 16. Submitting it as an assignment

- Make sure you replaced the placeholders with your own details and removed the "Sample" certificates you did not earn.
- Zip the project (leave out the `venv` folder) or upload it to GitHub.
- Be ready to explain: how Flask routes work (`@app.route`), how data flows from `portfolio_data.py` into `index.html`, and how the contact form is validated and saved with SQL.
