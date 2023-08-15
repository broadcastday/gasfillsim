# Create random price fluctuations day to day from 5.85 to 7.14
# Full is every 8 days, half every 4
# If today's price is lower than yesterday, full
# IF today's price is higher, half
# Methodology for pricing: If < yester price AND < last tx full, else half
import random

    
def gasPricing():
    gasPrice = 5.85

    outcome = random.randint(1,10)
    if outcome >= 8:
        gasPrice += .25
    elif outcome >= 3:
        gasPrice += .1
    elif outcome < 3:
        gasPrice -= .1
    elif outcome == 1:
        gasPrice -= -.25
    return gasPrice


gasTank = 14
costAcc = 0

#Day increment
pricemem = [5.85, 5.90, 5.75]
day = 0
for i in range(0,90):
    day += 1
    print("Day",day)
    gasTank -= 1.28
    pricemem.append(gasPricing())
    avgtargetprice = (pricemem[i] + pricemem[i-1] + pricemem[i-2])/3
    print("price today:",gasPricing())
    print("Fuel status:",gasTank)
    print("Avg target price is: ", avgtargetprice)
    if gasTank > 8:
        continue
    elif gasTank <= 2:
        costAcc += (14-gasTank)*gasPricing()
        print("Fill completed at" , gasTank, "on", day)
        gasTank = 14
    elif gasTank < 8 and gasTank > 2:
        if avgtargetprice > gasPricing():
            costAcc += (14-gasTank)*gasPricing()
            print("Fill completed at" , gasTank, "on", day)
            gasTank = 14
            if avgtargetprice < gasPricing():
                continue

print("Your cost is", costAcc)      
        

    
