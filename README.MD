#To make the setup work on your system

#Step 1: Install Python venv module (if not installed)
    #sudo apt install python3-venv

#Step 2: Create a Virtual Environment
   #Go to the folder where setup.py is located (your dnslookup folder). Then, create a virtual environment:
    python3 -m venv myenv

#Step 3: Activate the Virtual Environment
  #Activate the virtual environment with the following command:
    source myenv/bin/activate

#Step 4: Install dnspython
    python3 setup.py

#Step 5: Running the Script
    python3 dns_lookup.py

#Step 6: Deactivating the Virtual Environment
When you're done, you can deactivate the virtual environment using:
deactivate
