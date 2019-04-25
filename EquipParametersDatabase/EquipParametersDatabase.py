from TableBuilder import TableBuilder
from EquipParameterWriter import EquipParameterWriter
from DbGUI import DbGUI
from tkinter import *
import sqlite3

#conn = sqlite3.connect(':memory:')
#tb = TableBuilder(conn)
#tb.build_database("EquipParameters.lua")

root = Tk()
programGUI = DbGUI(root)
root.mainloop()

#epw = EquipParameterWriter(conn)
#epw.write_equip_parameters("test.lua")