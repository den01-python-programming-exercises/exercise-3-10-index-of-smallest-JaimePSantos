def main():
    #write your code below this line
    intList = []
    min1 = 9999999
    index = 0

    while(True):
      number = int(input())
      if(number==-1):
        break
      intList.append(number)
      if(min1>=intList[index]):
        min1 = intList[index]
      index+=1

    
    print("Smallest number: %s"%min1)

    for i in range(len(intList)):
      if(intList[i]==min1):
        print("Found at index: %s"%i)
if __name__ == '__main__':
    main()
