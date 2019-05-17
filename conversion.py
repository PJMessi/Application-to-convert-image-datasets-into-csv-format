from scipy.misc import imread
import numpy as np
import pandas as pd
import os
import random
from tqdm import tqdm


#root is the path to the dataset, output_file_name is the name that'd be used to save the converted csv file
def convert_to_csv(root, output_file_name):
    print("\nConverting datasets in: " + root + "\n")

    #counting the number of classes in the dataset i.e counting the number of folders in the dataset
    no_of_classes = 0
    try: 
        for f in os.listdir(root):             
            if os.path.isdir(os.path.join(root, f)): 
                no_of_classes += 1
    except: 
        print("\nError, Invalid Path")
   
    filename_index_start = len(root) + 1 #look at line no 30 to 33

    #go through each directory in the root folder given above
    x = os.walk(root)
    next(x) #skipping first iteration, as its the default folder
    current_class = 1
    for directory, subdirectories, files in x:
        
        #'directory' contains the whole path to this current directory
        #i.e '/home/prajwal/Desktop/github/dataset_to_csv/Test/31'
        #directory[filename_index_start:] extracts the current directory name form the 'directory' i.e 31
        
        print("Class: " + str(current_class) + "/" + str(no_of_classes))
        #go through each file in that directory

        for file in tqdm(files):	
            
            #reading the image file and extracting its pixels
            im = imread(os.path.join(directory,file))  

            #flattening the array to 1D array
            value = im.flatten()

            #value contains flattened 1D array of image data
            #adding the data name at the beginning of the value array
            value = np.hstack((directory[filename_index_start:],value))

            #converting the value into labeled dataframe
            df = pd.DataFrame(value).T #.T transposes the row and column
            df = df.sample(frac=1) # shuffle the dataset// it freaking doesnt work

            #adding the dataset to csv, naming the csv as temp.csv
            with open('temp.csv', 'a') as dataset: 
                df.to_csv(dataset, header=False, index=False)
        
        current_class += 1

    #for shuffling the datas in the temp.csv
    print("shuffling dataset")
    with open('temp.csv', 'r') as r, open(output_file_name, 'w') as w: #saving the shuffled temp.csv as the output_file_name
        data = r.readlines()
        header, rows = data[0], data[1:]
        random.shuffle(rows)
        rows = '\n'.join([row.strip() for row in rows])
        w.write(header + rows)
        print("Removing temporary file")
        
    os.remove('temp.csv') #removing the temp.csv
    print("Successfully converted datasets in '" + root + "' to " + output_file_name)

root = './Data'
convert_to_csv(root, "converted_datasets.csv")