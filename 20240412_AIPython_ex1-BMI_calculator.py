def BMI(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

def isObesity(bmi):
    if bmi < 20:
        return "저체중"
    elif bmi < 25:
        return "정상"
    elif bmi < 30:
        return "과체중"
    else:
        return "비만"
    

height = 190
weight = 90
bmi = BMI(height, weight)
print("Your BMI is", bmi)
print("당신은", isObesity(bmi), "입니다.")