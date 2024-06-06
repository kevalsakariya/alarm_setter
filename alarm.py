import datetime
from playsound import playsound
import win32com.client 


speaker = win32com.client.Dispatch("SAPI.SpVoice") 
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            text = "Time to Wake up now fast" 
            speaker.Speak(text)
            playsound('G:\python\project\Alarm_sound.mp3')  
            break

if __name__ == "__main__":
    alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
    print("Now,your alarm is set..")
    set_alarm(alarm_time)
    
    

        
