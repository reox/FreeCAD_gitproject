# (c) Sebastian Bachmann <hello@reox.at>, 2017

class GitProjectWorkbench (Workbench):
    """
    Git Project Workbench

    """
    MenuText = "git project"
    ToolTip = "git project workbench"
    Icon = '''
/* XPM */
static char * git_xpm[] = {
"16 16 2 1",
" 	c None",
"!	c #F05033",
"       !!       ",
"      !!!!      ",
"       !!!!     ",
"    !!  !!!!    ",
"   !!!!  !!!!   ",
"  !!!!!   !!!!  ",
" !!!!!!!   !!!! ",
"!!!!!!!! !  !!!!",
"!!!!!!!! !  !!!!",
" !!!!!!! !!!!!! ",
"  !!!!!  !!!!!  ",
"   !!!!  !!!!   ",
"    !!!! !!!    ",
"     !!!!!!     ",
"      !!!!      ",
"       !!       "};
    '''

    def Initialize(self):
        pass

    def GetClassName(self):
        return "Gui::GitProjectWorkbench"

Gui.addWorkbench(GitProjectWorkbench())
