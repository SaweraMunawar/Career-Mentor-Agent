def get_career_roadmap(career):
    roadmap = {
        "Software Developer": ["Learn Python", "Data Structures", "Git & GitHub"],
        "AI Engineer": ["Python", "ML Algorithms", "TensorFlow/PyTorch"],
        "Graphic Designer": [
            "Understand Design Principles",
            "Adobe Photoshop / Illustrator",
            "Figma / Canva",
            "UI/UX Basics",
            "Portfolio Projects"
        ],
        "UX Designer": [
            "User Research Techniques",
            "Wireframing (Figma, Adobe XD)",
            "Design Thinking Process",
            "Prototyping Tools",
            "Usability Testing"
        ],
        "Data Analyst": [
            "Excel & Data Cleaning",
            "SQL Queries",
            "Data Visualization (Tableau, Power BI)",
            "Python for Data Analysis (Pandas, Matplotlib)",
            "Statistics Basics"
        ],
        "Digital Marketer": [
            "SEO & SEM Fundamentals",
            "Social Media Marketing",
            "Google Analytics / Ads",
            "Email Marketing Tools (Mailchimp)",
            "Content Marketing Strategies"
        ],
        "Cybersecurity Analyst": [
            "Computer Networks Basics",
            "Linux & Command Line",
            "Ethical Hacking Tools (Kali Linux)",
            "Security Protocols",
            "Certifications (e.g., CEH, CompTIA Security+)"
        ],
        "Teacher / Educator": [
            "Subject Expertise",
            "Presentation & Communication",
            "Digital Teaching Tools (Zoom, Google Classroom)",
            "Lesson Planning",
            "Assessment & Feedback Techniques"
        ],
        "Business Analyst": [
            "Business Fundamentals",
            "Data Analysis with Excel",
            "Requirement Gathering",
            "UML Diagrams / Use Cases",
            "Stakeholder Communication"
        ],
        "Mobile App Developer": [
            "Learn Dart or Kotlin",
            "Frameworks (Flutter / Android Studio)",
            "Mobile UI/UX Design",
            "APIs & JSON",
            "Publish to App Stores"
        ]
    }
    return roadmap.get(career, ["No roadmap available"])
