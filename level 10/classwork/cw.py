def calculate_bmi():
    weight = float(input("53(კგ): "))
    height = float(input("1.77(მეტრი): "))
    bmi = weight / (height ** 2)
    print(f"თქვენი BMI: {bmi:.2f}")
    
    example_bmi = 25.0 
    print(f"BMI ({bmi:.2f}) > {example_bmi}: {bmi > example_bmi}")
    print(f"BMI ({bmi:.2f}) < {example_bmi}: {bmi < example_bmi}")
    print(f"BMI ({bmi:.2f}) >= {example_bmi}: {bmi >= example_bmi}")
    print(f"BMI ({bmi:.2f}) <= {example_bmi}: {bmi <= example_bmi}")
    print(f"BMI ({bmi:.2f}) == {example_bmi}: {bmi == example_bmi}")
    print(f"BMI ({bmi:.2f}) != {example_bmi}: {bmi != example_bmi}")

calculate_bmi()