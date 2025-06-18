import io

import openai
from fastapi import UploadFile

def speech_to_text(client: openai.OpenAI, audio_file: UploadFile) -> str:
    # https://platform.openai.com/docs/guides/speech-to-text#:~:text=Additional%20options-,python,%2C%20%0A%20%20%20%20file%3Daudio_file%2C%20%0A%20%20%20%20response_format%3D%22text%22%0A)%0A%0Aprint(transcription.text),-The%20API%20Reference
    audio_bytes = io.BytesIO(audio_file.file.read())
    audio_bytes.name = audio_file.filename

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_bytes,
        response_format="text"
    )
    return transcription


def text_to_speech(client: openai.OpenAI, text_: str) -> io.BytesIO:
    # https://platform.openai.com/docs/guides/text-to-speech#:~:text=from%20pathlib%20import,response.stream_to_file(speech_file_path)
    audio_buffer = io.BytesIO()

    with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="shimmer",
            input=text_,
            response_format="wav",
            instructions="Speak in a calm, professional tone.",
    ) as response:
        for chunk in response.iter_bytes():
            audio_buffer.write(chunk)

    audio_buffer.seek(0)
    return audio_buffer