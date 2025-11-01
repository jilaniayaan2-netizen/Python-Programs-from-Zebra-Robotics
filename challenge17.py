slices = int(input("how many slices: "))
students = int(input("how many children require sustenance: "))
slicePerChild = slices // students
leftOver = slices % students
print("each child will consume" + " " + str(slicePerChild) + ". " + "there will be" + " " + str(leftOver) + " " + "sustenance left over.")
