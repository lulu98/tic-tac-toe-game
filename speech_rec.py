import speech_recognition as sr

def get_row_col(voice_input):
    field_num = 1
    row = None
    col = None
    for i in range(1,10):
        if("eins" in voice_input.lower()):
            return 0,0
        elif("zwei" in voice_input.lower()):
            return 0,1
        elif ("drei" in voice_input.lower()):
            return 0, 2
        elif ("vier" in voice_input.lower()):
            return 1, 0
        elif ("fünf" in voice_input.lower()):
            return 1,1
        elif ("sechs" in voice_input.lower() or "sex" in voice_input.lower()):
            return 1, 2
        elif ("sieben" in voice_input.lower()):
            return 2, 0
        elif ("acht" in voice_input.lower()):
            return 2,1
        elif ("neun" in voice_input.lower()):
            return 2, 2
        if(str(i) in voice_input):
            field_num = i
            break
    for i in range(0,3):
        for j in range(0,3):
            if(3*i + j+1 == field_num):
                row,col = i,j
    return row,col

def get_position():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language="de-DE")
        print("You said: " + text)
        return get_row_col(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None,None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


