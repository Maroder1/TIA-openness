## Basic example on how to use openness with Python using Pythonnet

**Installation of TIA Openness**

 1. Install TIA v15.1 professional, make sure openness is checked [default]
	[Link to TIA v15.1 trail](https://support.industry.siemens.com/cs/ww/en/view/109761045)
 2. Right clik "My computer" -> Manage -> System tools -> Local users and groups - > Groups-> Double click "Siemens TIA Openness and add your username
 3. Edit the file path in the example file to match your installation of Siemens.Engineering.dll
 4. [Download and install Python](www.python.org)


**Option 1, running directly (not recommended)**

 1. in the windows search bar type "command prompt" to open Command Promt (CMD)
 2. Install pythonnet by typing: *pip install pythonnet*
 3. Browse to the location of the example file and type: *Python opennesspy.py*


**Option 2, running in a Virtual environment(in this example using Miniconda (Anaconda))**

 1. [Download Miniconda](https://docs.conda.io/en/latest/miniconda.html)
 2. Open Command Prompt (CMD)
 3. Create a new environment by typing: *conda create --name opennesspy python=3.7*
 4. Actiavte the environment: *conda activate opennesspy*
 5. Install pythonnet by typing: *pip install pythonnet*  Note: installing using *conda install* didnt work.
 6. Browse to the location of the example file and type: *Python opennesspy.py*
 7. To leave the environment type *conda deactiave opennesspy*
 
 Optional: instead of manually installing use the provided environment.yml file
 
 
 
