def selection():
    print("Welcome to Unit Convertor")
    print("==============================")
    print("Mode Selection Menu")
    print("==============================")
    print("1: Length")
    print("2: Mass")
    print("3: Temperature")
    print("4: Time")
    print("5: Exit")
    print("==============================")
    while True:
        choice = int(input("Enter your mode from 1-5: "))
        if choice == 1:
            length()

        elif choice == 2:
            mass()

        elif choice == 3:
            temperature()

        elif choice == 4:
            time()

        elif choice == 5:
            print("==============================")
            print("Exiting the Unit Convertor...")
            print("Thank you for using Unit Convertor")
            print("==============================")
            break

        else:
            print("Invalid choice. Enter your choice from 1-5")
    
def length():
    print("==============================")
    print("=========================")
    print("You Choose Length Mode")
    print("=========================")
    print("Select Conversion Unit")
    print("1: Centimeter to Kilometer")
    print("2: Centimeter to Meter")
    print("3: Centimeter to Inch")
    print("4: Centimeter to Mile")
    print("5: Kilometer to Centimeter")
    print("6: Kilometer to Meter")
    print("7: Kilometer to Inch")
    print("8: Kilometer to Mile")
    print("9: Meter to Centimeter")
    print("10: Meter to Inch")
    print("11: Meter to Kilometer")
    print("12: Meter to Mile")
    print("13: Inch to Centimeter")
    print("14: Inch to Meter")
    print("15: Inch to Kilometer")
    print("16: Inch to Mile")
    print("17: Mile to Centimeter")
    print("18: Mile to Meter")
    print("19: Mile to Kilometer")
    print("20: Mile to Inch")
    print("21: Exit Here")
    length_choice = int(input("Enter your choice from 1-21: "))
    if length_choice == 1:
        cm_to_km()
        
    elif length_choice == 2:
        cm_to_m()

    elif length_choice == 3:
        cm_to_inch()

    elif length_choice == 4:
        cm_to_mile()

    elif length_choice == 5:
        km_to_cm()

    elif length_choice == 6:
        km_to_m()

    elif length_choice == 7:
        km_to_inch()

    elif length_choice == 8:
        km_to_mile()

    elif length_choice == 9:
        m_to_cm()

    elif length_choice == 10:
        m_to_inch()

    elif length_choice == 11:
        m_to_km()

    elif length_choice == 12:
        m_to_mile()

    elif length_choice == 13:
        inch_to_cm()

    elif length_choice == 14:
        inch_to_m()

    elif length_choice == 15:
        inch_to_km()

    elif length_choice == 16:
        inch_to_mile()

    elif length_choice == 17:
        mile_to_cm()

    elif length_choice == 18:
        mile_to_m()

    elif length_choice == 19:
        mile_to_km()

    elif length_choice == 20:
        mile_to_inch()

    elif length_choice == 21:
        print("==============================")
        print("Exiting the Length Mode...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-21")
   
        
def cm_to_km():
    print("====================================================")
    print("You seleted to convert centimeter to kilometer")
    print("====================================================")
    value = float(input("Enter centimeter value here: "))
    result = value / 100000
    print("%.2f" % result, "km")

def cm_to_m():
    print("====================================================")
    print("You seleted to convert centimeter to meter")
    print("====================================================")
    value = float(input("Enter centimeter value here: "))
    result = value / 100
    print("%.2f" % result, "m")

def cm_to_inch():
    print("====================================================")
    print("You seleted to convert centimeter to inch")
    print("====================================================")
    value = float(input("Enter centimeter value here: "))
    result = value / 2.54
    print("%.2f" % result, "inch")

def cm_to_mile():
    print("====================================================")
    print("You seleted to convert centimeter to mile")
    print("====================================================")
    value = float(input("Enter centimeter value here: "))
    result = value / 160900
    print("%.2f" % result, "mile")

def km_to_cm():
    print("====================================================")
    print("You seleted to convert kilometer to centimeter")
    print("====================================================")
    value = float(input("Enter kilometer value here: "))
    result = value * 100000
    print("%.2f" % result, "cm")

def km_to_m():
    print("====================================================")
    print("You seleted to convert kilometer to meter")
    print("====================================================")
    value = float(input("Enter kilometer value here: "))
    result = value * 1000
    print("%.2f" % result, "m")

