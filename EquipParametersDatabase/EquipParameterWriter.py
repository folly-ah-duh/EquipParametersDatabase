from TableDictionaries import *
import sqlite3

class EquipParameterWriter():
    """writes sql database to file (sql -> lua)"""


    def __init__(self, connection):
        self.__conn = connection


    def __write_row(self, row):
        values = []

        for i in range(len(row)):
            value = row[i]

            if type(value) is str and not value.isdigit():
                if value.startswith('Tpp'):
                    values.append(value)
                else: 
                    values.append(f'"{value}"')
            else:
                values.append(str(value))

        return "{" + ",".join(values) + "}"


    def __compile_rows(self, rows, no_version):
        lua_rows = []

        for row in rows:
            if no_version:
                row = row[1:]
            
            lua_rows.append(self.__write_row(row))

        return ",".join(lua_rows)


    def __write_table(self, table_dictionary):
        table_name = table_dictionary["Name"]
        no_version = table_dictionary["Version"] == -1

        table_str = table_name + '={'

        if not no_version:
            has_version = True
            table_str += str(table_dictionary["Version"]) + ","
        
        c = self.__conn.cursor()
        c.execute("SELECT * FROM " + table_name)
        rows = c.fetchall()

        table_str += self.__compile_rows(rows, no_version) + "}"
        return table_str


    def __compile_tables(self):
        tables = []
        for table in TableDictionaries.dictionary_list:
            tables.append(self.__write_table(table))

        return ','.join(tables)


    def write_equip_parameters(self, equip_parameters_filename):
        with open(equip_parameters_filename, 'w+') as ep_writer:
            ep_writer.write("this={}TppEquip.ReloadEquipParameterTables2{" + self.__compile_tables() + "}return this")

