import customtkinter as ctk
import tkinter.filedialog as tkfd

class TopBarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class ButtonRowFrame(ctk.CTkFrame):
    def __init__(self, master, get_files_func, destination_files_func, run_program_func):
        super().__init__(master)

        self.grid_columnconfigure([0,1,2], weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.add_files_button = ctk.CTkButton(self, text="Select Input Files", command=get_files_func)
        self.add_files_button.grid(row=0, column=0, padx=10, sticky="wne")

        self.add_files_button = ctk.CTkButton(self, text="Select Destination", command=destination_files_func)
        self.add_files_button.grid(row=0, column=1, padx=10, sticky="wne")

        self.add_files_button = ctk.CTkButton(self, text="Run Program", command=run_program_func)
        self.add_files_button.grid(row=0, column=2, padx=10, sticky="wne")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scan PBR into Documents (UI IN DEV)")
        self.geometry("600x400")
        self.focus_force()
        self.grid_columnconfigure(0, weight=1) #use this to make widgets stretch
        self.grid_rowconfigure(1, weight=1)

        self.bind("<Escape>", lambda event: self.quit_app())

        self.top_bar = TopBarFrame(self)
        self.top_bar.grid(row=0, column=0, sticky="wne")

        self.button_row = ButtonRowFrame(self, self.get_files_func, self.destination_files_func, self.run_program_func)
        self.button_row.grid(row=1, column=0, sticky="nesw")

    def quit_app(self):
        self.destroy()

    def get_files_func(self):
        print("get files clicked") #REMOVE
        filepaths = tkfd.askopenfilenames(
            title="Choose pdf files to aggregate",
            filetypes=[("PDF File", "*.pdf"), ("Word Doc", "*.docx")],
            initialdir=None
        )
        print(filepaths) #REMOVE
        self.focus_force()

    def destination_files_func(self):
        print("destination files clicked") #REMOVE
        save_path = tkfd.askdirectory(
            initialdir=None,
            mustexist=True,
            parent=None,
            title="Destination to save files to"
        )
        print(save_path) #REMOVE
        self.focus_force()

    def run_program_func(self):
        print("run program clicked") #REMOVE

#this only runs if this file is directly ran, not imported
if __name__ == "__main__":
    app = App()
    app.mainloop()

