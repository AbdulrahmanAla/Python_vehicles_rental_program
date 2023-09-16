###########################################################################################################################################
#           print the banner that was given by the instructor                                                                             #
#           promot for the clasification: Budget( BD ) Daily ( D ) Weekly ( W ) any other letter will display an erorr message            #
#           promot for the number of days vechile was rented                                                                              #
#           promot The vehicle's odometer reading at the start of the rental period (an integer)                                          #
#           promot The vehicle's odometer reading at the end of the rental period (an integer)                                            #
#           preform calculations of the bill based on the information given in the pdf                                                    #
#           display the information that was promted in addtion to the bill                                                               #
#           promot again to see if the user wants to exit the loop by selecting B or continue by selecting the letter A                   #
###########################################################################################################################################

#import math library to use the math function was given in the document to calculate the weeks
import math


#display the banner
banner = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
print(banner)


# promot if the user want to countinue the program or not and create a loop for the program, then promot the classification code, days, odometer reading at start and odometer reading at end
promot = input("\nWould you like to continue (A/B)? \n")
while promot == "A":
    code= input("\nCustomer code (BD, D, W): \n")
    while code != "BD" and code !="D" and code != "W" :
        print("\n\t*** Invalid customer code. Try again. ***")
        code= input("\nCustomer code (BD, D, W): \n")
    days= int(input("\nNumber of days: \n"))
    Odometer_reading_at_the_start= int(input("Odometer reading at the start: \n"))
    Odometer_reading_at_the_end= int(input("Odometer reading at the end:   \n"))


#calculate the miles were driven taking into consideration the different cases  if the odometer reading at start was higher than odometer reading at end or the opssite, or id the odometer reading has rested it self if it reached the maximum
    if Odometer_reading_at_the_end > Odometer_reading_at_the_start:
        miles_driven= (Odometer_reading_at_the_end - Odometer_reading_at_the_start) /10
    elif Odometer_reading_at_the_start> Odometer_reading_at_the_end and (Odometer_reading_at_the_start+Odometer_reading_at_the_end) >= 1000000 :
        miles_driven= (((1000000-Odometer_reading_at_the_start)+Odometer_reading_at_the_end))/10         
    elif Odometer_reading_at_the_start> Odometer_reading_at_the_end:
        miles_driven= ((Odometer_reading_at_the_start - Odometer_reading_at_the_end)/10)
    

 #display the information that was promted from the user  - information such as: classification code, days, odometer reading at start, odometer reading at end and the miles that were driven

    print("\nCustomer summary:")
    print("\tclassification code:",code)
    print("\trental period (days):",days)
    print("\todometer reading at start:",Odometer_reading_at_the_start)
    print("\todometer reading at end:  ",Odometer_reading_at_the_end)
    print("\tnumber of miles driven: ",miles_driven)
    
    
#calculate the bill for each of classification codes taking into consideration the different cases if the user should be charged extra fee or not


#calculate the bill if the classification code was for days
    if code == "D":
        avg_mile_perday= miles_driven /(days)
        if avg_mile_perday > 100:    
            bill = (60.00 * days) +(0.25 * (miles_driven - (100*days)))
            print("\tamount due: $",bill)
            
        else:
            bill = (60.00 * days)
            print("\tamount due: $",bill)
            
#calculate the bill if the classification code was for Budget

    elif code == "BD":
        bill = (40.00 * days) +(0.25 * miles_driven)
        print("\tamount due: $",bill)

#calculate the bill if the classification code was for weeks
    elif code == "W":
        weeks= float(math.ceil(days/7))
        
 # calculate the bill if miles were driven per week less than 900 miles   
        if miles_driven < (900*weeks):
            bill = float((190*weeks))
            print("\tamount due: $",round(bill,2))

#calculate the bill if miles were driven per week more than 900 miles and less than 1500 miles
        elif (900*weeks) < miles_driven <(1500*weeks) :
            bill= float((100 *weeks))+float((weeks*190))
            print("\tamount due: $",round(bill,2))

#calculate the bill if miles were driven per week more than 1500 miles
        elif miles_driven > (1500*weeks) :
           bill= float((190*weeks))+  float((200 *weeks))+  float(((miles_driven-(1500*weeks))*0.25))
           
           print("\tamount due: $",round(bill,2))  
 # the displayed message if the user entered any letter other than W or D or BD. with also a promot for the classification code      
    else:
        print("\n\t*** Invalid customer code. Try again. ***")
        code= input("\nCustomer code (BD, D, W): \n")
        
    
    promot = input('''\nWould you like to continue (A/B)? \n''')
    

#The statment that will be printed if the user exist the loop
print("Thank you for your loyalty.")
