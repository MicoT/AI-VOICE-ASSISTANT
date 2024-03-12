# Chat GPT Voice Assistant using Raspberry Pi

This repository contains code for a Chat GPT voice assistant implemented on a Raspberry Pi. The voice assistant utilizes the Google Text-to-Speech (gTTS) library for speech synthesis and the SpeechRecognition library for speech recognition. It also leverages the OpenAI API for conversational responses using the GPT-3.5 model.

## Installation

To install the required dependencies, run the following commands:

```bash
sudo apt install python3-pyaudio flac mpg321 python3-tk -y
sudo pip3 install gtts speechrecognition openai

## Usage

Run the tk.py script to launch the GUI for the voice assistant. Click the "Speak" button to activate the assistant, which will listen for your voice input and respond accordingly.

## Files
- ai.py: Contains functions for audio input and output using the microphone and gTTS library.
- search.py: Implements the logic for processing user input, interacting with the OpenAI API, and generating responses.
- tk.py: GUI script that integrates the voice assistant functionality into a Tkinter window.

## Configuration
Make sure to replace 'KEY' in search.py with your actual OpenAI API key for the assistant to function properly.

