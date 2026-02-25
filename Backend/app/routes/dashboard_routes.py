from fastapi import APIRouter
from app.config.supabase_client import supabase

router = APIRouter()

@router.get("/{asha_id}")
def get_dashboard(asha_id: str):

    visits = supabase.table("visits") \
        .select("*") \
        .eq("asha_id", asha_id) \
        .execute()

    data = visits.data if visits.data else []

    total = len(data)
    high = len([v for v in data if v.get("risk_class") == 2])
    moderate = len([v for v in data if v.get("risk_class") == 1])
    low = len([v for v in data if v.get("risk_class") == 0])

    return {
        "total_visits": total,
        "high_risk": high,
        "moderate_risk": moderate,
        "low_risk": low,
        "priority_list": sorted(
            data,
            key=lambda x: x.get("priority_score", 0),
            reverse=True
        )[:5]
    }