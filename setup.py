from Project import app
from Project import Project_Gdrive
# from Project.RichMenu import *

def run():
    Project_Gdrive('DISENO001')
    app.run(port = 80)

if __name__ == '__main__':

    run()
