import wmi
from datetime import datetime

remote_computer = "adcservices-3"
#remote_computer = "localhost"


c = wmi.WMI(remote_computer, user="Administrator", password="Tecom_1!")  # создание подключения к WMI на удаленном ПК
#c = wmi.WMI()

process_name = "explorer.exe"
#process_id = 1234
#processes = c.Win32_Process(Name=process_name) if process_name else c.Win32_Process(ProcessId=process_id)
processes = c.Win32_Process(Name=process_name)

# вывод информации о процессе
for process in processes:
    #print(f"Name: {process.Name}")
    print(f"PID: {process.ProcessId}")
    #print(f"CommandLine: {process.CommandLine}")
    #print(f"Description: {process.Description}")
    #print(f"ExecutablePath: {process.ExecutablePath}")
    #print(f"CreationDate: {process.CreationDate}")
    #print(f"ThreadCount: {process.ThreadCount}")
    #print(f"WorkingSetSize: {process.WorkingSetSize}")
