def display_info(**kwargs):  # **  คือการส่งพารามิตเตอร์แบบคู่เช่น name="Alice", age=30, city="New York"
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

