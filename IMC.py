weight = float(input("Insert your weight: "))
height = float(input("Insert your height: "))

imc = weight / (height**2)

print(f"IMC: {imc:2f}")

if imc< 18.5:
    print("Low weight")
elif 18.5 <= imc < 24.9:
    print("Average weight")
elif 25 <= imc < 29.9:
    print("High weight")
else:
    print("Obessity")