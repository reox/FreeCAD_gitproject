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

    def __init__(self):
        # Monkey patch the save function, so we can hook it
        z = Gui.SendMsgToActiveView

        from GitWrapper import commitchanges
        def hookedSaveFunction(*args, **kwargs):
            res = z(*args, **kwargs)

            # We like to hook after the save was done
            if "Save" in args:
                Msg("save pressed\n")
                commitchanges()


            return res

        Gui.SendMsgToActiveView = hookedSaveFunction

    def Initialize(self):
        pass

    def GetClassName(self):
        return "Gui::GitProjectWorkbench"

Gui.addWorkbench(GitProjectWorkbench())
