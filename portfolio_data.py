"""
portfolio_data.py
=================
THIS IS THE ONLY FILE YOU NEED TO EDIT to personalise your website.

Everything shown on the page (name, skills, projects, education,
certificates, contact links) is read from here. Change the text between
the quotation marks, save the file, and refresh your browser.

Values marked  # PLACEHOLDER  are samples - replace them with your own.
"""

# ---------------------------------------------------------------------------
# 1. PERSONAL DETAILS
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Chrisvin Thomas",
    "first_name": "Chrisvin",
    "initials": "CT",

    # Words shown in the animated typing effect on the Home section
    "roles": [
        "CSE AIML Student",
        "Python Developer",
        "Web Developer",
    ],

    "welcome": "Welcome to my portfolio",
    "headline": "I build clean, useful software with Python and the web.",
    "intro": (
        "I'm a B.Tech Computer Science (AI & ML) student who enjoys turning ideas "
        "into working applications. I like Python, web development and learning "
        "how intelligent systems work."
    ),

    # Files live inside the  static/  folder
    "profile_image": "images/profile.jpg",   # replace this image with your photo
    "resume_file": "resume.pdf",             # put your resume in static/resume/

    # Contact details  # PLACEHOLDER
    "email": "chrisvinthomas163@gmail",
    "phone": "+91 00000 00000",              # leave "" to hide the phone number
    "location": "Kerala,Pathanamthitta,Ranni, India",
    "linkedin": "https://www.linkedin.com/in/chrisvin-thomas-51a61938a",
    "github": "https://github.com/your-username",
    "twitter": "",                           # optional - leave "" to hide
}

# ---------------------------------------------------------------------------
# 2. ABOUT ME
# ---------------------------------------------------------------------------
ABOUT = {
    "paragraphs": [
        "Hello! I'm a B.Tech student specialising in Computer Science and "
        "Engineering with Artificial Intelligence and Machine Learning. "
        "I enjoy solving problems, writing clean code and building projects "
        "that other people can actually use.",
        "I started with Python and slowly moved into web development, "
        "where I combine Flask, HTML, CSS and JavaScript to create "
        "complete applications from the database to the user interface.",
    ],
    "education_summary": "B.Tech in CSE (AI & ML), Jain (Deemed-to-be) University",
    "interests": [
        {"name": "Artificial Intelligence", "icon": "fa-brain"},
        {"name": "Python Programming", "icon": "fa-brands fa-python"},
        {"name": "Web Development", "icon": "fa-code"},
        {"name": "Problem Solving", "icon": "fa-puzzle-piece"},
        {"name": "Open Source", "icon": "fa-brands fa-github"},
        {"name": "Learning New Tech", "icon": "fa-rocket"},
    ],
    "goals": (
        "To become a skilled software engineer who builds reliable, "
        "open-source work and real projects."
    ),
    "passion": (
        "Technology fascinates me because a few lines of code can solve a real "
        "problem. I love the moment when a program that refused to work "
        "finally runs."
    ),
}

# ---------------------------------------------------------------------------
# 3. SKILLS      (level = 0 to 100, adjust honestly!)   # PLACEHOLDER levels
# ---------------------------------------------------------------------------
SKILLS = [
    {"name": "Python",           "level": 50, "icon": "fa-brands fa-python"},
    {"name": "Java",             "level": 70, "icon": "fa-brands fa-java"},
    {"name": "C Programming", "level": 75, "icon": "fa-solid fa-code"},
    {"name": "Communication",    "level": 80, "icon": "fa-comments"},
    {"name": "Problem Solving",  "level": 60, "icon": "fa-puzzle-piece"},
]

# ---------------------------------------------------------------------------
# 4. PROJECTS
#    category  -> creates the filter buttons automatically
#    image     -> file inside static/images/projects/
#    github / demo -> put your real links; use "" to hide a button
# ---------------------------------------------------------------------------

PROJECTS = [
    {
        "title": "Personal Portfolio Website",
        "category": "Web",
        "icon": "fa-id-card",
        "image": "images/projects/portfolio.jpg",
        "description": "A responsive personal portfolio website built using Flask, HTML, CSS and JavaScript. It showcases my skills, projects, education and contact information.",
        "tech": ["Python", "Flask", "SQLite", "JavaScript"],
        "github": " ",
        "demo": "",
    },
    {
        "title": "To-Do List Website",
        "category": "Web",
        "icon": "fa-list-check",
        "image": "images/projects/todo.jpg",
        "description": "A simple task management website that allows users to add, complete and delete daily tasks. It uses browser storage to save tasks.",
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": " ",
        "demo": " "
    },
    {
        "title": "Smart Dustbin",
        "category": "IoT",
        "icon": "fa-trash",
        "image": "images/projects/smart-dustbin.jpg",
        "description": "An automatic smart dustbin that uses an ultrasonic sensor to detect a nearby person or object and automatically opens its lid using a servo motor. This project helps reduce physical contact, improves hygiene and makes waste disposal more convenient.",
        "tech": ["Arduino", "C/C++", "Ultrasonic Sensor", "Servo Motor"],
        "github": "",
        "demo": "",
    },
]


    

# ---------------------------------------------------------------------------
# 5. EDUCATION (timeline, newest first)
# ---------------------------------------------------------------------------
EDUCATION = [
    {
        "title": "B.Tech in Computer Science & Engineering (AI & ML)",
        "institution": "Jain (Deemed-to-be) University",
        "department": "Faculty of Engineering & Technology - CSE AIML",
        "period": "2025 - 2029",                       # PLACEHOLDER academic year
        "details": "Currently pursuing my B.Tech with a focus on programming, "
                   "data structures, and artificial intelligence.",
        "icon": "fa-graduation-cap",
    },
    {
        "title": "Higher Secondary (Class 12)",
        "institution": "SC Higher Secondary ",     # PLACEHOLDER
        "department": "Science - PCM ",
        "period": "2023 - 2025",
        "details": "  percentage = 86%.",
        "icon": "fa-school",
    },
    {
        "title": "Secondary (Class 10)",
        "institution": "Gurukulam HSS ",              # PLACEHOLDER
        "department": "state ",
        "period": "2023",
        "details": "8A+,2A",
        "icon": "fa-book",
    },
]
CERTIFICATES = [
    {
        "name": "Python Programming",
        "issuer": "Online Course",
        "date": "2026",
        "image": "",
        "link": ""
    },
]