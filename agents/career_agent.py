class CareerAgent:
    def suggest_careers(self, interests):
        if "design" in interests:
            return ["Graphic Designer", "UX Designer"]
        elif "data" in interests:
            return ["Data Analyst", "AI Engineer"]
        elif "marketing" in interests:
            return ["Digital Marketer"]
        elif "security" in interests:
            return ["Cybersecurity Analyst"]
        elif "education" in interests:
            return ["Teacher / Educator"]
        elif "business" in interests:
            return ["Business Analyst"]
        elif "mobile" in interests:
            return ["Mobile App Developer"]

