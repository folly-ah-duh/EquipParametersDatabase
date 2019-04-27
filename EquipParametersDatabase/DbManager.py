import sqlite3
from TableDictionaries import TableDictionaries
from EquipParametersReader import EquipParametersReader

class DbManager():
    """writes lua tables to database (lua -> sql)"""


    def __init__(self, connection):
        self.__conn = connection
        self.__c = self.__conn.cursor()

    def __create_tables(self):
        with self.__conn:
            for dict in TableDictionaries.dictionary_list:
                self.__c.execute(dict["CREATE"])

    def __parse_lua_data(self, lua_file):
        epr = EquipParametersReader(lua_file)

        with self.__conn:
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
                    self.__c.execute(sql_insert)
            self.__conn.commit()


    def build_database(self, equip_parameters_filename):
        self.__create_tables()
        self.__parse_lua_data(equip_parameters_filename)


    def query_database(self, query):
        self.__c.execute(query)
        return self.__c.fetchall()


    def get_description(self):
        column_names = []
        for name_col in self.__c.description:
            column_names.append(name_col[0])
        return column_names