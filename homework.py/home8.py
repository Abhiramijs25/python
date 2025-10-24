class Employee:
    def __init__(self, *, name, role, **kwargs):
       
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")


class Trainer(Employee):
    def __init__(self, *, specialization, **kwargs):
      
        self.specialization = specialization
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Specialization: {self.specialization}")


class YogaInstructor(Employee):
    def __init__(self, *, yoga_style, **kwargs):
       
        self.yoga_style = yoga_style
        super().__init__(**kwargs)

    def display(self):
        super().display()
        print(f"Yoga Style: {self.yoga_style}")


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, *, name, role, specialization, yoga_style):

        super().__init__(name=name, role=role,
                         specialization=specialization,
                         yoga_style=yoga_style)

    def display(self):
       
        super().display()
        print(f"Yoga Style: {self.yoga_style}")


emp = Employee(name="John", role="Receptionist")
trainer = Trainer(name="Alice", role="Gym Trainer", specialization="Strength Training")
yoga_instructor = YogaInstructor(name="Priya", role="Yoga Instructor", yoga_style="Hatha Yoga")
multi_trainer = MultiTrainer(name="David", role="Multi Trainer", specialization="Cardio", yoga_style="Ashtanga Yoga")


print("Employee Details:")
emp.display()
print("\nTrainer Details:")
trainer.display()
print("\nYoga Instructor Details:")
yoga_instructor.display()
print("\nMulti-Trainer Details:")
multi_trainer.display()
