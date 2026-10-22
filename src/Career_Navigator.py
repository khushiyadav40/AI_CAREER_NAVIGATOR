CAREERS = {
    "Data Scientist": {
        "skills": ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization"],
        "path": ["Python", "Pandas", "Statistics", "SQL", "Machine Learning", "Projects"],
        "internships": ["Data Science Intern", "ML Intern"]
    },
    "Machine Learning Engineer": {
        "skills": ["Python", "SQL", "Statistics", "Machine Learning", "Deep Learning"],
        "path": ["Python", "Statistics", "ML", "Deep Learning", "Model Deployment"],
        "internships": ["ML Intern", "AI Intern"]
    },
    "Software Developer": {
        "skills": ["Python", "Java", "SQL", "Data Structures", "Web Development"],
        "path": ["Programming", "Data Structures", "SQL", "Web Development", "Projects"],
        "internships": ["Software Developer Intern", "Web Developer Intern"]
    },
    "Data Analyst": {
        "skills": ["Python", "SQL", "Statistics", "Data Visualization", "Excel"],
        "path": ["Excel", "SQL", "Statistics", "Pandas", "Power BI", "Projects"],
        "internships": ["Data Analyst Intern", "Business Analyst Intern"]
    },
    "Cybersecurity Analyst": {
        "skills": ["Python", "Networking", "Linux", "Cybersecurity", "SQL"],
        "path": ["Networking", "Linux", "Python", "Security Fundamentals", "Projects"],
        "internships": ["Cybersecurity Intern", "Security Analyst Intern"]
    }
}

TRAINING_DATA = [
    (["Python", "SQL", "Statistics", "Machine Learning"], "Data Scientist"),
    (["Python", "SQL", "Statistics", "Machine Learning"], "Data Scientist"),
    (["Python", "Statistics", "Machine Learning", "Deep Learning"], "Machine Learning Engineer"),
    (["Python", "Statistics", "Machine Learning", "Deep Learning"], "Machine Learning Engineer"),
    (["Python", "Java", "SQL", "Data Structures"], "Software Developer"),
    (["Python", "Java", "SQL", "Data Structures"], "Software Developer"),
    (["Python", "SQL", "Excel", "Data Visualization"], "Data Analyst"),
    (["Python", "SQL", "Excel", "Data Visualization"], "Data Analyst"),
    (["Python", "Linux", "Networking", "Cybersecurity"], "Cybersecurity Analyst"),
    (["Python", "Linux", "Networking", "Cybersecurity"], "Cybersecurity Analyst")
]

ALL_SKILLS = sorted({
    skill for career in CAREERS.values()
    for skill in career["skills"]
})


def skill_gap(career, student_skills):
    required = CAREERS[career]["skills"]
    student = {s.casefold() for s in student_skills}
    return (
        [s for s in required if s.casefold() in student],
        [s for s in required if s.casefold() not in student]
    )
