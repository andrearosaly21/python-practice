******************************************************************************************SECTION 1**********************************************************************************************************

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department) 
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code, initials)
last_three = employee_code[-3:]
print(last_three)

****************************************************************************************************SECTION 2*********************************************************************************************
  
email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')

display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

phone = '123-456-7890'
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')

dot_count = clean_email.count('.')
dash_count = employee_code.count('-')

print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')

************************************************************************SECTION 3******************************************************************************************************************

running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')

*************************************************************************************************SECTION 4**********************************************************************************************
  
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print(f'Final price of ticket: {final_price}') 

else:
    print('Ticket booking failed due to restrictions')

******************************************************************************************SECTION 5**********************************************************************************************************

 Build a Travel Weather Planner:

distance_mi = 1
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True
if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:        
    if distance_mi > 6 and (has_car or has_ride_share_app):
        print(True)
    else:
        print(False)

***********************************************************************************************SECTION 6***************************************************************************************************
MIO: CHATGPT EXERCISE FOR ME

  def saludar_centro(nombre_centro, idioma):                                                                                                                                                                                                           
    print(nombre_centro  + idioma)                                                                                                
    if idioma == "quechua":                                                                                    
      print("allianlla kachun", nombre_centro)                                                     
    elif idioma == "español":                                                                                            
      print("Bienvenidos al centro", nombre_centro)
    else:
      print("Centro médica:", nombre_centro)
  
def calcular_medicamento(pastillas_por_dia, dias):                                                               
        Total = (pastillas_por_dia, dias)                                        
        print('Total') # None                                                                                             
def calcular_medicamentos(pastillas_por_dias, dias)                           
        return(pastillas_por_dias, dias)                                                                                
        print('Total')
  
def obtener_alerta_salud(codigo_alerta):                                       
    if codigo_alerta ==1:                                                                 
      return( "Fiebre alta", "Nina unquy")                                                                  
    elif codigo_alerta ==2:                                                                                             
      return("Falta aire", "Samay siriy")                                                                        
    else:                                                                                                                        
      return("Consulta general", "Mana yachasqa unquy")   

************************************************************************SECTION 7****************************************************
BUILD A KITCHEN INVENTORY TRACKER

available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs

available_eggs = make_fried_egg(available_eggs)

check_kitchen_stock()
*******************************************************************section 8************************************************************************
Build an Apply Discount Function

def apply_discount(price, discount):
    if not isinstance(price,(int,float)):
        return "The price should be a number"
    if not isinstance(discount,(int,float)):
        return"The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount >100:
        return "The discount should be between 0 and 100"
    apply_discount = price*(discount/100)
    return price - apply_discount
  
***********************************************************SECTION 9********************************************************************************
BUILD A CAESAR CIPHER

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int) or isinstance(shift, bool):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text,13)
print(decrypted_text)
print(encrypted_text)

******************************************************************************SECTION 10*******************************************************




