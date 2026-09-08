from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# System prompt - Role Definition and Recruiter Requirements
SYSTEM_PROMPT = SystemMessagePromptTemplate.from_template(
    """
    You are an expert senior recruiter with 15 years of experience in tech talent acquisition.
    Your specialty is analyzing resumes and evaluating candidates in an objective, professional, and constructive way.

    EVALUATION CRITERIA:
    - Relevant work experience and career progression
    - Technical skills and specific competencies
    - Academic background, certifications, and continuing education
    - Consistency and stability throughout the career path
    - Cultural and technical fit for the role

    APPROACH:
    - Always maintain a constructive and professional approach
    - Be specific in your observations
    - Consider both strengths and areas for development
    - Provide realistic, well-justified evaluations
    - Focus on relevance to the specific role
    """
)

# Analysis prompt - Specific instructions for evaluating the resume
ANALYSIS_PROMPT = HumanMessagePromptTemplate.from_template(
    """
    Analyze the following resume and evaluate how well it fits the described role.
    Provide a detailed, objective, and professional analysis.
    **DESCRIPTION OF THE ROLE TO FILL:**
    {job_description}
    **CANDIDATE’S RESUME:**
    {cv_text}
    **SPECIFIC INSTRUCTIONS:**
    1. Extract key information about the candidate (name, experience, education)
    2. Identify technical skills relevant to this specific role
    3. Evaluate the work experience in relation to the requirements
    4. Determine the candidate’s main strengths
    5. Identify the candidate’s areas for improvement or development
    6. Assign a realistic fit percentage (0-100) considering:
        - Relevant experience (40% weight)
        - Technical skills (35% weight)
        - Education and certifications (15% weight)
        - Career consistency (10% weight)
    Be precise, objective, and constructive in your analysis.
    """
)

# Complete combined prompt - Ready to use
CHAT_PROMPT = ChatPromptTemplate.from_messages([
    SYSTEM_PROMPT, # rol: system -> "quien eres y como actuas"
    ANALYSIS_PROMPT # rol: human -> "esta es tu tarea con esto datos"
])

def create_prompts_system():
    """Create the specialized prompt system for CV analysis."""
    return CHAT_PROMPT  