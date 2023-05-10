import wmi
from datetime import datetime

time1 = datetime.now()
process_name = "ADC1000NT.exe"
remote_computers = ['adc-ctc01.tecomgroup.ru','adc-ctc02.tecomgroup.ru','adc-ctc03.tecomgroup.ru','adc-ctc04.tecomgroup.ru','adc-ctc05.tecomgroup.ru','adc-ctc06.tecomgroup.ru','adc-ctc07.tecomgroup.ru','adc-ctc08.tecomgroup.ru','adc-ctc09.tecomgroup.ru','adc-ctc10.tecomgroup.ru','adc-ctc11.tecomgroup.ru','adc-ctc12.tecomgroup.ru','adc-ctc13.tecomgroup.ru','adc-ctc14.tecomgroup.ru','adc-ctc15.tecomgroup.ru','adc-ctc16.tecomgroup.ru','adc-ctc17.tecomgroup.ru','adc-ctc18.tecomgroup.ru','adc-ctc19.tecomgroup.ru','adc-ctc20.tecomgroup.ru','adc-ctc21.tecomgroup.ru','adc-ctc22.tecomgroup.ru','adc-ctc23.tecomgroup.ru','adc-ctc24.tecomgroup.ru']

c = wmi.WMI(remote_computers, user="Administrator", password="Tecom_1!")  # создание подключения к WMI на удаленном ПК
#c = wmi.WMI()

processes = c.Win32_Process(Name=process_name)

# вывод информации о процессе
for process in processes:
    #print(process)
    #print(f"Name: {process.Name}")
    print(f"PID: {process.ProcessId}")
    #print(f"CommandLine: {process.CommandLine}")
    #print(f"Description: {process.Description}")
    #print(f"ExecutablePath: {process.ExecutablePath}")
    #print(f"CreationDate: {process.CreationDate}")
    #print(f"ThreadCount: {process.ThreadCount}")
    #print(f"WorkingSetSize: {process.WorkingSetSize}")

time2 = datetime.now()
time_diff = time2 - time1
print(time_diff)