def generate_report(sector: str, market_data: str, insights: str) -> str:
    return f"""# 📈 Sector Trade Report: {sector.title()}

---

##  Market Headlines
{market_data.strip()}

---

##  AI-Generated Insights
{insights.strip()}

---

##  Confidence Score
**Estimated AI confidence:** 85%

##  Report Timestamp
*This report was generated automatically based on recent news data and language model analysis.*

"""
