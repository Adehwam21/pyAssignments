class Student:
    def __init__(self) -> None:
        self._name = None
        self._studentID = None
        self._courseList = []

    def setName(self,name: str):
        self._name = name
        
    def getName(self) -> str:
        return self._name
        
    def setStudentID(self, studentID: str):
        self._studentID = studentID
        
    def getStudentID(self) -> str:
        return self._studentID
        
    def addCourse(self, course):
        if course not in self._courseList:
            self._courseList.append(course)
        else:
            print("Course already in list")
        
    def removeCourse(self, course):
        if course in self._courseList:
            self._courseList.remove(course)
            print(f"Course removed: {course}")
        else:
            print("There is no such course in the list")
    
    def displayCourses(self) -> None:
        return self._courseList
    
student1 = Student()

if __name__ == "__main__":
    # setting object attributes
    student1.setName("Aaron")
    student1.setStudentID("10964242")

    student1.addCourse("dcit 201")
    student1.addCourse("dcit 203")
    student1.addCourse("dcit 205")
    student1.addCourse("dcit 209")

    # displaying object's set attribites
    print(f"Student name: {student1.getName()}")
    print(f"Student ID: {student1.getStudentID()}")
    print(f"Courses Offering: {student1.displayCourses()}\n")

    # removing courses
    student1.removeCourse("dcit 209")

    # displaying courses after removing a course
    print(f"\nCourses Offering: {student1.displayCourses()}")



