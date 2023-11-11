# HeyGen's open source solution

## Thanks for [coqui](https://github.com/coqui-ai/TTS) and [video-retalking](https://github.com/OpenTalker/video-retalking)

### Environment Setup

```shell
conda create -n openheygen python=3.8

conda activate openheygen

conda install ffmpeg

pip install -r requirements.txt
```

### Usage

Put your original face video and audio file into `source` folder.

Run `openheygen.py` to generate the cloned audio for you input text.

```shell
python3 openheygen.py --text "Input your text here" --language "zh-cn"

--text: The text you want to generate.
--language: The language of the text. Currently support Arabic: ar, Brazilian Portuguese: pt , Chinese: zh-cn, Czech: cs, Dutch: nl, English: en, French: fr, German: de, Italian: it, Polish: pl, Russian: ru, Spanish: es, Turkish: tr, Japanese: ja, Korean: ko, Hungarian: hu.
--speaker_wav: The speaker wav file you want to use. Default is `source/test.wav`.
--output_path: The output path of the generated audio. Default is `result/output.wav`.
```

After the audio is generated, go to `video-retalking` folder and run `video-retalking.py` to generate the final video.

```shell
python3 inference.py \
  --face ../source/test.mp4 \
  --audio ../result/output.wav \
  --outfile ../result/output.mp4
  
--face: The face video you want to use.
--audio: The audio you want to use which is generated by `openheygen.py`.
--outfile: The output path of the generated video.
```
