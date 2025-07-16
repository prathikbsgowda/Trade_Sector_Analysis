from fastapi import APIRouter, Depends, HTTPException
from app.middleware.limiter import rate_limiter
from app.core.security import verify_api_key
from app.services.market import fetch_market_data
from app.services.ai import analyze_with_gemini
from app.services.report import generate_report
import re

router = APIRouter()

@router.get("/analyze/{sector}", dependencies=[Depends(rate_limiter), Depends(verify_api_key)])
async def analyze_sector(sector: str):


    if not re.match(r"^[a-zA-Z\s\-]+$", sector):
        raise HTTPException(status_code=400, detail="Sector must only contain letters, spaces, or hyphens")

    market_data = await fetch_market_data(sector)
    insights = await analyze_with_gemini(market_data)
    report = generate_report(sector, market_data, insights)
    return {"sector": sector, "report": report}
 
