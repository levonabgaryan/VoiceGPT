from uuid import uuid4

from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.concurrency import run_in_threadpool
from openai import OpenAI

from services.audio_io import speech_to_text, text_to_speech
from services.chatgpt import ask_gpt
from settings import OPEN_AI_API_KEY

router = APIRouter(tags=['voice-assistant'], prefix='/voice-assistant')
client = OpenAI(api_key=OPEN_AI_API_KEY)


@router.post("/ask")
async def interview(audio: UploadFile):
    # Audio → Text
    user_text = await run_in_threadpool(speech_to_text, client, audio)

    # Text -> GPT-answer
    gpt_answer = await run_in_threadpool(ask_gpt, client, user_text)

    # GPT-answer -> audio
    audio_stream = await run_in_threadpool(text_to_speech, client, gpt_answer)

    output_audio_file_name = f"{uuid4()}.mp3"
    headers = {"Content-Disposition": f'attachment; filename="{output_audio_file_name}"'}
    print(headers)
    return StreamingResponse(audio_stream, media_type="audio/mpeg", headers=headers)

