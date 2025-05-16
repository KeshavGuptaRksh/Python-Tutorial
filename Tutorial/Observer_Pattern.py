'''Behavioral Patterns: Focus on communication between objects

Observer, Strategy, Command, Iterator, State'''

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer: Subject's state changed to {subject.state}")

subject = ConcreteSubject("Initial")
observer = ConcreteObserver()
subject.attach(observer)
subject.state = "New State"  # Observer: Subject's state changed to New State