def km_to_inch():
    print("====================================================")
    print("You seleted to convert kilometer to inch")
    print("====================================================")
    value = float(input("Enter kilometer value here: "))
    result = value * 39370.0787
    print("%.2f" % result, "inch")

def km_to_mile():
    print("====================================================")
    print("You seleted to convert kilometer to mile")
    print("====================================================")
    value = float(input("Enter kilometer value here: "))
    result = value * 0.621371
    print("%.2f" % result, "mile")

def m_to_cm():
    print("====================================================")
    print("You seleted to convert meter to centimeter")
    print("====================================================")
    value = float(input("Enter meter value here: "))
    result = value * 100
    print("%.2f" % result, "cm")

def m_to_inch():
    print("====================================================")
    print("You seleted to convert meter to inch")
    print("====================================================")
    value = float(input("Enter meter value here: "))
    result = value * 39.3700787
    print("%.2f" % result, "inch")

def m_to_km():
    print("====================================================")
    print("You seleted to convert meter to kilometer")
    print("====================================================")
    value = float(input("Enter meter value here: "))
    result = value / 1000
    print("%.2f" % result, "km")

def m_to_mile():
    print("====================================================")
    print("You seleted to convert meter to mile")
    print("====================================================")
    value = float(input("Enter meter value here: "))
    result = value / 1609.344
    print("%.2f" % result, "mile")

def inch_to_cm():
    print("====================================================")
    print("You seleted to convert inch to centimeter")
    print("====================================================")
    value = float(input("Enter inch value here: "))
    result = value * 2.54
    print("%.2f" % result, "cm")

def inch_to_m():
    print("====================================================")
    print("You seleted to convert inch to meter")
    print("====================================================")
    value = float(input("Enter inch value here: "))
    result = value / 39.3700787
    print("%.2f" % result, "m")

def inch_to_km():
    print("====================================================")
    print("You seleted to convert inch to kilometer")
    print("====================================================")
    value = float(input("Enter inch value here: "))
    result = value / 39370.0787
    print("%.2f" % result, "km")

def inch_to_mile():
    print("====================================================")
    print("You seleted to convert inch to mile")
    print("====================================================")
    value = float(input("Enter inch value here: "))
    result = value / 63360
    print("%.2f" % result, "mile")

def mile_to_cm():
    print("====================================================")
    print("You seleted to convert mile to centimeter")
    print("====================================================")
    value = float(input("Enter mile value here: "))
    result = value * 160900
    print(result, "cm")

def mile_to_m():
    print("====================================================")
    print("You seleted to convert mile to meter")
    print("====================================================")
    value = float(input("Enter mile value here: "))
    result = value * 1609.344
    print("%.2f" % result, "m")

def mile_to_km():
    print("====================================================")
    print("You seleted to convert mile to kilometer")
    print("====================================================")
    value = float(input("Enter mile value here: "))
    result = value * 1.609344
    print("%.2f" % result, "km")

def mile_to_inch():
    print("====================================================")
    print("You seleted to convert mile to inch")
    print("====================================================")
    value = float(input("Enter mile value here: "))
    result = value * 63360
    print("%.2f" % result, "inch")


def mass():
    print("==============================")
    print("=========================")
    print("You Choose Mass Mode")
    print("=========================")
    print("Select Conversion Unit")
    print("1: Gram to Kilogram")
    print("2: Gram to Ounce")
    print("3: Gram to Pound")
    print("4: Kilogram to Gram")
    print("5: Kilogram to Ounce")
    print("6: Kilogram to Pound")
    print("7: Ounce to Gram")
    print("8: Ounce to Kilogram")
    print("9: Ounce to Pound")
    print("10: Pound to Gram")
    print("11: Pound to Kilogram")
    print("12: Pound to Ounce")
    print("13: Exit Here")
    mass_choice = int(input("Enter your choice from 1-13: "))
    if mass_choice == 1:
        gm_to_kg()
        
    elif mass_choice == 2:
        gm_to_ounce()

    elif mass_choice == 3:
        gm_to_pound()

    elif mass_choice == 4:
        kg_to_gm()

    elif mass_choice == 5:
        kg_to_ounce()

    elif mass_choice == 6:
        kg_to_pound()

    elif mass_choice == 7:
        ounce_to_gm()

    elif mass_choice == 8:
        ounce_to_kg()

    elif mass_choice == 9:
        ounce_to_pound()

    elif mass_choice == 10:
        pound_to_gm()

    elif mass_choice == 11:
        pound_to_kg()

    elif mass_choice == 12:
        pound_to_ounce()

    elif mass_choice == 13:
        print("==============================")
        print("Exiting the Mass Mode...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-13")

