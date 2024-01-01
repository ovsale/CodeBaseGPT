class FileNode:
    def __init__(self, name: str, is_folder: bool, folder_content: list, size: int):
        self.name = name
        self.is_folder = is_folder
        self.folder_content = folder_content
        self.size = size

    def __repr__(self):
        return f'FileNode(name={self.name}, is_folder={self.is_folder}, folder_content={self.folder_content}, size={self.size})'