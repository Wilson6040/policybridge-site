from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List
import uuid
from datetime import datetime, timezone


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")  # Ignore MongoDB's _id field
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    
    # Convert to dict and serialize datetime to ISO string for MongoDB
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    _ = await db.status_checks.insert_one(doc)
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    # Exclude MongoDB's _id field from the query results
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    
    # Convert ISO string timestamps back to datetime objects
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    
    return status_checks


# ---- Document deliverables (download centre) ----
DELIVERABLES_DIR = ROOT_DIR / 'deliverables'

COMPARISON_GROUP = "Media & Entertainment — market comparison"
WORDING_GROUP = "Media & Music Combined wording (0526)"

DOCUMENTS = [
    {
        "id": "comparison_full",
        "title": "Full Coverage Comparison",
        "subtitle": "TMHCC vs 5 competitors",
        "description": "A like-for-like, section-by-section comparison of the TMHCC Media & Music "
                       "Combined wording against all five competitor wordings — Tysers (Zurich), "
                       "Yutree (AXA), Liberty, Allianz and AXA XL (XL Catlin). Coverage matrix, "
                       "Media-Liability feature detail, competitor-by-competitor analysis, "
                       "exclusions / conditions / limits and clause mapping.",
        "base": "TMHCC_Media_Coverage_Comparison_FULL",
        "accent": "#00648B",
        "group": COMPARISON_GROUP,
    },
    {
        "id": "comparison_gapfill",
        "title": "Gap-Fill / Wording Enhancement Strategy",
        "subtitle": "Strategic recommendations",
        "description": "Evidence-based recommendations to make the TMHCC base wording more holistic and "
                       "demonstrably market-leading — coverage gaps to fill, exclusion write-backs, "
                       "definitions/conditions to clarify, an underwriting risk assessment and an "
                       "implementation roadmap. Each item is supported by at least one competitor wording.",
        "base": "TMHCC_Media_GapFill_Enhancement_Strategy",
        "accent": "#B88A3C",
        "group": COMPARISON_GROUP,
    },
    {
        "id": "comparison_qa",
        "title": "QA / Methodology Report",
        "subtitle": "Method, findings & sign-off",
        "description": "Documents reviewed, comparison method, key TMHCC strengths and gaps, recommended "
                       "enhancements, exclusion issues, assumptions, points for legal/underwriting sign-off "
                       "and the final 10-point report.",
        "base": "TMHCC_Media_Comparison_QA_Methodology",
        "accent": "#C0563F",
        "group": COMPARISON_GROUP,
    },
    {
        "id": "wording_tracked",
        "title": "Final Wording (0526) — Tracked Changes (Round 7)",
        "subtitle": "Latest update — shows the changes",
        "description": "The final TMHCC Media Combined 0526 wording with the Round 7 amendments shown as tracked changes "
                       "(from a clean accepted baseline): the Admission-of-Liability condition precedent replaced with a "
                       "prejudice-qualified condition; a new 'Proof of Ownership and Value' claims requirement (Sections 1–11); "
                       "'Accounts Receivable (Book Debts)' in Section 3; and the Section 15 'CyberGuard™ (Cyber Liability)' title. "
                       "Section 12 enhancements are held for sign-off and are NOT in the wording.",
        "base": "TMHCC_Media_Combined_0526_FINAL_TrackedChanges",
        "accent": "#E20033",
        "group": WORDING_GROUP,
    },
    {
        "id": "wording_clean",
        "title": "Final Wording (0526) — Clean (Round 7)",
        "subtitle": "Latest update — changes accepted",
        "description": "The same final wording as the tracked-changes version with the Round 7 amendments accepted "
                       "(clean copy). This is the current working policy wording.",
        "base": "TMHCC_Media_Combined_0526_FINAL_Clean",
        "accent": "#009CE5",
        "group": WORDING_GROUP,
    },
    {
        "id": "wording",
        "title": "New Wording (0526) — Polished (pre-update baseline)",
        "subtitle": "Prior baseline (superseded by Round 7)",
        "description": "The full TMHCC Media Combined 0526 wording with red text removed, a clean two-column hyperlinked "
                       "Contents page (bold 'Section N:' labels, right-aligned page numbers, accurate destinations), "
                       "no blank pages, and a PDF copy that retains all clickable internal navigation. Superseded by the "
                       "Round 7 Tracked Changes / Clean versions above.",
        "base": "TMHCC_Media_Combined_0526_FINAL_polished",
        "accent": "#6C7378",
        "group": WORDING_GROUP,
    },
    {
        "id": "changes",
        "title": "Summary of Changes",
        "subtitle": "0223C vs 0526 comparison",
        "description": "A branded, traffic-light comparison of the previous and new wordings, with an "
                       "exclusions deep-dive, conditions and limits changes, and reviewer notes.",
        "base": "TMHCC_Media_Combined_Summary_of_Changes_FINAL",
        "accent": "#C79000",
    },
    {
        "id": "cover",
        "title": "Summary of Cover",
        "subtitle": "Based on the 0526 wording",
        "description": "A clear, high-level summary of cover across all 15 sections, with key exclusions, "
                       "conditions, a limits/excess table and the required disclaimer.",
        "base": "TMHCC_Media_Combined_Summary_of_Cover_FINAL",
        "accent": "#0066CC",
    },
    {
        "id": "qa",
        "title": "QA Report",
        "subtitle": "Review & sign-off notes",
        "description": "Files reviewed, comparison method, key enhancements, restrictions, exclusions, "
                       "corrections made and items recommended for underwriting / legal sign-off.",
        "base": "TMHCC_Media_Combined_QA_Report",
        "accent": "#E20033",
    },
]


@api_router.get("/documents")
async def list_documents():
    items = []
    for d in DOCUMENTS:
        formats = []
        for ext in ("docx", "pdf"):
            fp = DELIVERABLES_DIR / f"{d['base']}.{ext}"
            if fp.exists():
                formats.append({
                    "ext": ext,
                    "filename": fp.name,
                    "size_kb": round(fp.stat().st_size / 1024),
                })
        item = {k: v for k, v in d.items() if k != "base"}
        item.setdefault("group", WORDING_GROUP)
        item["formats"] = formats
        items.append(item)
    return {"documents": items}


@api_router.get("/documents/download/{filename}")
async def download_document(filename: str, inline: bool = False):
    safe = os.path.basename(filename)
    fp = DELIVERABLES_DIR / safe
    if not fp.exists() or fp.suffix.lower() not in (".docx", ".pdf"):
        raise HTTPException(status_code=404, detail="Document not found")
    is_pdf = fp.suffix.lower() == ".pdf"
    media = ("application/pdf" if is_pdf
             else "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    # PDFs can be viewed inline in the browser; .docx must download (browsers can't render it)
    disposition = "inline" if (inline and is_pdf) else "attachment"
    return FileResponse(
        path=str(fp),
        media_type=media,
        headers={"Content-Disposition": f'{disposition}; filename="{safe}"'},
    )


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()