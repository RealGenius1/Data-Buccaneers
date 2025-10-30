import threading
import webview

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

    def open_file_dialog(self):
        #can't have two widnows at once from same thread, so thread webview dialogs
        def _open_file_dialog():
            filepaths = webview.windows[0].create_file_dialog(
                webview.FileDialog.OPEN,
                allow_multiple=True,
                file_types=("PDF File (*.pdf)", "Word Doc (*.docx)")
            )
            print(filepaths) #REMOVE
            if (filepaths != None): self.files = filepaths
        threading.Thread(target=_open_file_dialog).start()

    def open_directory_dialog(self):
        def _open_directory_dialog():
            dir_path = webview.windows[0].create_file_dialog(
                webview.FileDialog.FOLDER,
            )
            print(dir_path) #REMOVE
            if (dir_path != None): self.dir_path = dir_path[0]
        threading.Thread(target=_open_directory_dialog).start()

    def print(self, val, identifier):
        print(f"Value from {identifier}:{val}")

if __name__ == "__main__":
    api = API()
    webview.create_window(
        title="Hello world",
        url="./index.html",
        js_api=api,
    )
    webview.start()
