#jasmin ericka a. celebre
#bscpe 1-4

#open file
with open ("student_gwa.txt", "r") as my_file:
#initialize the name and highest gwa
    highest_gwa = 0
    student_name= " "
#loop through the file
    for line in my_file:
        #split
        student, gwa = line.split(" ")
        #float gwa
        gwa = float (gwa)
#check the gwas
#print output