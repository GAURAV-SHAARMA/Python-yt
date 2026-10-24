# virtual enviroment is used toisolate a particualr python enviroment on a single machine , allowing  you to work on a multiple projects with different dependencies and packageswithout conflits

#useful when packages are incomapatible with each other


#create a virtual enviroment
# >>>>python -m venv  myenv


#activate the virtual enviroment
# >>>>>myenv\Scripts\activate


#to deactivate enviroment
#>>> deactivate

import pandas as pd
pd.__version__

# if we want to create a vE for a particular package like pandas(1-5)

#>>>>>>>>>>> python -m venv  myenvpython -m venv  myenv pandas1-5



# no some files->>>>
# "requirements.txt"

# output the list of packages
#>>>>>>>> pip freeze > requirements.txt

#install the packages listed in requirements.txt
#>> pip install -r requirements.txt