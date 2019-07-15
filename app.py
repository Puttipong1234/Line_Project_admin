from Project import app
from Project import Project_Gdrive
# from Project.RichMenu import *
if __name__ == '__main__':

    # print(create_mainmenu())
    # print(create_submenu())
    # print(create_adminmenu())

    ###SETUP DIRECTORY

    Project_Gdrive('DISENO001')


    app.run(port = 80)
    

    

### RichMenu สามารถเชื่อมต่อกันได้เต็ใรูปแบบ
### Next : สร้าง แต่ละ Menu (Fucntion)


#### introduction 
### เมื่อทำการ run python app.py ตัวแอพจะทำการสร้าง 
# 1. database จาก Gdrive_Config เปลี่ยน directory เป็น Ture สร้าง project_name.sqlite3
# 2. Gdrive จะสร้าง directory ตามที่ได้ระบุไว้ใน Privatefolder / PublicFolder โดยมีหมวดหมู่คือ ar st mep และ etc.
# 3. แอพจะทำการาเก็บ ข้อมูลของ folder ไว้ใน sqlite3 tabase อัตโนมัต 
# 4. กรณีที่ เรียกตัว object instance Gdrive ออกมาหากไฟล์ credentials.txt ยังไม่มีข้อมูลของ user 
# 5. จำเป็นจะต้องทำการ authenthicate ครั้งแรก เพื่อให้ API สามารถเชื่อมต่อกับ drive ได้
# 6. ตรวจสอบไฟล์ SETTING.YAML