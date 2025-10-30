import pathlib
import threading
from types import FunctionType
import webview


def run_in_new_thread(passed_function: FunctionType) -> FunctionType:
    """Run's passed function in a new thread

    I wanted to try out Python decorators, they seem cool and made the API
    classes functions cleaner.
    """
    def wrapper(*args, **kwargs):
        threading.Thread(target=passed_function, args=args, kwargs=kwargs).start()
    return wrapper

class API:
    """This is the communication bridge between js and python, it groups the functions
    we use in the frontend window so it"s easier to call python
    """
    def __init__(self):
        self.files = tuple()
        self.dir_path: str = ""

    def get_file_paths(self):
        return self.files

    def get_dir_path(self):
        return self.dir_path

    @run_in_new_thread
    def open_file_dialog(self):
        #can't have two windows at once from same thread, so thread webview dialogs
        filepaths = webview.windows[0].create_file_dialog(
            webview.FileDialog.OPEN,
            allow_multiple=True,
            file_types=("PDF File (*.pdf)", "Word Doc (*.docx)")
        )
        print(filepaths) #REMOVE
        if (filepaths != None): self.files = filepaths

    @run_in_new_thread
    def open_directory_dialog(self, get_files_from_dir=False):
        dir_path = webview.windows[0].create_file_dialog(
            webview.FileDialog.FOLDER,
        )
        print("directory choosen:", dir_path) #REMOVE
        if (dir_path != None and not get_files_from_dir): self.dir_path = dir_path[0]
        if (dir_path != None and get_files_from_dir): self.files = self.get_prb_files_from_dir(dir_path[0])
        print("Current PRB files (self.files):", self.files) #REMOVE

    def get_prb_files_from_dir(self, dir_path: str):
        dir = pathlib.Path(dir_path)
        all_pdf_files = tuple(str(file) for file in dir.iterdir() if (file.is_file() and file.suffix == ".pdf"))
        return all_pdf_files

    def generate_excel_file(self):
        #TODO implement call with files tuple and dir_path
        if (len(self.files) <= 0 and len(self.dir_path) <= 0):
            return False
        return True

    def print(self, val, identifier="JS"):
        print(f"Value from {identifier}:{val}")

if __name__ == "__main__":
    api = API()
    webview.create_window(
        title="Convert PDFs to Excel",
        url="./index.html",
        js_api=api,
        background_color="#fdf4e6",
        resizable=False
    )
    webview.start()
