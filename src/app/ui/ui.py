import pathlib
import webbrowser
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
        return_res = list()
        if (dir_path != None):
            self.files = dir_path[0]
            return_res = [str(x) for x in pathlib.Path(self.files).iterdir() if x.is_dir()]
        return return_res;

    def generate_excel_file(self, rootFolder: bool):
        print("generate")

        print(f"self.files: typeof-{type(self.files)}, str(val)-{str(self.files)}")

        if (rootFolder):
            generate_from_root(str(self.files))
        else:
            generate_from_group(str(self.files))

        print("done")

        #TODO implement call with files tuple and dir_path
        if (len(self.files) <= 0 and len(self.dir_path) <= 0):
            return False
        return True

    def print(self, val, identifier="JS"):
        print(f"Value from {identifier}:{val}")

    # Open the github wiki in the default browser
    def openGithubWiki(self):
        webbrowser.open_new("https://github.com/RealGenius1/Data-Buccaneers/wiki")

if __name__ == "__main__":
    api = API()
    webview.create_window(
        title="Convert PDFs to Excel",
        url="./index.html",
        js_api=api,
        background_color="#fdf4e6",
        resizable=False,
    )
    webview.start()
