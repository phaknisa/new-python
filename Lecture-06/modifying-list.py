# ตำแหน่ง 0 1 2 3 4 (เริ่มนับจาก 0 เสมอ)
shapes = ["circle", "square", "triangle", "rectangle", "hexagon"]
shapes[1] = "ellipse" # สามาเปลี่ยนข้อมูลใน List ได้โดยใช้ ตัวเปลี่ยนตำแหน่งและใส่ข้อมูลลงไปแทน
shapes[3] = "pentagon" # [....] ใส่ตำแหน่งด้านใน [...] = "....."
print(f"Modified shapes: {shapes}")