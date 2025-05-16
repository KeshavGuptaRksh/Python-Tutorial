# Composition example for a computer system
class CPU:
    def process(self):
        print("Processing data")

class Memory:
    def store(self, data):
        print(f"Storing {data}")

class HardDrive:
    def read(self):
        return "Some data from disk"

class Computer:
    def __init__(self):
        self.cpu = CPU()          # Composition
        self.memory = Memory()    # Composition
        self.hard_drive = HardDrive()  # Composition
    
    def start(self):
        data = self.hard_drive.read()
        self.memory.store(data)
        self.cpu.process()

# Aggregation example for a university
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []  # Aggregation
    
    def enroll(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.title}")

# Usage
comp_sci = Course("Computer Science 101")
alice = Student("Alice")
bob = Student("Bob")

comp_sci.enroll(alice)
comp_sci.enroll(bob)