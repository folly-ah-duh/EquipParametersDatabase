from tkinter import *

class DbGUI():
    """description of class"""


    def __init__(self, parent):
        self.parent = parent
        
        self.parent.minsize(300, 200)
        self.parent.geometry("640x400")

        self.appContainer = Frame(parent)
        self.appContainer.pack(fill=BOTH, expand=YES)

        button_width = 6

        button_padx = "2m"
        button_pady = "1m"

        padding_dictionary = dict(padx="3m", ipadx="3m")

        self.label_frame = Frame(self.appContainer)
        self.label_frame.pack(**padding_dictionary, anchor=NW, fill=X)
        query_label = Label(self.label_frame, text = "Query:").pack(anchor=NW)

        self.query_frame = Frame(self.appContainer)
        self.query_frame.pack(**padding_dictionary, anchor=NW, fill=X)

        self.user_query = StringVar()
        self.query_box = Entry(self.query_frame, textvariable = self.user_query)
        self.query_box.pack(side=LEFT, expand=YES, fill=BOTH)
        self.submit_query_button = Button(self.query_frame, width=button_width, text="Submit", command=self.submit_query)
        self.submit_query_button.pack(side=RIGHT)

        self.response_frame = Frame(self.appContainer)
        self.response_frame.pack(**padding_dictionary, anchor=N, expand=YES, fill=BOTH)

        self.query_response = StringVar()
        self.response_message = Message(self.response_frame, relief=RIDGE, textvariable = self.query_response)
        self.response_message.pack(anchor=N, expand=YES, fill=BOTH)

        self.destination_frame = Frame(self.appContainer)
        self.destination_frame.pack(**padding_dictionary, anchor=S, fill=X)

        self.dest_dir = StringVar()
        self.dest_box = Entry(self.destination_frame, textvariable = self.dest_dir)
        self.dest_box.pack(side=LEFT, expand=YES, fill=BOTH)
        self.select_dir_button = Button(self.destination_frame, text="...", command=self.submit_query)
        self.select_dir_button.pack(side=RIGHT)

        self.export_button_frame = Frame(self.appContainer)
        self.export_button_frame.pack(**padding_dictionary, anchor=S, fill=X)
        self.export_button = Button(self.export_button_frame, text="Export", command=self.export_file)
        self.export_button.configure(width=button_width)
        self.export_button.pack(anchor=E, expand=YES)

    def submit_query(self):
        self.query_response.set("I miss .NET " * 100)

    def export_file(self):
        print(self.user_query.get())