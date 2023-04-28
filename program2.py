#jasmin ericka a. celebre
#bscpe 1-4

#open the file
file = open("student_gwa.txt","r")

#initialize the highest GWA and the student who got it
highest_gwa = 0
name = ""

#Loop through each line of the file
for line in file:
    #split the line
    student,gwa = line.split(" ")
    #convert the gwa to a float
    gwa = float(gwa)

    #check if the gwa is higher than the previous highest gwa
    if gwa > highest_gwa:
        #update the highest gwa and the student who got it
        highest_gwa = gwa
        name = student

#print the student who got the highest gwa
print("The student who got the highest GWA is {} with GWA of {}".format(name,highest_gwa))

#close the file
file.close()