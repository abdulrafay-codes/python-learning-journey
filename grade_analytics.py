def calculate_average(total_marks, total_subjects):
    average = total_marks / total_subjects
    return average
def calculate_scholarship(average):
    if average >= 90:
        return "Full Scholarship (Tier 1)"
    elif average >= 80:
        return "Partial Scholarship (Tier 2)"
    else:
        return "No Scholarship avaliable."
Marks = int(input("Enter total marks obtained: "))
Subjects = int(input("Enter total number of subjects: "))
final_avg = calculate_average(Marks, Subjects)
scholarship_status = calculate_scholarship(final_avg)
print("Average Marks:", final_avg)
print("Scholarship Status:", scholarship_status)
