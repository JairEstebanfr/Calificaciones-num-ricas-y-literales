class GradeEvaluator:
    def __init__(self, numeric_grade):
        self.numeric_grade = numeric_grade
        self.literal_grade = None
        self.evaluation = None

    def evaluate_grade(self):
        if self.numeric_grade > 9.0:
            self.literal_grade = 'A'
            self.evaluation = 'Excelente'
        elif self.numeric_grade > 8.0:
            self.literal_grade = 'B'
            self.evaluation = 'Muy bien'
        elif self.numeric_grade >= 7.5:
            self.literal_grade = 'C'
            self.evaluation = 'Bien'
        else:
            self.literal_grade = 'R'
            self.evaluation = 'Reprobado'

    def is_passed(self):
        return self.literal_grade != 'R'

    def display_result(self):
        self.evaluate_grade()
        status = "Aprobado" if self.is_passed() else "Reprobado"
        print(f"Calificación numérica: {self.numeric_grade}")
        print(f"Calificación literal: {self.literal_grade}")
        print(f"Evaluación: {self.evaluation}")
        print(f"Estado: {status}")

# Ejemplo de uso
grade = float(input("Ingrese su calificación numérica: "))
evaluator = GradeEvaluator(grade)
evaluator.display_result()
