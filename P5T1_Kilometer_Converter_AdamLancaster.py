# Kilometer Converter
# 4/4/20
# CTI-110 P5T1
# Adam Lancaster

# miles = kilometers * 0.6214

def main():
    km = int(input('enter distance in kilometers: '))
    distConvert(km)

def distConvert(km):
    miles = km * 0.6214
    print('converted distance:', format(miles, ',.2f'), 'miles')

main()
