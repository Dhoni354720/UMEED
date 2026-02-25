from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth_routes, visit_routes, dashboard_routes, member_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(visit_routes.router, prefix="/visit")
app.include_router(dashboard_routes.router, prefix="/dashboard")
app.include_router(member_routes.router, prefix="/member")

@app.get("/")
def root():
    return {"message": "UMEED Backend Running"}