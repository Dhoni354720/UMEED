# Backend/services/member_service.py

from Backend.app.config.supabase_client import supabase
import uuid


def create_member(data):

    member = {
        "id": str(uuid.uuid4()),
        "family_id": data.get("family_id"),
        "name": data.get("name"),
        "gender": data.get("gender"),
        "date_of_birth": data.get("date_of_birth"),
        "phone": data.get("phone"),
        "category": data.get("category"),
        "adhaar_last4": data.get("adhaar_last4"),
        "status": data.get("status")
    }

    response = supabase.table("members").insert(member).execute()

    return response.data


def get_member(member_id):

    response = supabase.table("members").select("*").eq("id", member_id).execute()

    return response.data