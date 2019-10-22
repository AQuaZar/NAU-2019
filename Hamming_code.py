import random

print("Enter your number")
initValue = int(input())
binaryStr = str(bin(initValue))
elemList = list(map(int, binaryStr[2:]))
print(f"Your number formatted in binary: {elemList}")

print(f"Type index of bit where mistake will occur [1 - {len(elemList)}]")
errorIndex = int(input()) - 1
errorIndexAnalyzed = 0

newListWithError = [
    1 - elemList[x] if x == errorIndex else elemList[x] for x in range(len(elemList))
]
print(f"Corrupted binary message: {newListWithError}")

_ = input()
8
print(
    "Control bits are inserted in special places, indexes that are power of 2 (1,2,4,8..)"
)


def controlBitValue(tempList):
    print("Inserting control bits")
    [tempList.insert((2 ** x) - 1, 0) for x in range(4)]
    print(tempList)
    controlBitsAmount = [0, 0, 0, 0]
    for k in range(1, len(tempList) + 1):
        if tempList[k - 1] == 1:
            binTemp = str(bin(k))
            for s in range(1, len(binTemp)):
                if binTemp[-s] == "1":
                    controlBitsAmount[s - 1] += tempList[k - 1]
    _ = input()
    print(
        "Counting how many ones controls every control bit, if amount is odd - control bit = 1, else control bit = 0"
    )
    for x in range(4):
        if controlBitsAmount[x] % 2 != 0:
            tempList[(2 ** x) - 1] = 1
    _ = input()


_ = input()
controlBitValue(elemList)
print(f"Ready for sending binary message: {elemList}")
print(" ")
_ = input()
print(f"Now we repeat procedure of calculating control bits for corrupted message")
controlBitValue(newListWithError)
print(newListWithError)

for x in range(4):
    if elemList[(2 ** x) - 1] != newListWithError[(2 ** x) - 1]:
        errorIndexAnalyzed += 2 ** x
_ = input()
print(f"Index of the error: {errorIndexAnalyzed}")
print("Fixing mistake")
newListWithError[errorIndexAnalyzed - 1] = 1 - newListWithError[errorIndexAnalyzed - 1]
print(newListWithError)
print("Removing control bits")
newListWithoutError = []
x = 0
for i in range(len(newListWithError)):
    if i != (2 ** x) - 1:
        newListWithoutError.append(newListWithError[i])
    else:
        x += 1

print(newListWithoutError)
