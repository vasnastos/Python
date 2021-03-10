import session_teams as ses
"""
from PyQt5.QtWidgets import QApplication
def Run_Gui():
    a=QApplication([])
    win=w.window()
    win.show()
    a.exec()
"""

if __name__=='__main__':
    timelimit = input('Give Lesson Participation time Limit(minutes):')
    teams=ses.msteams(timelimit)
    teams.OpenFile('lab_source.csv')
    teams.Connections()
    teams.meeting_details()
    teams.meeting_time_hold_per_person()
    teams.Export_Participation_List()


