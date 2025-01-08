dongari = ["MatKor", "WiCys", "CyKor", "AlKor", "$clear"]
letter = input()
print(next(item for item in dongari if item[0] == letter))