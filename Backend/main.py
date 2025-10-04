from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
app = FastAPI(
    title="Medical Assistant",
    description="API For AI Medical Assistant Chatbot"
)

# CORS Setup
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://your-frontend-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)

# middleware exception handlers
app.middleware("http")(catch_exception_middleware)
# routers

# 1, upload pdfs

#2 asking query