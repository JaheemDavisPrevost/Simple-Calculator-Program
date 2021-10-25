#Author: Jaheem Prevost
#Project: Simple Calculator Program
#Date Created: 10/23/2021

def calculator():
        
            

    try: 
            print("Welcome to Calculator")

            num1 = int(input("Enter A Number: "))#User will be prompted to enter a number that will be stored in variabl "num1"

            operator = input("Enter an Operator: ")#User will be prompted to enter an operator that will be stored in variable "operator"

            num2 = int(input("Enter A second Number: "))#User will be prompted to enter a second number that will be stored in variable "num2"

            if operator == "+": #Conditional Statment Block that performs operations on the two variables and prints the result to screen depending on user input and prints out an error message when given an invalid operator
                
                print("The result is: ", num1 + num2)
            elif operator == "-":
                print("The result is: ", num1 - num2)
            elif operator == "/": 
                print("The result is: ", num1 / num2)
            elif operator =="*": 
                print("The result is: ", num1 * num2)
            elif operator == "**":
                print("The result is: ", num1 ** num2)
            elif operator == "//": 
                print("The result is: ", num1 // num2)
            elif operator == "%": 
                print("The result is: ", num1 % num2)
            elif operator != "*":
                print("Syntax Error: Valid Operator was not given.")
            elif operator != "-":
                print("Syntax Error: Valid Operator was not given.")
            elif operator != "+":
                print("Syntax Error: Valid Operator was not given.")
            elif operator != "/":
                print("Syntax Error: Valid Operator was not given.")
            elif operator != "//":
                print("Syntax Error: Valid Operator was not given.")
            elif operator != "%":
                print("Syntax Error: Valid Operator was not given.")

    except ValueError:# ValueError Except Block that executes in the case that the user does not input a valid integer
            print("Syntax Error: Valid Integer Value Not Given. Try Again.")

    except ZeroDivisionError:# ZeroDivisionError Except Block that executes in the case that the user attempts to divide or modulo by zero
            print("Syntax Error: Division By Zero Not Possible.")


calculator()
