from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
# handling loading of files
import fileinput
import glob
import sys
from collections import namedtuple

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# create Patient Tuple for graphing
Patient = namedtuple('Patient', ['id', 'x', 'y', 'z'])
# get directory of coatsvillefiles
dir_coats = 'C:/Users/galea/OneDrive/Documents/#Summer 2020/DATA_VA/Raw Coatesville Data/'
# create storage for coatsville files
patients_coats = []

# load coatsville patient id, x,y,z into memory
# for file in glob.glob(dir_coats + '*.csv'):
# print(file)
# add each day to the day coats[]
# patient_idxyz = pd.read_csv(file, usecols=[1, 5, 6, 7], header=None)
# print(patient_idxyz)
# add the raw files to day_coats (file array)
#   patients_coats.append(patient_idxyz)
#  print(patients_coats)


# search for patient (add in return tuple)
def getPatientCoords(_id):
    xArray = []
    yArray = []
    zArray = []
    coord = []
    file = dir_coats + 'ids/' + str(_id) + '.csv'
    patient_xyz = pd.read_csv(file, usecols=[5, 6, 7], header=None)
    for index, row in patient_xyz.iterrows():
        # print(type(index))
        # print(type(patient_xyz))
        # print(patient_xyz.iat[index,0])
        # print(type(x))
        xArray.append(int(patient_xyz.iat[index, 0]))
        # print(type(xArray))
        yArray.append(int(patient_xyz.iat[index, 1]))
        zArray.append(int(patient_xyz.iat[index, 2]))
    coord.append(xArray)
    coord.append(yArray)
    coord.append(zArray)
    return coord


root = Tk()
root.title('Prototype')

root.iconbitmap('C:/Users/galea/OneDrive/Documents/#Summer 2020/UI/Data/IMGS/joe.ico')
root.geometry("1000x1000")

coatsville_image = ImageTk.PhotoImage(
    Image.open('C:/Users/galea/OneDrive/Documents/#Summer 2020/UI/Data/IMGS/coatsville_blueprint.png'))
coatsville_blueprint = Label(image=coatsville_image)
coatsville_blueprint.grid(row=0, column=0, columnspan=5)


def command(call):
    if call == 5:
        id = Patient.get()
        coord = getPatientCoords(int(id))
        # print(id)
        print(coord)
        printout = Label(root, text=id)
        printout.grid(row=0, column=6, columnspan=1)
        plt.scatter(coord[0], coord[1], c=coord[2])
        plt.gray()
        plt.show()
        return


clicked = StringVar()
clicked.set("Coatsville")

rewind = Button(root, text="<<", command=lambda: command(0))
pause = Button(root, text="Pause", command=lambda: command(1))
play = Button(root, text="Play", command=lambda: command(2))
fastforward = Button(root, text=">>", command=lambda: command(3))
Select_Facility = OptionMenu(root, clicked, "Coatsville", "Philadelphia", "SEARCHING")
Patient = Entry(root)
Patient.insert(0, "Enter Patient Number")
Select_Patient = Button(root, text="Select Patient", command=lambda: command(5))
rewind.grid(row=1, column=0, columnspan=1)
pause.grid(row=1, column=1, columnspan=1)
play.grid(row=1, column=2, columnspan=1)
fastforward.grid(row=1, column=3, columnspan=1)
Select_Facility.grid(row=1, column=4, columnspan=1)
Patient.grid(row=1, column=5, columnspan=1)
Select_Patient.grid(row=2, column=5, columnspan=1)

root.mainloop()
