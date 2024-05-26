num1 = 25
num2 = 45

# Calculating HCF here
for i in range(1, max(num1, num2)):
    if num1 % i == num2 % i == 0:
        hcf = i

# LCM formula
lcm = (num1*num2)//hcf

print("LCM of", num1, "and", num2, "is", lcm,"hcf is" ,hcf)