fruits_with_duplicates = ["apple" , "banana", "apple" , "cherry", "banana", "apple" , "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits without duplicates: {fruits_with_duplicates}")

# remove = loop ลบ list ออกจาก list เดิม และดันตัวข้างหลังเข้ามาแทน