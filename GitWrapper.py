import git
import FreeCAD
import os
if FreeCAD.GuiUp:
    import FreeCADGui

def commitchanges():
    """
    Commit the changes of the current active file
    """
    f = FreeCAD.ActiveDocument.FileName
    if len(f) == 0:
        # Not saved yet...
        return

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


class CommandCommit:
    """
    Command to commit the current file
    """

    def GetResources(self):
        return {'Pixmap': os.path.join(os.path.dirname(__file__),"icons",'git-commit.svg'),
                'MenuText': "Commit",
                'ToolTip': 'Commit the current file in git',
                }

    def Activated(self):
        commitchanges()


class CommandTag:
    """
    Command to create a new tag
    """

    def GetResources(self):
        return {'Pixmap': os.path.join(os.path.dirname(__file__),"icons",'tag.svg'),
                'MenuText': "Tag",
                'ToolTip': 'Tag the current commit',
                }

    def Activated(self):
        pass


class CommandCreate:
    """
    Init a new git repo in the current folder
    """

    def GetResources(self):
        return {'Pixmap': os.path.join(os.path.dirname(__file__),"icons",'git.svg'),
                'MenuText': "Init",
                'ToolTip': 'Initialize a new git repository',
                }

    def Activated(self):
        pass


if FreeCAD.GuiUp:
    FreeCADGui.addCommand('GitProject_CommandCommit',CommandCommit())
    FreeCADGui.addCommand('GitProject_CommandTag',CommandTag())
    FreeCADGui.addCommand('GitProject_CommandCreate',CommandCreate())
