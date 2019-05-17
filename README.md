# Convert-dataset-to-CSV

## Required Libraries:
1. Scipy *$pip install scipy*
2. Pandas *$pip install pandas*
3. Numpy *pip install numpy*   
   
I'm using the datasets in 'Data.zip' and convert them into csv.   
   
'Data.zip' contains 46 folders. Each folder represents a Nepali character. Folder '0' to Folder '9' contains datasets for Nepali digits. Folder '10' to Folder '45' contains datasets for Nepali Letters. Each folder contains about 1700 datasets.   
   
The label for each of those datasets will be their corresponding parent folder name.   
   
In order to use your own datasets, give its path in 'root' variable in line 72   
   
Run 'conversion.py' to see the results.