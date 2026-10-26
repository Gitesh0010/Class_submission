# --- LIST OPERATIONS ---
print("--- LIST ---")
students_list = ["Amit", "Bhavna", "Chetan"]
print("Original List:", students_list)
students_list.append("Diya")       # Add
print("After Add:", students_list)
students_list[1] = "Bharat"        # Update
print("After Update:", students_list)
students_list.remove("Chetan")     # Delete
print("After Delete:", students_list)

# --- TUPLE OPERATIONS ---
print("\n--- TUPLE ---")
# Tuples are immutable, so we use list conversion as a workaround
students_tuple = ("Esha", "Farhan", "Gaurav")
print("Original Tuple:", students_tuple)
temp_list = list(students_tuple)
temp_list.append("Harsh")          # Add
temp_list[0] = "Eshaan"            # Update
temp_list.remove("Farhan")         # Delete
students_tuple = tuple(temp_list)
print("After Add, Update, Delete:", students_tuple)

# --- DICTIONARY OPERATIONS ---
print("\n--- DICTIONARY ---")
students_dict = {101: "Isha", 102: "Jatin"}
print("Original Dictionary:", students_dict)
students_dict[103] = "Karan"       # Add
print("After Add:", students_dict)
students_dict[102] = "Jatin Roy"   # Update
print("After Update:", students_dict)
students_dict.pop(101)             # Delete
print("After Delete:", students_dict)