def gm_to_kg():
    print("====================================================")
    print("You seleted to convert gram to kilogram")
    print("====================================================")
    value = float(input("Enter gram value here: "))
    result = value / 1000
    print("%.2f" % result, "kg")
    
def gm_to_ounce():
    print("====================================================")
    print("You seleted to convert gram to ounce")
    print("====================================================")
    value = float(input("Enter gram value here: "))
    result = value / 28.3495
    print("%.2f" % result, "ounce")
    
def gm_to_pound():
    print("====================================================")
    print("You seleted to convert gram to pound")
    print("====================================================")
    value = float(input("Enter gram value here: "))
    result = value / 453.592
    print("%.2f" % result, "pound")
    
def kg_to_gm():
    print("====================================================")
    print("You seleted to convert kilogram to gram")
    print("====================================================")
    value = float(input("Enter kilogram value here: "))
    result = value * 1000
    print("%.2f" % result, "gm")
    
def kg_to_ounce():
    print("====================================================")
    print("You seleted to convert kilogram to ounce")
    print("====================================================")
    value = float(input("Enter kilogram value here: "))
    result = value * 35.274
    print("%.2f" % result, "ounce")
    
def kg_to_pound():
    print("====================================================")
    print("You seleted to convert kilogram to pound")
    print("====================================================")
    value = float(input("Enter kilogram value here: "))
    result = value * 2.20462
    print("%.2f" % result, "pound")
    
def ounce_to_gm():
    print("====================================================")
    print("You seleted to convert ounce to kilogram")
    print("====================================================")
    value = float(input("Enter ounce value here: "))
    result = value * 28.3495
    print("%.2f" % result, "gm")
    
def ounce_to_kg():
    print("====================================================")
    print("You seleted to convert ounce to kilogram")
    print("====================================================")
    value = float(input("Enter ounce value here: "))
    result = value / 35.274
    print("%.2f" % result, "kg")
    
def ounce_to_pound():
    print("====================================================")
    print("You seleted to convert ounce to pound")
    print("====================================================")
    value = float(input("Enter ounce value here: "))
    result = value / 16
    print("%.2f" % result, "pound")
    
def pound_to_gm():
    print("====================================================")
    print("You seleted to convert pound to gram")
    print("====================================================")
    value = float(input("Enter pound value here: "))
    result = value * 453.592
    print("%.2f" % result, "gm")
    
def pound_to_kg():
    print("====================================================")
    print("You seleted to convert pound to kilogram")
    print("====================================================")
    value = float(input("Enter pound value here: "))
    result = value / 2.20462
    print("%.2f" % result, "kg")
    
def pound_to_ounce():
    print("====================================================")
    print("You seleted to convert pound to ounce")
    print("====================================================")
    value = float(input("Enter pound value here: "))
    result = value * 16
    print("%.2f" % result, "ounce")
    
   
def temperature():
    print("==============================")
    print("=========================")
    print("You Choose Temperature Mode")
    print("=========================")
    print("Select Conversion Unit")
    print("1: Celcius to Fahrenheit")
    print("2: Celcius to Kelvin")
    print("3: Fahrenheit to Celcius")
    print("4: Fahrenheit to Kelvin")
    print("5: Kelvin to Celcius")
    print("6: Kelvin to Fahrenheit")
    print("7: Exit Here")
    temperature_choice = int(input("Enter your choice from 1-7: "))
    if temperature_choice == 1:
        c_to_f()
        
    elif temperature_choice == 2:
        c_to_k()

    elif temperature_choice == 3:
        f_to_c()

    elif temperature_choice == 4:
        f_to_k()

    elif temperature_choice == 5:
        k_to_c()

    elif temperature_choice == 6:
        k_to_f()

    elif temperature_choice == 13:
        print("==============================")
        print("Exiting the Temperature Mode...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-7")

def c_to_f():
    print("====================================================")
    print("You seleted to convert celcius to fahrenheit")
    print("====================================================")
    value = float(input("Enter celcius value here: "))
    result = (value * 1.8) + 32
    print("%.2f" % result, "F")

