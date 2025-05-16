class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def fly(self):
        return "Sorry, I can't fly but I swim well!"

class Parrot(Bird):
    pass  # Inherits fly() from Bird

def bird_flying_test(bird):
    print(bird.fly())

# Using polymorphism
birds = [Bird(), Penguin(), Parrot()]

for bird in birds:
    bird_flying_test(bird)
    
# Output:
# I can fly!
# Sorry, I can't fly but I swim well!
# I can fly!