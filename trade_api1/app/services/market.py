# import httpx

# async def fetch_market_data(sector: str) -> str:
#     query = f"{sector} sector news India"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1")
#         if response.status_code == 200:
#             data = response.json()
#             abstract = data.get("AbstractText") or data.get("Abstract") or ""
#             related = data.get("RelatedTopics", [])
#             extras = "\n".join(
#                 f"- {t['Text']}" for t in related if isinstance(t, dict) and "Text" in t
#             )
#             return abstract + "\n" + extras if (abstract or extras) else f"No market data found for {sector}."
#         raise Exception("Failed to fetch market data.")

import httpx
from app.core.config import NEWS_API_KEY

async def fetch_market_data(sector: str) -> str:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": f"{sector} sector India",
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 6,  
        "apiKey": NEWS_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            if not articles:
                return f"No recent news articles found for '{sector}' sector."

            output = [f"Top News for '{sector}' Sector:\n"]
            for i, article in enumerate(articles, 1):
                title = article.get("title", "No title")
                desc = article.get("description", "")
                source = article.get("source", {}).get("name", "Unknown source")
                url = article.get("url", "#")
                output.append(
                    f"{i}. {title} ({source})\n   {desc}\n   Link: {url}\n"
                )
            return "\n".join(output)

        elif response.status_code == 429:
            return "NewsAPI rate limit exceeded. Please try again later."
        else:
            return f"Error fetching news data (status {response.status_code})."
