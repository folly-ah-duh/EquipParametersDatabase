from TableDictionaries import *
import sqlite3

class EquipParameterWriter():
    """writes sql database to EquipParameters.lua"""


    def __init__(self, connection):
        self.conn = connection


    def write_table(self, table_dictionary):
        c = self.conn.cursor()
        table_str = table_dictionary["Name"] + "={"
        no_version = table_dictionary["Version"] == -1

        if not no_version:
            has_version = True
            table_str += str(table_dictionary["Version"]) + ","

        c.execute("SELECT * FROM " + table_dictionary["Name"])
        rows = c.fetchall()
        lua_rows = []

        for row in rows:
            if no_version:
                row = row[1:]
            
            values = []
            row_str = "{"
            for i in range(len(row)):
                value = row[i]

                if type(value) is str and not value.isdigit():
                    if value.startswith('Tpp'):
                        values.append(value)
                    else: 
                        values.append(f'"{value}"')
                else:
                    values.append(str(value))

            row_str += ",".join(values) + "}"
            lua_rows.append(row_str)

        table_str += ",".join(lua_rows) + "}"
        return table_str


    def compile_tables(self):
        tables = []
        for table in TableDictionaries.dictionary_list:
            tables.append(self.write_table(table))

        return ','.join(tables)


    def write_equip_parameters(self, equip_parameters_filename):
        with open(equip_parameters_filename, 'w+') as ep_writer:
            ep_writer.write("this={}TppEquip.ReloadEquipParameterTables2{" + self.compile_tables() + "}return this")

