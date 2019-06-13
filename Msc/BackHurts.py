from playsound import playsound
playsound("C:\Windows\media\Windows Notify System Generic.wav")

from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Sit up straight!", "Strengthen your back!")


