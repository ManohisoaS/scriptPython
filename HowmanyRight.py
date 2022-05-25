
file_path="numberList.txt"

def howManyRight(numbers):
    rightCount = 0 
    for i in range(len(numbers)-1):
        number = numbers[i]
        subNumbers = numbers[i+1:]
        if number > max(subNumbers):
            rightCount+=1
    return rightCount

if __name__ == "__main__":
    with open(file_path,"r") as file:
        rawNumbers = file.readlines()
        numbers = ''.join(rawNumbers).split(",")
        rightCount = howManyRight(numbers)
        print(f"Il y a %d entiers qui sont strictement plus grands que tous les entiers à leur droite dans la le fichier %s"%(rightCount,file_path))


