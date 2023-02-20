from tkinter import *
import webbrowser
from deepface import DeepFace as dp
import cv2
import uuid
import os
import settings
import playlistMaker as pm




root = Tk()
root.configure(bg = "green")
root.geometry('300x300')
root.title("Musical Recognition")

def callback(url):
    webbrowser.open_new(url)
def pic():
    REAL_PATH = os.path.join('data', 'tests')
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        ret, frame = capture.read()

        frame = frame[100:100+250,200:200+250,:]

        if cv2.waitKey(1) & 0XFF == ord('c'):
            imgname = os.path.join(REAL_PATH, '{}.jpg'.format(uuid.uuid1()))
            cv2.imwrite(imgname,frame)
            break;

        cv2.imshow('Image Collection', frame)
        # if cv2.waitKey(1) & 0XFF == ord('q'):
        #     break
    capture.release()
    cv2.destroyAllWindows()

    i_path = imgname

    img = cv2.imread(i_path)

    demo = dp.analyze(i_path, enforce_detection=False)
    demo

    main_emotion = demo[0]['dominant_emotion']  
    if main_emotion == 'disgust':
        print("No time for music! Your main emotion is " + main_emotion +  " Go exercise.")
        l0=Label(root, text = "No time for music! your main emotion is disgust. Go exercise.")
        l0.pack()
    elif main_emotion == 'happy' or main_emotion == 'sad' or main_emotion == 'fear' or main_emotion == 'angry':
        hyperlink = pm.create_mood_playlist(main_emotion)
        l1=Label(root, text = "Click here to view your Playlist", fg="blue", cursor="hand2", underline=31)#.grid(column=2,row=1)
        l1.pack()
        l1.bind("<Button-1>", lambda x: callback(hyperlink))
        print("Your emotion was " + main_emotion)
        
    else:
        l2=Label(root, text = "retry")
        l2.pack()
    str = "Your emotion is {}".format(main_emotion)
    l3=Label(root, text = str)
    l3.pack(side = BOTTOM)

def login():
    settings.ACCESS_TOKEN = pm.user_authorize_Spotipy()
    print (settings.ACCESS_TOKEN)
    # global ACCESS_TOKEN
    b1 = Button(frm, text="Take Picture", command= pic, highlightbackground="green", fg = "blue").grid(column=2, row=1)
    b2 = Button(frm, text="Quit", command=root.destroy, highlightbackground="green", fg = "red").grid(column=2, row=7)
    #b2.pack(side=BOTTOM)

frm = Frame(root,bg="green")
frm.grid()
frm.pack()

b0= Button(frm, text = "Login", command = login, highlightbackground="green", fg = "green").grid(column=2, row=1)
root.mainloop()


