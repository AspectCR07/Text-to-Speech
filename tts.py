
**`tts.py`**
```python
import argparse
import pyttsx3
import os

def text_to_speech(input_file, output_file=None, rate=None, voice=None):
    if not os.path.isfile(input_file):
        print('Input file not found')
        return
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    engine = pyttsx3.init()
    if rate:
        engine.setProperty('rate', rate)
    if voice:
        voices = engine.getProperty('voices')
        if 0 <= voice < len(voices):
            engine.setProperty('voice', voices[voice].id)
    if output_file:
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        print(f'Audio saved to {output_file}')
    else:
        engine.say(text)
        engine.runAndWait()

def main():
    parser = argparse.ArgumentParser(description='Convert text file to speech (pyttsx3)')
    parser.add_argument('input', help='Input text file')
    parser.add_argument('--output', help='Output audio file (e.g., out.mp3)')
    parser.add_argument('--rate', type=int, help='Speech rate (words per minute)')
    parser.add_argument('--voice', type=int, help='Voice index (0,1,...)')
    args = parser.parse_args()
    text_to_speech(args.input, output_file=args.output, rate=args.rate, voice=args.voice)

if __name__ == '__main__':
    main()
