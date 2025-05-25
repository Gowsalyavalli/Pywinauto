from pywinauto import application
from timings import Timings

#acts as implicit wait .Delay timing of script execution 2 times faster or slower
#Timings.defaults()
Timings.slow() # double all timings (~2x slower script execution)
#Timings.fast() 

app=application.Application().start("notepad.exe")
#Windows specification: we can specify the window in 2 ways 
#Windows Specification is an object that describes either the application window or the control element.
#1.main_dlg=app.UntitledNotepad
#(saveas_dialog=app.SaveAs)
#2.main_dlg = app.window(title='Untitled - Notepad')

main_dlg = app.window(title='Untitled - Notepad')
main_dlg.wait('visible')
main_dlg.print_control_identifiers()


#enter keys 
main_dlg.Edit.type_keys("notepad started ")
#select menu dropdown save as under file
main_dlg = app.window(title='*Untitled - Notepad')
main_dlg.menu_select("File->Save As")
saveas_dialog=app.window(title='Save As')
saveas_dialog.wait('visible')
saveas_dialog.print_control_identifiers()



#In saveas window select dropdown item
print(saveas_dialog.ComboBox2.selected_text())
saveas_dialog.ComboBox3.select("ANSI")


#In saveas window set text
#saveas_dialog.edit1.set_text("Example-utf8.txt")

#click save button
saveas_dialog.Save.click()



