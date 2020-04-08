# Feet to Inches Converter
# 4/4/20
# CTI-110 P5T2_FeetToInches
# Adam Lancaster
#

def main():
    ft = int(input('enter distance in feet: '))
    feet_to_inches(ft)
    
def feet_to_inches(ft):
    inches = ft * 12
    print('converted distance:', inches, 'inches')

main()
    
    
