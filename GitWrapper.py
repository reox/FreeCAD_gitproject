import git
import FreeCAD
import os

def commitchanges():
    f = FreeCAD.ActiveDocument.FileName

    try:
        repo = git.Repo(os.path.dirname(f), search_parent_directories=True)
    except git.InvalidGitRepositoryError:
        FreeCAD.Console.PrintMessage("{} is not a git repo...\n".format(os.path.dirname(f)))
        return
    except git.NoSuchPathError:
        FreeCAD.Console.PrintError("Ooops! The folder does not exist.\n")
        return

    # Add and commit the file
    index = repo.index
    index.add([f])
    index.commit("[FreeCAD autocommit]")