def c_to_k():
    print("====================================================")
    print("You seleted to convert celcius to kelvin")
    print("====================================================")
    value = float(input("Enter celcius value here: "))
    result = value + 273.15
    print("%.2f" % result, "K")

def f_to_c():
    print("====================================================")
    print("You seleted to convert fahrenheit to celcius")
    print("====================================================")
    value = float(input("Enter fahrenheit value here: "))
    result = (value - 32) / 1.8
    print("%.2f" % result, "C")

def f_to_k():
    print("====================================================")
    print("You seleted to convert fahrenheit to kelvin")
    print("====================================================")
    value = float(input("Enter fahrenheit value here: "))
    result = ((value - 32) / 1.8) + 273.15
    print("%.2f" % result, "K")

def k_to_c():
    print("====================================================")
    print("You seleted to convert kelvin to celcius")
    print("====================================================")
    value = float(input("Enter kelvin value here: "))
    result = value - 273.15
    print("%.2f" % result, "C")

def k_to_f():
    print("====================================================")
    print("You seleted to convert kelvin to fahrenheit")
    print("====================================================")
    value = float(input("Enter kelvin value here: "))
    result = ((value - 273.15) * 1.8) + 32
    print("%.2f" % result, "F")

def time():
    print("==============================")
    print("=========================")
    print("You Choose Time Mode")
    print("=========================")
    print("Select Conversion Unit")
    print("1: Second to Minute")
    print("2: Second to Hour")
    print("3: Second to Day")
    print("4: Minute to Second")
    print("5: Minute to Hour")
    print("6: Minute to Day")
    print("7: Hour to Second")
    print("8: Hour to Minute")
    print("9: Hour to Day")
    print("10: Day to Second")
    print("11: Day to Minute")
    print("12: Day to Hour")
    print("13: Exit Here")
    time_choice = int(input("Enter your choice from 1-13: "))
    if time_choice == 1:
        sec_to_min()
        
    elif time_choice == 2:
        sec_to_hour()

    elif time_choice == 3:
        sec_to_day()

    elif time_choice == 4:
        min_to_sec()

    elif time_choice == 5:
        min_to_hour()

    elif time_choice == 6:
        min_to_day()

    elif time_choice == 7:
        hour_to_sec()

    elif time_choice == 8:
        hour_to_min()

    elif time_choice == 9:
        hour_to_day()

    elif time_choice == 10:
        day_to_sec()

    elif time_choice == 11:
        day_to_min()

    elif time_choice == 12:
        day_to_hour()

    elif time_choice == 13:
        print("==============================")
        print("Exiting the Time Mode...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-13")

def sec_to_min():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value / 60
        print("%.2f" % result, "min")
    else: 
        print("Please enter the positive value")

def sec_to_hour():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value / 3600
        print("%.2f" % result, "hour")
    else: 
        print("Please enter the positive value")

def sec_to_day():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value / 86400
        print("%.2f" % result, "day")
    else: 
        print("Please enter the positive value")

def min_to_sec():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value * 60
        print("%.2f" % result, "sec")
    else: 
        print("Please enter the positive value")

def min_to_hour():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value / 60
        print("%.2f" % result, "hour")
    else: 
        print("Please enter the positive value")

def min_to_day():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value / 1440
        print("%.2f" % result, "day")
    else: 
        print("Please enter the positive value")

def hour_to_sec():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value * 3600
        print("%.2f" % result, "sec")
    else: 
        print("Please enter the positive value")

def hour_to_min():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value * 60
        print("%.2f" % result, "min")
    else: 
        print("Please enter the positive value")

def hour_to_day():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value / 24
        print("%.2f" % result, "day")
    else: 
        print("Please enter the positive value")

def day_to_sec():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value * 86400
        print("%.2f" % result, "sec")
    else: 
        print("Please enter the positive value")

def day_to_min():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value * 1440
        print("%.2f" % result, "min")
    else: 
        print("Please enter the positive value")

def day_to_hour():
    print("====================================================")
    print("You seleted to convert second to minute")
    print("====================================================")
    value = float(input("Enter second value here: "))
    if value > 0:
        result = value * 24
        print("%.2f" % result, "hour")
    else: 
        print("Please enter the positive value")


selection()