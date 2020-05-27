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

class the_date:
    def __init__(self, day):
        self.day = day

class time_coord:
    def __init__(self, hour_min_sec, x, y, z):
        # an array of times pertaining to this date
        self.hour_min_sec = hour_min_sec
        self.x = x
        self.y = y
        self.z = z


class patient_data:
    def __init__(self, _id):
        self.id = _id;
        # storage by day which contains time per day
        self.date = []


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# get directory of coatsvillefiles
dir_coats = 'C:/Users/galea/OneDrive/Documents/#Summer 2020/DATA_VA/Raw Coatesville Data/'


# create storage for coatsville files


# search for patient by id raw data
def getPatientCoordsRawData(_id):
    # contains day storage for time coord
    day = []

    # first two elements signify day and time
    # last three are x y z

    file = dir_coats + 'ids/' + str(_id) + '.csv'
    # we need to store by day
    patient_date_xyz = pd.read_csv(file, usecols=[4, 5, 6, 7], header=None)
    # construct
    patient = patient_data(_id)

    # get first date EVER
    dateInUse = patient_date_xyz.iat[0, 0].split(" ", 1)
    for index, row in patient_date_xyz.iterrows():
        # split the date
        # dateInUse = patient_date_xyz.iat[index, 0].split(" ", 1)
        # check to see if the new value is not the same date
        if dateInUse != patient_date_xyz.iat[index, 0].split(" ", 1)[0]:
            # add old data into appropriate date
            patient.date.append(day)
            # clear old data
            day.clear()
            # store the new date that we are going to be working with.
            dateInUse = patient_date_xyz.iat[index, 0].split(" ", 1)[0]

        # hour/min/sec x y z
        day.append(time_coord(
            patient_date_xyz.iat[index, 0].split(" ", 1)[1],
            patient_date_xyz.iat[index, 1],
            patient_date_xyz.iat[index, 2],
            patient_date_xyz.iat[index, 3]
        ))
        print(day[0].hour_min_sec, day[0].x, day[0].y, day[0].z)
        print(day)

        # print last day as a debug test

        # print(type(index))
        # print(type(patient_date_xyz))
        # print(patient_date_xyz.iat[index,0])
        # print(type(x))
        # xArray.append(int(patient_date_xyz.iat[index, 1]))
        # print(type(xArray))
        # yArray.append(int(patient_date_xyz.iat[index, 2]))
        # zArray.append(int(patient_date_xyz.iat[index, 3]))
    # add old data into appropriate date
    print(day[0].hour_min_sec)
    patient.date.append(day)
    print(patient.date[0][0].hour_min_sec)
    # clear old data
    day.clear()
    # print(patient.date)
    return patient


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
        _id = Patient.get()
        coord = getPatientCoordsRawData(int(_id))
        # print(id)
        # print(coord)
        printout = Label(root, text=id)
        printout.grid(row=0, column=6, columnspan=1)
        # plt.scatter(coord[0], coord[1], c=coord[2])
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
Patient.insert(0, '')
Select_Patient = Button(root, text="Select Patient", command=lambda: command(5))
rewind.grid(row=1, column=0, columnspan=1)
pause.grid(row=1, column=1, columnspan=1)
play.grid(row=1, column=2, columnspan=1)
fastforward.grid(row=1, column=3, columnspan=1)
Select_Facility.grid(row=1, column=4, columnspan=1)
Patient.grid(row=1, column=5, columnspan=1)
Select_Patient.grid(row=2, column=5, columnspan=1)

root.mainloop()
