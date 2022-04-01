#1.Create a .py file
#2.Copy the class calculator to the .py file
#3.add the init function
#4.add the paramter self to the created functions
#5.create new ipynb, import that class calculator and call any of the functions.



class ageAadhar():
    
    def init(self):
        pass
        
    def ageCata(self):
        age=int(input("Enter the age:"))
        if(age<=18):
            print("childern")
        elif(age<=35):
            print("Adult")
        elif(age<=59):
            print("Citizen")
        else:
            print("Senior Citizen") 
            
    def addition(self):
        num1=int(input("ENter the number1:"))
        num2=int(input("ENter the number2:"))
        add=num1+num2
        print(add)
        
    def sub(self):
        print("Sub")
        
