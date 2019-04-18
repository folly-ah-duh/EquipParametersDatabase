import sqlite3
from TableDictionaries import TableDictionaries
from EquipParametersReader import EquipParametersReader

class TableBuilder():
    """"""
    def __init__(self, connection):
        self.conn = connection
        self.c = self.conn.cursor()

    def create_tables(self):
        with self.conn:
            for dict in TableDictionaries.dictionary_list:
                self.c.execute(dict["CREATE"])

    def parse_lua_data(self, lua_file):
        epr = EquipParametersReader(lua_file)

        with self.conn:
            for dict in TableDictionaries.dictionary_list:
                table_content = epr.get_parameter_table(dict["Name"])
                no_version = dict["Version"] == -1
                entry_index = 0

                start_index = 1
                while True:
                    start_index = table_content.find('{', start_index) + 1
                    end_index = table_content.find('}', start_index)

                    if start_index == 0: break

                    data_entry = table_content[start_index : end_index].split(',')
                    for i in range(len(data_entry)):
                        if data_entry[i].startswith("Tpp"):
                            data_entry[i] = (f'"{data_entry[i]}"')

                    if no_version:
                        data_entry.insert(0, str(entry_index))
                        entry_index += 1

                    sql_insert = (f"INSERT INTO {dict['Name']} VALUES({', '.join(data_entry)})")
                    #print(sql_insert)
                    self.c.execute(sql_insert)
            self.conn.commit()