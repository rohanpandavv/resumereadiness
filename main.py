import streamlit as st
import PyPDF2
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set page config with file upload limit
st.set_page_config(
    page_title="Resume Readiness Checker", 
    page_icon="💼", 
    layout="centered"
)

# Set maximum file upload size to 5MB
st.config.set_option('server.maxUploadSize', 5)

st.title("Resume Readiness Checker")
st.markdown("""
Upload your resume and get AI-powered feedback to improve your job application success.
""")

# Check for OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("⚠️ OpenAI API key not found. Please add OPENAI_API_KEY to your .env file.")
    st.stop()

# File upload with size limit
file = st.file_uploader(
    "Upload your resume (PDF format only)", 
    type=["pdf"],
    help="Maximum file size: 5MB"
)

# Input fields
job_role = st.text_input(
    "Enter the job role you're applying for (optional)",
    placeholder="e.g., Software Engineer, Data Scientist, Product Manager"
)

job_description = st.text_area(
    "Enter the job description (optional)",
    placeholder="Paste the job description here for more targeted feedback...",
    height=100
)

analyze = st.button("🔍 Analyze Resume", type="primary")

def pdf_to_text(uploaded_file):
    """Extract text from PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num, page in enumerate(pdf_reader.pages):
            try:
                text += page.extract_text() + "\n"
            except Exception as e:
                st.warning(f"Warning: Could not extract text from page {page_num + 1}")
                continue
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

def extract_text_from_file(uploaded_file):
    """Extract text from uploaded file."""
    if uploaded_file.type == "application/pdf":
        return pdf_to_text(uploaded_file)
    else:
        st.error("Unsupported file type. Please upload a PDF file.")
        return None

def analyze_resume_with_ai(file_content, job_role, job_description):
    """Analyze resume using OpenAI API."""
    try:
        # Build context-aware prompt
        context = ""
        if job_role:
            context += f"Target Job Role: {job_role}\n"
        if job_description:
            context += f"Job Description: {job_description}\n"
        
        prompt = f"""Please analyze this resume and provide constructive, actionable feedback.

        {context}

        Focus on these key aspects:
        1. **Content Quality & Impact**: How well does the content showcase achievements?
        2. **Skills Alignment**: How well do the skills match the target role?
        3. **Experience Presentation**: Are experiences described with quantifiable results?
        4. **ATS Compatibility**: Will this resume pass through Applicant Tracking Systems?
        5. **Areas for Improvement**: Specific, actionable recommendations
        
        {"6. **Job Match Analysis**: How well does this resume align with the provided job requirements?" if job_role or job_description else "6. **General Recommendations**: Suggestions for broader job market appeal"}

        Resume Content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific, actionable recommendations."""

        client = OpenAI(api_key=OPENAI_API_KEY)
        
        with st.spinner("🤖 AI is analyzing your resume..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert resume analyst and career coach with extensive experience in recruitment and HR. Provide detailed, actionable feedback that helps job seekers improve their resumes for better job prospects."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500,
            )
        
        return response.choices[0].message.content, response.usage
    
    except Exception as e:
        st.error(f"Error analyzing resume: {str(e)}")
        return None, None

# Main analysis logic
if analyze and file:
    # Check file size (additional check)
    file_size = len(file.getvalue()) / (1024 * 1024)  # Convert to MB
    if file_size > 5:
        st.error("❌ File size exceeds 5MB limit. Please upload a smaller file.")
        st.stop()
    
    st.write("📄 Processing your resume...")
    
    # Extract text from file
    file_content = extract_text_from_file(file)
    
    if not file_content:
        st.error("❌ Could not extract text from the file. Please ensure it's a valid PDF.")
        st.stop()
    
    if not file_content.strip():
        st.error("❌ The file appears to be empty or contains no readable text.")
        st.stop()
    
    # Show extracted text preview (optional)
    with st.expander("📝 View Extracted Text (Preview)"):
        st.text_area("Extracted Content", file_content[:1000] + "..." if len(file_content) > 1000 else file_content, height=200)
    
    # Analyze with AI
    analysis_result, usage_info = analyze_resume_with_ai(file_content, job_role, job_description)
    
    if analysis_result:
        st.markdown("## 📊 Resume Analysis Results")
        st.markdown(analysis_result)
        
        # Optional: Show usage statistics in an expander
        if usage_info:
            with st.expander("📈 Analysis Statistics"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Tokens", usage_info.total_tokens)
                with col2:
                    st.metric("Prompt Tokens", usage_info.prompt_tokens)
                with col3:
                    st.metric("Response Tokens", usage_info.completion_tokens)
        
        # Add download option for feedback
        st.download_button(
            label="💾 Download Analysis",
            data=analysis_result,
            file_name=f"resume_analysis_{job_role.replace(' ', '_') if job_role else 'general'}.txt",
            mime="text/plain"
        )

elif analyze and not file:
    st.warning("⚠️ Please upload a resume file to analyze.")

else:
    st.info("👆 Upload your resume above to get started with AI-powered feedback!")

# Add footer with tips
st.markdown("---")
st.markdown("""
### 💡 Tips for Better Results:
- **Use a clear, well-formatted PDF** for best text extraction
- **Provide job role and description** for targeted feedback
- **Include quantifiable achievements** in your resume
- **Keep file size under 5MB** for faster processing
""")