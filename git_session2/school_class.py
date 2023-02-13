
class School:
    
    name = "lagos state college of health"
    location = "8, harvey road yaba lagos"
    deparment = ["mlt", "chew", "jchew", "eht", "phleb", "complementry", "pharmacy", "health_record"]
    population = 0
    max_population = 10000
    provost = "Dr_moyo_kassim"
    deupty_provost = "mrs_oyeronkeb_izobo"
    
    def __init__(self):
        print(f"school class{school.name} successfuly created.")
        
    @classmethod   
    def display_name(cls):
        print(school.name)
        
    @classmethod    
    def display_location(cls):
        print(school.location)
        
    @classmethod   
    def display_departmen(cls):
        for dept in school.deparment:
            print(dept)
    
    @classmethod
    def check_population(cls):
        print(school.population)
        
    @classmethod
    def display_max_population(cls):
        print(School.max_population)
        
    @classmethod
    def provost(cls):
        print(school.provost)
        
    @classmethod
    def deupty_provost(cls):
        print(school.deupty_provost)
        
        
class Deparment(School):
    
    
    def __init__(self, student_name, dept, matric):
        self.name = name
        self.dept = dept
        self.matric = matric
        self.admission_year = int(input("enter year of admission:"))
        
        
    def get_student_name(self):
        return self.name
    
    def get_dept(self):
        if self.dept not in school.deparment:
            print("invalid input for deparment. please check and re-enter your department")
            while True:
                dept = input("enter your department:")
            print(self.department)
    
    def get_matric(self):
        if self.department in school.department and self.admission_year == 2023:
            print(self.department[0:2]+(self.admission_year[0:3]))
            
