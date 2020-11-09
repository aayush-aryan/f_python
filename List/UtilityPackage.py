class Ulility:
    @staticmethod
    def createList():
        givenList=[]
        try:
            a=int(input("Enter the number of element in list: "))
            print()
            for i in range(a):
                value=input("Enter the element of list: ")
                givenList.append(value)
            return givenList
        except:
            print("PROVIDE CORRECT INPUT")
