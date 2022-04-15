# Voice-Based-Organizer

The project has a prototype part to view the GUI (how it would look with voice support) and a code section that separated the functionality, allowing us to evaluate and focus on both separately.

# Setup

These instructions have been tried for Windows 10. They may differ for other platforms.

1. Install miniconda for Python 3.8
2. Once installed, open the Miniconda Prompt and make sure there is a (base) prefix on the prompt.
3. Install speech_recognition using conda install -c speech_recognition.
4. Install pyaudio.
5. Using pip (make sure it is conda's built in pip) install pyttsx3.



![2022-04-14 14_52_53-](https://user-images.githubusercontent.com/77152143/163507155-e36d3d45-20b9-451c-acdd-378028c52315.png)
![2022-04-14 14_57_12-](https://user-images.githubusercontent.com/77152143/163507193-f1287688-a2f2-4107-9568-100674e36f00.png)

For Windows, there is a flac file in this repository to be placed in C:\Windows\System32.

IF you have other python distributions on your system, you may have to include the path to the one shipped with this environment to run the program.

# Unit Test

This test attempts to detect the sound hardware on your system. The device_index listed is what is used as an argument for the speech recognition instance. For systems I have tested on, the device_index needed was 1. It may differ for your system. 
The test will attempt to record one phrase from you and display it. Please speak when you see the 'Listening' portion. If it worked, you should hear something back from the engine.

[Test Passing]
![test-pass-2022-04-15 01_10_27-Window](https://user-images.githubusercontent.com/77152143/163507269-936a7d06-434d-4f78-8bc6-6b1cbd5dfb48.png)

[Test Failing]
![test-fail-2022-04-15 01_10_05-Window](https://user-images.githubusercontent.com/77152143/163507319-3137fbec-ee91-4f88-9c34-c377f8c194ae.png)



