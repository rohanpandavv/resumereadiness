# 💼 Resume Readiness Checker

An AI-powered web application that analyzes your resume and provides actionable feedback to improve your job application success. Built with Streamlit and powered by OpenAI's GPT-4.

![Python](https://img.shields.io/badge/python-v3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)

## 🌟 Features

- **📄 PDF Resume Upload**: Support for PDF resume files with intelligent text extraction
- **🤖 AI-Powered Analysis**: Advanced resume analysis using OpenAI's GPT-4 model
- **🎯 Job-Specific Feedback**: Tailored recommendations based on target job role and description
- **🔑 Flexible API Key Input**: Support for both environment variables and secure frontend input
- **📊 Comprehensive Evaluation**: Analysis across multiple dimensions:
  - Content Quality & Impact
  - Skills Alignment
  - Experience Presentation
  - ATS Compatibility
  - Actionable Improvement Areas
- **💾 Downloadable Reports**: Export your analysis results for future reference
- **📈 Usage Statistics**: Track token usage and analysis metrics
- **🔒 Secure Processing**: Local file processing with API-based analysis
- **⚡️ Lightweight Model**: Using `gpt-4o-mini` to keep the analysis cost efficient

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- OpenAI API Key (can be provided via environment variable or frontend input)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rohanpandavv/resumereadiness.git
   cd resumereadiness
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or if using uv:
   ```bash
   uv sync
   ```

4. **Configure OpenAI API Key**
   
   **Option 1: Environment Variable (Recommended)**
   
   Create a `.env` file in the root directory:
   ```env
   # Optional (will prompt for frontend input if not provided)
   OPENAI_API_KEY=your_openai_api_key_here

   # Optional (default values shown)
   STREAMLIT_SERVER_PORT=8501
   STREAMLIT_SERVER_HEADLESS=false
   ```

   **Option 2: Frontend Input**
   
   If no environment variable is found, the app will prompt you to enter your API key directly in the web interface. This is perfect for:
   - Streamlit Cloud deployments
   - Sharing the app with others
   - Testing without local configuration

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

The application will open in your default web browser at `http://localhost:8501`.

## 🖥️ Usage

1. **Enter API Key** (if not set via environment variable): Securely input your OpenAI API key
2. **Upload Resume**: Select and upload your resume in PDF format (max 5MB)
3. **Specify Job Details** (Optional):
   - Enter the target job role you're applying for
   - Paste the job description for more targeted feedback
4. **Analyze**: Click the "🔍 Analyze Resume" button
5. **Review Results**: Get comprehensive AI-powered feedback
6. **Download Report**: Save your analysis for future reference

## 📋 Dependencies

- **[Streamlit](https://streamlit.io/)** (≥1.45.1) - Web application framework
- **[OpenAI](https://openai.com/)** (≥1.82.0) - AI-powered analysis
- **[PyPDF2](https://pypdf2.readthedocs.io/)** (≥3.0.1) - PDF text extraction
- **[python-dotenv](https://python-dotenv.readthedocs.io/)** (≥1.1.0) - Environment variable management

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Optional (will prompt for frontend input if not provided)
OPENAI_API_KEY=your_openai_api_key_here
```

### File Upload Limits

- **Maximum file size**: 5MB
- **Supported formats**: PDF only
- **Text extraction**: Automatic with error handling for corrupted pages

## 🎯 Analysis Features

The AI provides feedback on six key areas:

1. **Content Quality & Impact** - How well achievements are showcased
2. **Skills Alignment** - Relevance to target role
3. **Experience Presentation** - Use of quantifiable results
4. **ATS Compatibility** - Applicant Tracking System optimization
5. **Areas for Improvement** - Specific, actionable recommendations
6. **Job Match Analysis** - Alignment with provided job requirements

## 📊 Example Output

The analysis provides structured feedback including:

- ✅ **Strengths**: What's working well in your resume
- ⚠️ **Areas for Improvement**: Specific issues to address
- 🎯 **Recommendations**: Actionable steps to enhance your resume
- 📈 **ATS Optimization**: Tips for better applicant tracking system compatibility

## 🛠️ Development

### Project Structure

```
resumereadiness/
├── main.py              # Main Streamlit application
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Dependency lock file
├── .env                # Environment variables (create this)
├── .python-version     # Python version specification
└── README.md           # Project documentation
```

### Running in Development Mode

```bash
# Install development dependencies
uv sync --dev

# Run with auto-reload
streamlit run main.py --server.runOnSave true
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔐 Privacy & Security

- **Local Processing**: PDF text extraction happens locally
- **API Usage**: Only extracted text is sent to OpenAI for analysis
- **No Storage**: No resume data is permanently stored
- **Secure API Key Handling**: 
  - Environment variables are preferred for local development
  - Frontend input uses password-masked fields
  - API keys are session-only and never stored permanently
- **Session Security**: All data processing happens within your browser session

## 🆘 Troubleshooting

### Common Issues

**Issue**: "Please enter your OpenAI API key to use the resume analyzer"
- **Solution**: Either set `OPENAI_API_KEY` in your `.env` file or enter it directly in the web interface when prompted

**Issue**: "Error analyzing resume" (API key related)
- **Solution**: Verify your API key is valid and has sufficient credits. You can test it at [OpenAI Platform](https://platform.openai.com/)

**Issue**: "Could not extract text from PDF"
- **Solution**: Ensure your PDF is not image-based or encrypted

**Issue**: "File size exceeds limit"
- **Solution**: Compress your PDF or use a smaller file (max 5MB)

**Issue**: "Empty or unreadable text"
- **Solution**: Try converting your resume to a text-searchable PDF

### Getting Help

If you encounter any issues:
1. Check the troubleshooting section above
2. Review the [Issues](https://github.com/yourusername/resumereadiness/issues) page
3. Create a new issue with detailed description

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4 API
- Streamlit team for the excellent web framework
- PyPDF2 contributors for PDF processing capabilities

---

**Made with ❤️ for job seekers worldwide**
