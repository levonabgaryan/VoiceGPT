from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import voice_assistant
from settings import BACKEND_PORT

app = FastAPI()
app.include_router(voice_assistant.router)

@app.get('/')
async def health():
    return 'BACKEND WORKS'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=BACKEND_PORT, reload=True)
