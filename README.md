# Tic-Tac-Toe Game
## Introduction
A simple application to play Tic-Tac-Toe on. You can either use your voice or just click the desired field.  

![alt text](https://github.com/lulu98/tic-tac-toe-game/blob/master/thumbnail.PNG)

## Technical details
For the graphics the same simple graphics library is used as in the chess project. The game comes into being by positioning the cross and the circle on a specific position within the window.  
To use speech recognition the package SpeechRecognition is used with Google API. This recognition is very slow and especially in English (maybe because you are no native speaker, neither am I) inefficient. So I set the language settings to german language and for edge cases I used simple if clauses. If it takes long, just wait and maybe don't just say the number but also another word, so that the algorithm for speech recognition has more material to work on (e.g. "Position [1-9]" in my case).
