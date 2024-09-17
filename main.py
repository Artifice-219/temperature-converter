# convertion  function
def convertion(input_temp, input_scale, output_scale):
   
    # parsing given output scale and printing the result
    if(output_scale == 'k' and input_scale == 'c'):
     print(f'Result :  {to_kelvins(input_temp)}')

    elif(output_scale == 'c' and input_scale == 'k'):
       print(f'Result : {to_celsius(input_temp)}')


# helper function to convert 
def to_kelvins(input_temp):
    converred_value =  input_temp + 273.15 
    return round(converred_value, 2)

def to_celsius(input_temp): 
   converted_value = input_temp - 273.15
   return round(converted_value, 2)

def will_retry():
   choice = str(input('Would you like to continue [ y/n ]'))

   if(choice == 'y' or choice == 'Y'):
      return True
#    defaults to false
   else:
      return False
   


while(True):

 input_temp = float(input('Enter Temperature value :'))
 print('Allowed Scales are [ c ] Celsius & [ k ] Kelvins')
 input_scale = str(input('Enter Scale : '))
 print('Allowed Output Scales are [ c ] Celsius & [ k ] Kelvins')
 output_scale = str(input('Enter output scale : '))

 convertion(input_temp,input_scale,output_scale)

#  loop control 
 if(will_retry() == False):
    break

