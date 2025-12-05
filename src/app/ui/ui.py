import pathlib
import webview
from main import generate_from_root, generate_from_group

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

    def open_group_dialog(self):
        filepaths = webview.windows[0].create_file_dialog(
            webview.FileDialog.FOLDER,
        )
        print(filepaths) #REMOVE
        if (filepaths != None): self.files = filepaths[0]
        return self.files

    def open_root_dialog(self, get_files_from_dir=False):
        dir_path = webview.windows[0].create_file_dialog(
            webview.FileDialog.FOLDER,
        )
        print("directory choosen:", dir_path) #REMOVE
        if (dir_path != None): self.files = dir_path[0]
        return self.files

    def get_prb_groups_from_dir(self, dir_path: str):
        #TODO - correct pathing to get groups for list
        #dir = pathlib.Path(dir_path)
        #all_pdf_files = tuple(str(file) for file in dir.iterdir() if (file.is_file() and file.suffix == ".pdf"))
        all_pdf_files = tuple(["Group1", "Group2", "Group3"])
        return all_pdf_files

    def generate_excel_file(self, rootFolder: bool):
        print("generate")

        print(f"self.files: typeof-{type(self.files)}, str(val)-{str(self.files)}")

        if (rootFolder):
            generate_from_root(self.files)
        else:
            generate_from_group(self.files)

        print("done")

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
        resizable=True,
    )
    webview.start()
