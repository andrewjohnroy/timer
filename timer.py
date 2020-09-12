from playsound import playsound
import time
for i in range(600):
    if i//60 == 1 and i % 60 == 1:
        print(str(i//60) + " minute and " + str(i % 60) + " second.")
    elif i//60 == 1:
        print(str(i//60) + " minute and " + str(i % 60) + " seconds.")
    elif i % 60 == 1:
        print(str(i//60) + " minutes and " + str(i % 60) + " second.")
    else:    
        print(str(i//60) + " minutes and " + str(i % 60) + " seconds.")
    time.sleep(1)
print("PIZZA TIME!")
playsound(r"C:\Users\Andrew\Music\Spider-Man 2_ The Game Pizza Theme.mp3")
input()
