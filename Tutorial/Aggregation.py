class Professor:
    def __init__(self, name):
        self.name = name
    
    def teach(self):
        print(f"{self.name} is teaching")

class Department:
    def __init__(self, name, professors=None):
        self.name = name
        self.professors = professors if professors else []  # Aggregation
    
    def add_professor(self, professor):
        self.professors.append(professor)
    
    def list_professors(self):
        print(f"Professors in {self.name}:")
        for prof in self.professors:
            print(f"- {prof.name}")

# Usage
prof1 = Professor("Dr. Smith")
prof2 = Professor("Dr. Johnson")

cs_dept = Department("Computer Science")
cs_dept.add_professor(prof1)
cs_dept.add_professor(prof2)

cs_dept.list_professors()
# Professors exist independently of the department