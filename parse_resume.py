import json

resume_text = """
SUMMARY
Aspiring software engineer passionate about coding and problem-solving. Eager to contribute fresh ideas and learn from experienced professionals. Proficient in C++, Java, Python. Ready to tackle exciting challenges and grow in a dynamic environment.

TECHNICAL SKILLS
Programming languages: C++, Java
Web Technologies: HTML, CSS
Data Management: MySQL

CERTIFICATIONS
• Basic Java, Code Tantra - Sep’23
• Computer Architecture and Computer Organization, Udemy - Apr’23
• Introduction to Hardware and Operating System, Coursera - May’23
• Theory of Computation, Udemy - Nov’23
• Cloud Essentials, edX - Nov’23

EXTRA CURRICULAR ACTIVITIES
• Engaged participant in Untangle Organization | an event organizing club - May’23

PROJECTS
Cat-dog Classification Project - Oct’23
Domain: Artificial Intelligence | Programming language: Python
• Objective: Develop an AI/ML model to accurately classify images as either "cat" or "dog" based on visual features, aiming for high precision and recall
• Details: Data preparation, model selection and training, evaluation and validation
• Outcomes: Optimizing for high accuracy and generalization, and integrating the model into a user-friendly application for seamless image classification.

Temperature Converter using GUI - Aug’22
Domain: Web Application | Programming language: Java
• Objective: Develop a Java-based GUI application for converting temperatures between Celsius and Fahrenheit, providing a user-friendly interface.
• Details: GUI Design and Implementation, Temperature Conversion Logic, User Experience Enhancement
• Outcome: Develop a Java GUI temperature converter, ensuring user-friendly design, accurate conversion logic, and additional features for an enhanced, intuitive, and efficient experience.

SUMMER TRAINING Jun’22-Jul’23
Basics of Java – Code Tantra
• Gained knowledge in areas like arrays, loops, operators and object-oriented programming
• After completion of every topic problems are solved in order to apply the concept
• Developed a web application called ‘Temperature Converter’
• Well-versed in finding & debugging the errors in code. Detected and tracked software bugs and inconsistencies in the program
• Made a report on the project and performed presentation on the project

ACHIEVEMENTS
3-star rating in C++ on HackerRank Jan’21-Sep '22

EDUCATION
BTech in Computer Science Mar’21-Present
Lovely Professional University | Phagwara
CGPA 6.53

Intermediate Jul’18- Mar’20
Sri Chaitanya Junior College | VSKP | AP
CGPA 9.07

Secondary Education Jun’17-May’18
Sri Chaitanya School | VSKP | AP
CGPA 9.7
"""

def parse_resume(resume_text):
    resume_json = {
        "summary": "Aspiring software engineer passionate about coding and problem-solving. Eager to contribute fresh ideas and learn from experienced professionals. Proficient in C++, Java, Python. Ready to tackle exciting challenges and grow in a dynamic environment.",
        "technical_skills": {
            "programming_languages": ["C++", "Java"],
            "web_technologies": ["HTML", "CSS"],
            "data_management": ["MySQL"]
        },
        "certifications": [
            {"title": "Basic Java", "issuer": "Code Tantra", "date": "Sep’23"},
            {"title": "Computer Architecture and Computer Organization", "issuer": "Udemy", "date": "Apr’23"},
            {"title": "Introduction to Hardware and Operating System", "issuer": "Coursera", "date": "May’23"},
            {"title": "Theory of Computation", "issuer": "Udemy", "date": "Nov’23"},
            {"title": "Cloud Essentials", "issuer": "edX", "date": "Nov’23"}
        ],
        "extra_curricular_activities": [
            {"activity": "Engaged participant in Untangle Organization | an event organizing club", "date": "May’23"}
        ],
        "projects": [
            {
                "title": "Cat-dog Classification Project",
                "date": "Oct’23",
                "domain": "Artificial Intelligence",
                "programming_language": "Python",
                "objective": "Develop an AI/ML model to accurately classify images as either 'cat' or 'dog' based on visual features, aiming for high precision and recall",
                "details": ["Data preparation", "Model selection and training", "Evaluation and validation"],
                "outcomes": "Optimizing for high accuracy and generalization, and integrating the model into a user-friendly application for seamless image classification."
            },
            {
                "title": "Temperature Converter using GUI",
                "date": "Aug’22",
                "domain": "Web Application",
                "programming_language": "Java",
                "objective": "Develop a Java-based GUI application for converting temperatures between Celsius and Fahrenheit, providing a user-friendly interface.",
                "details": ["GUI Design and Implementation", "Temperature Conversion Logic", "User Experience Enhancement"],
                "outcomes": "Develop a Java GUI temperature converter, ensuring user-friendly design, accurate conversion logic, and additional features for an enhanced, intuitive, and efficient experience."
            }
        ],
        "summer_training": {
            "title": "Basics of Java – Code Tantra",
            "date": "Jun’22-Jul’23",
            "details": [
                "Gained knowledge in areas like arrays, loops, operators and object-oriented programming",
                "After completion of every topic problems are solved in order to apply the concept",
                "Developed a web application called ‘Temperature Converter’",
                "Well-versed in finding & debugging the errors in code. Detected and tracked software bugs and inconsistencies in the program",
                "Made a report on the project and performed presentation on the project"
            ]
        },
        "achievements": [
            {"title": "3-star rating in C++ on HackerRank", "date": "Jan’21-Sep '22"}
        ],
        "education": [
            {
                "degree": "BTech in Computer Science",
                "institution": "Lovely Professional University",
                "location": "Phagwara",
                "date": "Mar’21-Present",
                "cgpa": 6.53
            },
            {
                "degree": "Intermediate",
                "institution": "Sri Chaitanya Junior College",
                "location": "VSKP, AP",
                "date": "Jul’18- Mar’20",
                "cgpa": 9.07
            },
            {
                "degree": "Secondary Education",
                "institution": "Sri Chaitanya School",
                "location": "VSKP, AP",
                "date": "Jun’17-May’18",
                "cgpa": 9.7
            }
        ]
    }
    return json.dumps(resume_json, indent=4)

print(parse_resume(resume_text))
