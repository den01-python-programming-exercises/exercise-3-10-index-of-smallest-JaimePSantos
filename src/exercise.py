def main():
    #write your code below this line
    intList = []
    min1 = str(9999999)
    index = 0

    while(True):
      numberStr = input()
      if(numberStr=="-1"):
        break
      intList.append(numberStr)
    
    for i in range(len(intList)):
      if(int(intList[i])<int(min1)):
        min1 = intList[i]
    print("Smallest number: %s"%min1)

    for i in range(len(intList)):
      if(int(intList[i])==int(min1)):
        print("Found at index: %s"%i)
    
if __name__ == '__main__':
    main()
