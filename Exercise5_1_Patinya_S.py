"""
Patinya Sribrowornnara
19:15 4/6/2564

Exercise 5 : ปฏิบัติการพัฒนาโปรแกรมที่ใช้งานได้จริง และ ข้อมูล
1.ตั้งชื่อไฟล์ Exercise5_1_ชื่อ_ตัวอักษรแรกของนามสกุล.py

"ให้ผู้เรียนลองใช้งานประโยชน์จากตัวแปร และ ตัวดำเนินการ รวมถึงข้อมูลสร้างโปรแกรมสำคัญคำนวณเลข โดยจะมีตัวเลขทั้งหมด 2 ตัว
นำมาทำการ บวก ลบ คูณ และ หารกัน โดยให้แสดงคำตอบออกมาในรูปแบบด้านล่าง
ดยตัวเลขสามารถเป็นตัวเลขอะไรก็ได้ที่ผู้ใช้งานต้องการ โดยการเปลี่ยนตัวเลขใหม่นั้นให้ผู้ใช้งานแก้ไขโค้ดให้น้อยที่สุด"

ตัวอย่างรูปแบบ Output ที่แสดงผลโปรแกรม
-----------------------------------
10 + 2 = 12
10 - 2 = 8
10 * 2 = 20
10 / 2 = 5
-----------------------------------
"""


number1 = 10
number2 = 2

addition    = number1 + number2
minus       = number1 - number2
subtraction = number1 * number2
divide      = number1 / number2

print (number1,"+",number2,"=",addition)
print (number1,"-",number2,"=",minus)
print (number1,"*",number2,"=",subtraction)
print (number1,"/",number2,"=",divide)


"""
ข้อนี้ผมคิดว่าโจทย์ผลลัพธ์ที่ได้จากการหารคือ 5 ผิด ถูกจะเป็น 5.0 (ไม่แน่ใจอาจจะวางบัคไว้หรือเปล่า)
หากนำไปหารกันไม่ว่าการประเภทข้อมูลจะเป็นชนิด integer หรือ float 
ผลลัพธ์จะออกมาได้เป็น float ตามที่พี่เปรมได้เคยอธิบายไว้ใน EP ก่อนในเรื่องของตัว Operator
"""
