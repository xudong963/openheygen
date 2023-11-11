from TTS.api import TTS
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, default="Hello, world!")
    parser.add_argument("--output_path", type=str, default="result/output.wav")
    parser.add_argument("--speaker_wav", type=str, default="source/test.wav")
    parser.add_argument("--language", type=str, default="en")
    args = parser.parse_args()

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    tts.tts_to_file(text=args.text,
                    file_path=args.output_path,
                    speaker_wav=args.speaker_wav,
                    language=args.language)

    print("Finish cloning the voice!")
