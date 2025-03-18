def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def get_average(self):
        return calculate_average(self.grades)
    
    def __str__(self):
        return f"{self.name} - Average: {self.get_average():.2f}"

# Example usage
def main():
    # Create a list of students
    students = [
        Student("Alice", [85, 92, 78, 95]),
        Student("Bob", [72, 88, 91, 68]),
        Student("Charlie", [90, 95, 89, 92])
    ]
    
    # Print student information
    for student in students:
        print(student)
    
    # Demonstrate list comprehension
    all_grades = [grade for student in students for grade in student.grades]
    print(f"\nClass average: {calculate_average(all_grades):.2f}")

if __name__ == "__main__":
    main()