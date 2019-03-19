from scipy.misc import imread
import numpy as np
import pandas as pd
import os
import random

#there are 2 datasets: Train, Test
#Each of them contains data of 58 nepali characters in 58 different folders
#folder 0 to 9 contains data of nepali digit 0 to 9 respectively
#folder 10 to 45 contains data of nepali consonanats kaa to gya respectively
#folder 46 to 57 contains data of nepali vowels aaa to aahh respectively

#root is the path to the dataset, output_file_name is the name that'd be used to save the converted csv file
def convert_to_csv(root, output_file_name):
    print("Converting datasets in: " + root)

    #counting the number of data in the dataset
    #i.e counting the number of folders in the dataset
    d_list = list() 
    try: 
        for f in os.listdir(root):             
            if os.path.isdir(os.path.join(root, f)): 
                d_list.append(f) 
    except: 
        print("\nError, once check the path")
    #d_list is the list containing the names of all folders inside the dataset
    #len(d_list) will give the no. of folders in the dataset

    no_data_trained = 0 #just to track the progress and display it in the console

    #go through each directory in the root folder given above
    for directory, subdirectories, files in os.walk(root):

        #go through each file in that directory
        for file in files:	

            #just displaying the progress in the console
            print("Converting Dataset:", end = ' ')
            filename_index_start = len(root) + 1
            #'directory' contains the whole path to this current directory
            #i.e '/home/prajwal/Desktop/github/dataset_to_csv/Test/31'
            #directory[filename_index_start:] extracts the current directory name form the 'directory' i.e 31
            print( directory[filename_index_start:], end = ' ' )
            print("Progress:", end = ' ')
            print(no_data_trained, end=' ')
            print("/", end =' ')
            print(len(d_list))

            #reading the image file and extracting its pixels
            im = imread(os.path.join(directory,file))  
            im2 = im 

            #the dataset from 46 to 57 (nepali vowels) are different from the rest
            #i.e they are 28 by 28 pixels instead of 32 by 32, and they are black in white, instead of white in black
            #so converting these data to be same as rest
            if( int(directory[filename_index_start:]) > 45 ):
                im2 = np.empty((32, 32))   
                print("This is a vowel")
                additional_zeroes = np.array([255, 255])                
                for i in range(len(im2)):
                    for j in range(len(im2[i])):
                        im2[i][j] = 255
                for i in range(len(im)):
                    im2[i+2] = np.hstack((additional_zeroes, im[i], additional_zeroes))

                for i in range(len(im2)):
                    for j in range(len(im2[i])):
                        im2[i][j] = 255 - im2[i][j]                           
            

            #flattening the array to 1D array
            value = im2.flatten()

            #value contains flattened 1D array of image data
            #adding the data name at the beginning of the value array
            value = np.hstack((directory[filename_index_start:],value))

            #converting the value into labeled dataframe
            df = pd.DataFrame(value).T #.T transposes the row and column
            df = df.sample(frac=1) # shuffle the dataset// it freaking doesnt work

            #adding the dataset to csv, naming the csv as temp.csv
            with open('temp.csv', 'a') as dataset: 
                df.to_csv(dataset, header=False, index=False)
        print()
        no_data_trained = no_data_trained + 1 #just for showing progress

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


#converting the dataset in Test dataset folder
root = './Test'
convert_to_csv(root, "test.csv")

#converting the dataset in the Train dataset folder
root = './Train'
convert_to_csv(root, "train.csv")
