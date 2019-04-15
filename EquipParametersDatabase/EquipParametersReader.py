class EquipParametersReader:
    """Reads EquipParameters to get specific tables"""


    def __init__(self, equip_parameters_filename):
        with open(equip_parameters_filename, 'r') as ep_reader:
            self.__ep_content = str(ep_reader.read())
        self.__ep_content = ' '.join(self.__ep_content.split())


    def get_all(self):
        return self.__ep_content


    def __find_table_name(self, table_name, starting_index = 0):
        hit_index = self.__ep_content.find(table_name, starting_index)

        if hit_index > 0:
            char_before_hit = self.__ep_content[hit_index - 1]
            char_after_hit = self.__ep_content[hit_index + len(table_name)]

            if char_before_hit not in '{, ' or char_after_hit not in '= ':
                hit_index = self.__find_table_name(table_name, hit_index + 1)

        return hit_index


    def __get_table_indices(self, index_of_table_name):
        start_index = self.__ep_content.find('{', index_of_table_name)
        end_index = start_index
        bracketCount = 1

        while bracketCount != 0:
            end_index += 1
            character_at_index = self.__ep_content[end_index]

            if character_at_index == '{':
                bracketCount += 1
            elif character_at_index == '}':
                bracketCount -= 1

        return start_index, end_index


    def get_parameter_table(self, table_name):
        table_name_index = self.__find_table_name(table_name)

        if table_name_index == -1:
            return "table not found"
        
        s, e = self.__get_table_indices(table_name_index)
        return self.__ep_content[s : e]