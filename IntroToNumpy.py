import numpy as np
print(f"Numpy version number is {np.__version__}\n")

ray = np.array([1, 2, 4, 4, 5, 6])
print(ray)
print(ray[2:5])


newRay = ray.reshape(2, 3)
print(f"ray Array has {newRay.ndim} dimensions.")
print(newRay[0, 1:3])
print(type(newRay))
print(newRay)
fourInst = np.where(newRay == 4)
print(f"The number 4 appears at {fourInst}")
evenInst = np.where(newRay % 2 == 0)
print(f"Even numbers are located at: {evenInst}")

newRayArr = newRay.reshape(3, 2)
print(newRayArr)
print(newRayArr[2, 0:])

copyNewest = newRayArr.copy()
copyNewest[1, 0] = 9
print(copyNewest)

viewOriginal = ray.view()
viewOriginal[0] = 9
print(viewOriginal)
print(f"{ray}\n")
viewOriginal[0] = 1

for r in ray:
    print(r)
print()
for r in newRay:
    print(r)
print()
for r in newRayArr:
    print(r)

arr1 = np.array([10, 11, 12, 13])
arr2 = np.array([14, 15, 16, 17])
arrComb = np.concatenate((arr1, arr2))
print(f"\n{arr1}\n +\n{arr2}\n =\n{arrComb}")

arr1New = arr1.reshape(2, 2)
arr2New = arr2.reshape(2, 2)
arrCombNew = np.concatenate((arr1New, arr2New), axis=1)
print(f"\n{arr1New}\n +\n{arr2New}\n =\n{arrCombNew}")

arr3 = np.array([10, 20, 30, 40, 50, 60])
nArr3 = np.array_split(arr2, 3)
print(f"\n{arr2}")
print(nArr3)

SS1 = np.searchsorted(arr3, 15)
print(SS1)

tripleO = np.array([6, 1, 5, 10, 7, 8])
print(f"\n{tripleO.dtype}")
print(tripleO)
print(np.sort(tripleO))

groceryList = np.array(['banana', 'apple', 'orange', 'grape'])
print(f"\n{groceryList.dtype}")
print(groceryList)
print(np.sort(groceryList))

boolList = np.array([True, False, True, False, True, False])
newBoolList = boolList.reshape(2, 3)
print(boolList)
print(np.sort(boolList))
print(newBoolList)
print(np.sort(newBoolList))

arr4 = np.array([100, 200, 300, 400, 500, 600])
j = [True, False, True, False, True, False]
newArr4 = arr4[j]
print(f"\n{arr4}")
print(newArr4)
reArr4 = arr4.reshape(3, 2)
print(reArr4)
z = np.array([[True, False], [True, False], [True, False]])
newReArr4 = reArr4[z]
print(newReArr4)

arr5 = np.array([41, 42, 43, 44])
filter_arr = []
for x in arr5:
    if x > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newArr5 = arr5[filter_arr]
print(f"\n{arr5}")
print(filter_arr)
print(newArr5)
