import ReadData

#Test Opener
#filename='test.csv'
filename='source.csv'
teamsobject=ReadData.teams()
teamsobject.Open_Csv(filename)
teamsobject.show_participants()