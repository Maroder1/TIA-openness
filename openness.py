
import clr
from System.IO import DirectoryInfo
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V15_1\PublicAPI\\V15.1\\Siemens.Engineering.dll')
from Siemens.Engineering import*
from Siemens.Engineering.HW import*

projectPath = DirectoryInfo ('C:\\Jonas\\TIA')
projectName = 'PythonTest'

#Starting TIA
print ("Starting TIA with UI")
myTia = TiaPortal(TiaPortalMode.WithUserInterface)
#Creating new project
print ("Creating project")
myProject = myTia.Projects.Create(projectPath, projectName)
#Addding Stations
print ("creating station 1")
station1MLFB = 'OrderNumber:6ES7 515-2AM01-0AB0/V2.6'
station1 = myProject.Devices.CreateWithItem(station1MLFB,'station1', 'station1')

print ("creating station 2")

station1MLFB = 'OrderNumber:6ES7 518-4AP00-0AB0/V2.6'
station1 = myProject.Devices.CreateWithItem(station1MLFB,'station2', 'station2')

print ("press any key to quit")
input()
quit()