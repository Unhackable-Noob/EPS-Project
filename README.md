# EPS-Project - detailed readme is the pdf file with images

**References:**

**1. OpenMined Documentation - PySyft example on Breast Cancer study:** https://docs.openmined.org/en/latest/getting-started/introduction.html


**Dependency/Module installations:**

_Install Jupyter Notebook and create a folder_

_Install Pysyft, pandas, numpy and sklearn libraries/modules using pip as below:_

pip install syft

pip install pandas

pip install numpy

pip install sklearn


**When running the Jupyter Notebook:**

_Restart kernel before running_

_Run one cell at a time and not all together as there are some initialization/configuration cells that have to be run only once, skip the next times you run the code again_

**Cell 5:** Creating an admin account for each local site using default credentials
_Run this cell just once initially_

**Cell 7:** Change the account credentials to make the site more secure
_Run this cell too just once, skip the next time you run the code again_

**Cells 17 and 19: **Change the path that accesses the user dataset csv files as per your system before running

**Cell 99 **- Creating projects
Run this cell once for initializing the projects and only when you run the code from scratch.
Other times, access the project using the below code snippets:
_fitcheck_project1 = global_client1.projects[0]
fitcheck_project2 = global_client2.projects[0]_

**Cell 111: **Creating code requests
_Run this cell only once,_ unless you have restarted a Jupyter notebook and run the code from scratch. Otherwise skip. 
Running this multiple times creates multiple code requests which hinders sharing the results with the global model due to approval status:Pending.


Everything else has to be run._
_
_If any errors occur especially when running cells with client initialization or database uploads, shut down and restart Jupyter Notebook and run the code from scratch._

