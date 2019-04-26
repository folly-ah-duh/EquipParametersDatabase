from tkinter import *
from DbManager import *
from EquipParameterWriter import *
import sqlite3

class DbGUI():
    """description of class"""


    def __init__(self, parent):
        self.parent = parent
        self.conn = sqlite3.connect(':memory:')
        self.db = DbManager(self.conn)
        self.db.build_database("EquipParameters.lua")
        
        self.parent.minsize(300, 200)
        self.parent.geometry("740x500")

        self.appContainer = Frame(parent)
        self.appContainer.pack(fill=BOTH, expand=YES)

        button_width = 6

        padding_dictionary = dict(padx="3m", ipadx="3m")

        self.label_frame = Frame(self.appContainer)
        self.label_frame.pack(**padding_dictionary, anchor=NW, fill=X)
        query_label = Label(self.label_frame, text = "Query:").pack(anchor=NW)

        self.query_frame = Frame(self.appContainer)
        self.query_frame.pack(**padding_dictionary, anchor=NW, fill=X)

        self.query_box = Entry(self.query_frame)
        self.query_box.bind("<Return>", self.submit_query)
        self.query_box.pack(side=LEFT, expand=YES, fill=BOTH)
        self.submit_query_button = Button(self.query_frame, width=button_width, text="Submit", command=self.submit_query)
        self.submit_query_button.pack(side=RIGHT)

        self.response_frame = Frame(self.appContainer)
        self.response_frame.pack(**padding_dictionary, pady="2m", anchor=N, expand=YES, fill=BOTH)

        self.query_response = StringVar()
        self.response_listbox = Listbox(self.response_frame, relief=RIDGE)
        self.response_listbox.pack(anchor=N, expand=YES, fill=BOTH)

        self.export_frame = Frame(self.appContainer)
        self.export_frame.pack(**padding_dictionary, anchor=S, fill=X)

        self.export_label = Label(self.export_frame, text="Export to file: ")
        self.export_label.pack(anchor=NW)

        self.destination_frame = Frame(self.export_frame)
        self.destination_frame.pack(anchor=S, fill=X)

        self.dest_box = Entry(self.destination_frame)
        self.dest_box.pack(side=LEFT, expand=YES, fill=BOTH)
        self.select_dir_button = Button(self.destination_frame, text="...", command=self.select_folder)
        self.select_dir_button.pack(side=RIGHT)

        self.export_button_frame = Frame(self.export_frame, pady="2m")
        self.export_button_frame.pack(anchor=S, fill=X)
        self.export_button = Button(self.export_button_frame, text="Export", command=self.export_file)
        self.export_button.configure(width=button_width)
        self.export_button.pack(anchor=E, expand=YES)

    def submit_query(self, event=None):
        epw = EquipParameterWriter(self.conn)
        fetched_result = self.db.query_database(self.query_box.get())
        description = self.db.get_description()

        row_str = epw.write_row(description)
        self.response_listbox.insert(0, row_str)

        for row in fetched_result:
            row_str = epw.write_row(row)
            self.response_listbox.insert(END, row_str)


    def select_folder(self):
        pass


    def export_file(self):
        print(self.dest_box.get())