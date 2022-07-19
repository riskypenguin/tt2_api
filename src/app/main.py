import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.app.routers import api
from src.domain.stage import Stage

load_dotenv()

ENV_STAGE = os.getenv('STAGE')

app = FastAPI(title=f"TT2 Raid Data API | {ENV_STAGE}",
              version="0.1.0",
              description="""
    Provides access to raid seed data for the mobile game Tap Titans 2.
    You can get raw (unmodified) seeds and enhanced (with useful extra information) seeds.
    """,
              swagger_ui_parameters={
                  "defaultModelsExpandDepth": -1,
                  "tryItOutEnabled": ENV_STAGE != Stage.DEV
              })

cors_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")
