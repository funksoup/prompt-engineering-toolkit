# 🎯 Prompt Engineering Toolkit

An interactive educational tool demonstrating prompt engineering concepts and best practices. Compare outputs from OpenAI and Claude side-by-side while learning how to craft effective prompts.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-purple)

## Screenshots

### Basic vs Advanced Prompts
![Basic vs Advanced](screenshots/basic-vs-advanced.jpg)

### Few-Shot Learning
![Few-Shot](screenshots/few-shot.jpg)


## 🌟 Features

### 📊 Four Learning Modules

1. **Basic vs Advanced Prompts**
   - Compare simple vs well-structured prompts
   - See how specificity improves output quality
   - Learn to add context, audience, and format specifications

2. **Few-Shot Learning**
   - Provide examples to guide AI responses
   - Practice email classification, sentiment analysis, and text transformation
   - Understand when examples improve performance

3. **Prompt Chaining**
   - Break complex tasks into sequential steps
   - Use output from one prompt as input to the next
   - See how chaining improves quality for multi-step workflows

4. **Chain-of-Thought Reasoning**
   - Request step-by-step reasoning from AI models
   - Solve math problems, logic puzzles, and decision analysis
   - Improve accuracy on complex problems

### 🔄 Side-by-Side Comparison
- Compare outputs from OpenAI (GPT-4) and Anthropic (Claude) simultaneously
- Understand how different models respond to the same prompts
- Learn which models excel at different tasks

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Anthropic API key ([Get one here](https://console.anthropic.com/))

### Installation

1. Clone this repository:
```bash
git clone https://github.com/[your-username]/prompt-engineering-toolkit.git
cd prompt-engineering-toolkit
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the App

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser to `http://localhost:8501`

3. Enter your API keys in the sidebar

4. Start exploring prompt engineering concepts!

## 📖 Usage Guide

### Entering API Keys

In the left sidebar:
1. Paste your OpenAI API key
2. Paste your Anthropic API key
3. Select which models to use

**Note:** Your API keys are only used locally and are never stored or transmitted anywhere except to OpenAI and Anthropic APIs.

### Exploring Each Module

**Basic vs Advanced:**
- Enter a topic you want explained
- Compare how basic and advanced prompts differ
- See the quality improvement in responses

**Few-Shot Learning:**
- Choose a task type (classification, sentiment, transformation)
- See examples of the pattern
- Try your own input and see the AI follow the pattern

**Prompt Chaining:**
- Enter a blog topic
- Watch as the AI:
  1. Brainstorms key points
  2. Creates an outline
  3. Writes the introduction
- See how each step builds on the previous

**Chain-of-Thought:**
- Choose a problem type
- See the AI break down its reasoning step-by-step
- Compare reasoning approaches between models

## 🎓 Learning Objectives

By using this toolkit, you'll learn:

✅ How to structure effective prompts
✅ When to use few-shot learning vs zero-shot
✅ How to break complex tasks into chains
✅ When to request step-by-step reasoning
✅ Differences between AI models (GPT-4 vs Claude)
✅ How to specify format, tone, and length
✅ The importance of context and examples

## 🛠️ Technology Stack

- **Frontend:** Streamlit (Python web framework)
- **AI APIs:** 
  - OpenAI GPT-4 API
  - Anthropic Claude API
- **Python Libraries:**
  - `streamlit` - Interactive web interface
  - `openai` - OpenAI API client
  - `anthropic` - Anthropic API client

## 📁 Project Structure

```
prompt-engineering-toolkit/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore            # Git ignore file
└── LICENSE               # MIT License
```

## 🔐 Security Notes

- Never commit API keys to Git
- Use environment variables for production deployments
- API keys entered in the sidebar are session-only (not persisted)
- Consider using `.env` file for local development

## 🎯 Future Enhancements

Potential additions to this toolkit:

- [ ] System prompt comparison
- [ ] Temperature and parameter tuning
- [ ] Prompt templates library
- [ ] Cost tracking for API usage
- [ ] Export/save results
- [ ] Multi-modal prompt examples (images + text)
- [ ] Prompt optimization suggestions

## 🤝 Contributing

This is an educational project! Contributions are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Additional Resources

**Prompt Engineering Guides:**
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Learn Prompting](https://learnprompting.org/)

**Research Papers:**
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Few-Shot Learning](https://arxiv.org/abs/2005.14165)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Josephine Dorado**
- GitHub: [@funksoup](https://github.com/funksoup)
- LinkedIn: [funksoup](https://linkedin.com/in/funksoup)
- Immersive Learning Portfolio: [coda.io/funksoup](https://coda.io/@funksoup/immersive-learning)
- Portfolio: [funksoup.com](https://funksoup.com)

## 🙏 Acknowledgments

- Built as part of AI skills development for enterprise AI adoption roles
- Inspired by prompt engineering best practices from OpenAI and Anthropic
- Thanks to the Streamlit team for the excellent framework

---

**Note:** This is an educational tool. API usage will incur costs based on your OpenAI and Anthropic pricing plans. Monitor your usage carefully.
