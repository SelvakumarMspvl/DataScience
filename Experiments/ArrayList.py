import numpy as np

class ArrayList:
    def __init__(self):
        self.StudentMarkList = [65,45,85,95,55,64,77,85,94,35]
        self.StudentMarkTuple = (25,35,48,65,75,48,95,65,48,45)

    def main(self):
        print("Student Mark List:", self.StudentMarkList )
        print("Student Mark Tuple", self.StudentMarkTuple)

        arrayList = np.array(self.StudentMarkList )
        arrayTuple = np.array(self.StudentMarkTuple)

        print("\nStudent Mark List Array:", arrayList )
        print("Student Mark Tuple Array :", arrayTuple)

        n = len(arrayList)
        part_size = n // 3

        slice1 = arrayList[:part_size]
        slice2 = arrayList[part_size:2 * part_size]
        slice3 = arrayList[2 * part_size:]

        print("\nSlice 1:", slice1)
        print("Slice 2:", slice2)
        print("Slice 3:", slice3)

if __name__ == "__main__":
    obj = ArrayList()
    obj.main()