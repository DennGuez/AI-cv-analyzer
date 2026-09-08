from pydantic import BaseModel, Field

class AnalysisCV(BaseModel):
    """Structured analysis of a candidate's CV: extracted profile data plus a fit assessment."""
    name: str = Field(description="Full name of the candidate extracted from the CV")
    years_of_experience: int = Field(description="Years of relevant experience in the field")
    key_skills: list[str] = Field(description="List of key skills extracted from the CV")
    education: str = Field(description="Highest education level and main especialization")
    relevant_experience: str = Field(description="Resume of the more relevant experience")
    streghts: list[str] = Field(description="3-5 core strengths derived from the candidate’s profile")
    evelopment_areas: list[str] = Field(description="2-4 areas where the candidate could develop or improve")
    fit_score: int = Field(description="Fit score from 0-100 based on experience, skills, and education", ge=0, le=100) 