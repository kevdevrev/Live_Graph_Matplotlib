
import numpy as np
import pandas as pd


import csv
import re
#handling loading of files
import fileinput
import glob
import sys

import os.path
from os import path

from collections import namedtuple

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# get directory of coatsvillefiles
dir_coats = 'C:/Users/galea/OneDrive/Documents/#Summer 2020/DATA_VA/Raw Coatesville Data/'
# create storage for coatsville files
patients_coats = []
# load coatsville patient id, x,y,z into memory

patient_ids_unique = [20708, 23001, 24801, 20000, 20580, 11090, 10101, 22230, 21077, 20058, 20604, 10110]
# this here loads all the files into memory per facility
num_files = 0
for file in glob.glob(dir_coats + '*.csv'):
    # add each day to the day coats[]
    num_files = num_files + 1
    patient_by_id = pd.read_csv(file, header=None)
    # print(patient_idxyz)
    # add the raw files to day_coats (file array)
    patients_coats.append(patient_by_id)


# print(patients_coats)

# def getUniqueIds():
    # get all ids and add to a list



def patientFileCreator(_id):
    # print("in function")
    filename = dir_coats + 'ids/' + str(_id) + '.csv'
    print("doing ID number: " + str(_id))
    tempPatient = []
    tempPatientDataframe = pd.DataFrame()

    # iterate throughout all files now stored in memory
    for index, item in enumerate(patients_coats):
        print("reviewing file #: " + str(index) + " out of " + str(num_files))
        # tempPatient.clear()
        # create an dataframe consisting of just the ids (probably not needed but works)
        # parsedIdDataframe = pd.DataFrame(patients_coats[index], columns=[1])
        # print(parsedIdDataframe)
        # iterate all the rows of every file to find every instance of this ID
        # print(type(patients_coats[index]))
        for jndex, row in patients_coats[index].iterrows():
            # row now gives me the value i need.
            # print(row)
            # print(index)
            # print(jndex)
            # parse currently looking at id

            # print(id)
            #print(str(id_being_checked) + ' ' + str(_id))
            #print(id_being_checked == _id)

            if int(patients_coats[index].iloc[jndex, 1]) == _id:
                if(path.isfile(filename)):
                    tempPatient.append(patients_coats[index].iloc[[jndex]])
                    #free some memory by writing to file
                    if (sys.getsizeof(tempPatient) > 8000000):
                        #concatinate all the list into a dataframe
                        tempPatientDataframe = pd.concat(tempPatient)
                        tempPatientDataframe.to_csv(filename, mode = 'a', header=False, index=False)
                        #clear the dataframe
                        tempPatientDataframe.drop(tempPatientDataframe.index, inplace=True)
                        print("size of dataframe: " + str(sys.getsizeof(tempPatientDataframe)))
                        #clear the list
                        tempPatient.clear()
                        print("size of list: " + str(sys.getsizeof(tempPatient)))

                else:
                    #should occur on the first find of the id in the fileset and execute once
                    tempPatient.append(patients_coats[index].iloc[[jndex]])
                    tempPatientDataframe = pd.concat(tempPatient)
                    tempPatientDataframe.to_csv(filename, header=False, index=False)

                # now we want to append it to the file named after patient (to dataframe type)
                # print("match")
            #    print("the id raw")
             # #  print(id_being_checked)
               # print("the iloc")
                #print(patients_coats[index].iloc[jndex, 1])


            # print(tempPatient)
            # x = patients_coats[index].iloc[jndex, 1]
            # y = patients_coats[index].iloc[jndex, 2]
            # z = patients_coats[index].iloc[jndex, 3]
            # array of touples xyz
            # returnStr = str(x) + " " + str(y) + " " + str(z)
            # print(id, x, y, z)
            # print("ooof")
            # xArray.append(x)
            # yArray.append(y)
            # zArray.append(z)
    # print(tempPatient)
    # tempPatientDataframe = pd.concat(tempPatient)
    return


def createAllPatientFiles():
    print(patient_ids_unique)
    for _id in patient_ids_unique:
        patientFileCreator(_id)


#patient_ids_unique = getUniqueIds()
createAllPatientFiles()
# patientFileCreator(20708)

print("done")
