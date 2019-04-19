from TableBuilder import TableBuilder
from EquipParameterWriter import EquipParameterWriter
import sqlite3

conn = sqlite3.connect(':memory:')
tb = TableBuilder(conn)
tb.build_database("EquipParameters.lua")

epw = EquipParameterWriter(conn)
epw.write_equip_parameters("test.lua")