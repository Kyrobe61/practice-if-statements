countries = ("USA", "Switzerland")

country = input("Please enter the country for citizenship inquiry: ")

if country not in countries:
 print("Invalid entry! Terminating the program.")


if country == "USA":
        aa = input("Was the applicant born in the United States or a territory of the United States? ").lower()
        if aa == "yes":
              print("The applicant is a U.S. citizen.")
        elif aa == "no":
              bb = input("Was at least one of the applicant's parents a U.S. citizen? ").lower()
              if bb == "yes":
                   print("The applicant is a U.S. citizen.")
              elif bb == "no":
                   print("The applicant is not a U.S. citizen.")
              else:
                 print("Invalid entry! Terminating the program.") 

        else: 
          print("Invalid entry! Terminating the program.")


elif country == "Switzerland":
       cc = input("Are the applicant's parents married? ").lower()
       if cc == "yes":
            dd = input("Is one of the parents a Swiss citizen? ").lower()
            if dd == "yes":
                 print("The applicant is a Swiss citizen.")
            elif dd == "no":
                 print("The applicant is not a Swiss citizen.")
            else:
                 print("Invalid entry! Terminating the program.")     

       elif cc == "no":
             ee = input("Is unmarried mother a Swiss citizen? ").lower()
             if ee == "yes":
                 print("The applicant is a Swiss citizen.")
             elif ee == "no":
                 ff = input("Is unmarried father a Swiss citizen? ").lower()
                 if ff == "yes":
                      gg = input("Does unmarried father acknowledge paternity? ").lower()
                      if gg == "yes":
                            print("The applicant is a Swiss citizen.")
                      elif gg == "no":
                            print("The applicant is not a Swiss citizen.")
                      else: 
                        print("Invalid entry! Terminating the program.")  

                 elif ff == "no":
                       print("The applicant is not a Swiss citizen.")
                 else: 
                        print("Invalid entry! Terminating the program.")       

             else:
                 print("Invalid entry! Terminating the program.")

       else:
          print("Invalid entry! Terminating the program.")
