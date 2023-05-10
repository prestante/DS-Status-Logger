import wmi
from datetime import datetime
from multiprocessing import Pool

remote_computers = ['adc-ctc01.tecomgroup.ru', 'adc-ctc02.tecomgroup.ru', 'adc-ctc03.tecomgroup.ru',
                    'adc-ctc04.tecomgroup.ru', 'adc-ctc05.tecomgroup.ru', 'adc-ctc06.tecomgroup.ru',
                    'adc-ctc07.tecomgroup.ru', 'adc-ctc08.tecomgroup.ru', 'adc-ctc09.tecomgroup.ru',
                    'adc-ctc10.tecomgroup.ru', 'adc-ctc11.tecomgroup.ru', 'adc-ctc12.tecomgroup.ru',
                    'adc-ctc13.tecomgroup.ru', 'adc-ctc14.tecomgroup.ru', 'adc-ctc15.tecomgroup.ru',
                    'adc-ctc16.tecomgroup.ru', 'adc-ctc17.tecomgroup.ru', 'adc-ctc18.tecomgroup.ru',
                    'adc-ctc19.tecomgroup.ru', 'adc-ctc20.tecomgroup.ru', 'adc-ctc21.tecomgroup.ru',
                    'adc-ctc22.tecomgroup.ru', 'adc-ctc23.tecomgroup.ru', 'adc-ctc24.tecomgroup.ru']

def get_process_ids(computer):
    try:
        connection = wmi.WMI(computer, user="Administrator", password="Tecom_1!")
        processes = connection.Win32_Process(name="ADC1000NT.exe")
        return [(computer, process.ProcessId) for process in processes]
    except wmi.x_access_denied:
        print(f"Access denied for {computer}")
    except wmi.x_wmi:
        print(f"WMI connection failed for {computer}")

if __name__ == '__main__':
    time1 = datetime.now()
    with Pool() as p:
        results = p.map(get_process_ids, remote_computers)
    for r in results:
        for computer, pid in r:
            print(f"Computer: {computer} | Process ID: {pid}")
    time_diff = datetime.now() - time1
    print(time_diff)
