import numpy as np
StudentMarkList = [65,45,85,95,55,64,77,85,94,35]
StudentMarkTuple = (25,35,48,65,75,48,95,65,48,45)

print("Student Mark List:", StudentMarkList )
print("Student Mark Tuple", StudentMarkTuple)

arrayList = np.array(StudentMarkList )
arrayTuple = np.array(StudentMarkTuple)

print("\nStudent Mark List Array:", arrayList )
print("Student Mark Tuple Array :", arrayTuple)

part_size = (len(arrayList)) // 3

slice1 = arrayList[:part_size]
slice2 = arrayList[part_size:2 * part_size]
slice3 = arrayList[2 * part_size:]

print("\nSlice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)
