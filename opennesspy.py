
import clr
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V15_1\PublicAPI\\V15.1\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo
import Siemens.Engineering as tia


project_path = DirectoryInfo ('C:\\Jonas\\TIA')
project_name = 'PythonTest'

#Starting TIA
print ('Starting TIA with UI')
mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)

#Creating new project
print ('Creating project')
myproject = mytia.Projects.Create(project_path, project_name)

#Addding Stations
print ('Creating station 1')
station1_mlfb = 'OrderNumber:6ES7 515-2AM01-0AB0/V2.6'
station1 = myproject.Devices.CreateWithItem(station1_mlfb, 'station1', 'station1')

print ('Creating station 2')
station2_mlfb = 'OrderNumber:6ES7 518-4AP00-0AB0/V2.6'
station2 = myproject.Devices.CreateWithItem(station2_mlfb, 'station2', 'station2')

print ("Press any key to quit")
input()
quit()
