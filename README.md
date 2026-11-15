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

 routes work (`@app.route`), how data flows from `portfolio_data.py` into `index.html`, and how the contact form is validated and saved with SQL.
