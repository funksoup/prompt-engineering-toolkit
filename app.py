import streamlit as st
import openai
from anthropic import Anthropic
import os

# Page config
st.set_page_config(
    page_title="Prompt Engineering Toolkit",
    page_icon="🎯",
    layout="wide"
)

# Title and description
st.title("🎯 Prompt Engineering Toolkit")
st.markdown("""
An educational tool demonstrating prompt engineering concepts and best practices.
Compare outputs from different AI models and learn how to craft effective prompts.
""")

# Sidebar for API keys
st.sidebar.title("⚙️ Configuration")
st.sidebar.markdown("---")

# API Key inputs
openai_key = st.sidebar.text_input(
    "OpenAI API Key", 
    type="password",
    help="Get your API key from platform.openai.com"
)
anthropic_key = st.sidebar.text_input(
    "Anthropic API Key", 
    type="password",
    help="Get your API key from console.anthropic.com"
)

# Model selection
st.sidebar.markdown("---")
st.sidebar.subheader("Model Selection")
openai_model = st.sidebar.selectbox(
    "OpenAI Model",
    ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo"]
)
anthropic_model = st.sidebar.selectbox(
    "Anthropic Model",
    ["claude-sonnet-4-20250514", "claude-sonnet-3-5-20241022", "claude-opus-3-5-20241022"]
)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🎓 Basic vs Advanced",
    "📝 Few-Shot Learning",
    "🔗 Prompt Chaining",
    "🧠 Chain-of-Thought"
])

def call_openai(prompt, system="You are a helpful assistant."):
    """Call OpenAI API"""
    if not openai_key:
        return "⚠️ Please enter your OpenAI API key in the sidebar."
    
    try:
        client = openai.OpenAI(api_key=openai_key)
        response = client.chat.completions.create(
            model=openai_model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

def call_claude(prompt, system="You are a helpful assistant."):
    """Call Claude API"""
    if not anthropic_key:
        return "⚠️ Please enter your Anthropic API key in the sidebar."
    
    try:
        client = Anthropic(api_key=anthropic_key)
        response = client.messages.create(
            model=anthropic_model,
            max_tokens=1000,
            system=system,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# TAB 1: Basic vs Advanced Prompts
with tab1:
    st.header("🎓 Basic vs Advanced Prompts")
    st.markdown("""
    See how prompt engineering improves output quality. Compare a basic prompt 
    with an advanced, well-structured prompt.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("❌ Basic Prompt")
        basic_topic = st.text_input("Topic:", "Python", key="basic_topic")
        basic_prompt = f"Explain {basic_topic}"
        st.code(basic_prompt, language="text")
        
    with col2:
        st.subheader("✅ Advanced Prompt")
        advanced_topic = st.text_input("Topic:", "Python", key="advanced_topic")
        audience = st.selectbox("Audience:", ["beginner programmer", "experienced developer", "non-technical manager"])
        format_type = st.selectbox("Format:", ["concise explanation", "detailed guide", "pros and cons"])
        
        advanced_prompt = f"""Please explain {advanced_topic} to a {audience}.

Structure your response as a {format_type} that:
- Uses clear, accessible language
- Includes practical examples
- Highlights key takeaways
- Keeps the explanation focused and actionable

Target length: 2-3 paragraphs."""
        
        st.code(advanced_prompt, language="text")
    
    if st.button("🚀 Compare Results", key="compare_basic"):
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.subheader("📊 OpenAI Response")
            with st.spinner("Calling OpenAI..."):
                st.markdown("**Basic Prompt:**")
                basic_result = call_openai(basic_prompt)
                st.info(basic_result)
                
                st.markdown("**Advanced Prompt:**")
                advanced_result = call_openai(advanced_prompt)
                st.success(advanced_result)
        
        with col_b:
            st.subheader("📊 Claude Response")
            with st.spinner("Calling Claude..."):
                st.markdown("**Basic Prompt:**")
                basic_result_claude = call_claude(basic_prompt)
                st.info(basic_result_claude)
                
                st.markdown("**Advanced Prompt:**")
                advanced_result_claude = call_claude(advanced_prompt)
                st.success(advanced_result_claude)

# TAB 2: Few-Shot Learning
with tab2:
    st.header("📝 Few-Shot Learning")
    st.markdown("""
    Few-shot learning provides examples in your prompt to guide the AI's responses.
    This is especially useful for specific formats, styles, or tasks.
    """)
    
    task = st.selectbox(
        "Task Type:",
        ["Email Classification", "Sentiment Analysis", "Text Transformation"]
    )
    
    if task == "Email Classification":
        examples = """Here are examples of how to classify emails:

Example 1:
Email: "Hi team, please review the Q4 budget by Friday."
Classification: Work - Action Required

Example 2:
Email: "Your Amazon order has shipped!"
Classification: Personal - Notification

Example 3:
Email: "Reminder: Dentist appointment tomorrow at 2pm"
Classification: Personal - Reminder

Now classify this email:"""
        
        user_email = st.text_area("Enter email to classify:", "Hey! Want to grab coffee this weekend?")
        full_prompt = f"{examples}\nEmail: {user_email}\nClassification:"
        
    elif task == "Sentiment Analysis":
        examples = """Analyze the sentiment of these reviews:

Review: "This product exceeded my expectations! Highly recommend."
Sentiment: Positive (Enthusiastic)

Review: "It's okay, does what it says but nothing special."
Sentiment: Neutral

Review: "Waste of money. Broke after one week."
Sentiment: Negative (Frustrated)

Now analyze this review:"""
        
        user_review = st.text_area("Enter review to analyze:", "The features are good but customer service was terrible.")
        full_prompt = f"{examples}\nReview: {user_review}\nSentiment:"
        
    else:  # Text Transformation
        examples = """Transform these sentences into professional business language:

Casual: "Can you send me that thing we talked about?"
Professional: "Could you please send me the document we discussed?"

Casual: "The meeting was kinda boring tbh"
Professional: "The meeting could have been more engaging."

Casual: "Yeah, I'll get to it whenever I can"
Professional: "I will prioritize this task and complete it as soon as possible."

Transform this sentence:"""
        
        user_text = st.text_area("Enter casual text:", "Nah, that idea won't work, we tried it before")
        full_prompt = f"{examples}\nCasual: {user_text}\nProfessional:"
    
    st.code(full_prompt, language="text")
    
    if st.button("🚀 Run Few-Shot Prompt", key="fewshot"):
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.subheader("📊 OpenAI Response")
            with st.spinner("Processing..."):
                result = call_openai(full_prompt)
                st.success(result)
        
        with col_b:
            st.subheader("📊 Claude Response")
            with st.spinner("Processing..."):
                result = call_claude(full_prompt)
                st.success(result)

# TAB 3: Prompt Chaining
with tab3:
    st.header("🔗 Prompt Chaining")
    st.markdown("""
    Prompt chaining breaks complex tasks into steps, using the output of one prompt 
    as input to the next. This improves quality for multi-step workflows.
    """)
    
    topic = st.text_input("Blog topic:", "The future of remote work")
    
    st.subheader("Chain Steps:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Step 1: Brainstorm** \nGenerate key points")
    with col2:
        st.info("**Step 2: Outline** \nOrganize into structure")
    with col3:
        st.info("**Step 3: Write** \nCreate introduction")
    
    if st.button("🚀 Run Prompt Chain", key="chain"):
        # Step 1: Brainstorm
        st.markdown("---")
        st.subheader("Step 1: Brainstorming Key Points")
        prompt1 = f"List 5 key points to discuss about '{topic}' in a blog post. Format as a numbered list."
        
        with st.spinner("Brainstorming..."):
            brainstorm = call_claude(prompt1)
            st.code(prompt1, language="text")
            st.success(brainstorm)
            
        # Step 2: Create Outline
        st.markdown("---")
        st.subheader("Step 2: Creating Outline")
        prompt2 = f"""Based on these key points:

{brainstorm}

Create a blog post outline for '{topic}' with:
- Engaging title
- Introduction hook
- 3-4 main sections
- Conclusion

Format as a clear outline."""
        
        with st.spinner("Creating outline..."):
            outline = call_claude(prompt2)
            st.code(prompt2, language="text")
            st.success(outline)
            
        # Step 3: Write Introduction
        st.markdown("---")
        st.subheader("Step 3: Writing Introduction")
        prompt3 = f"""Using this outline:

{outline}

Write a compelling 2-paragraph introduction for the blog post about '{topic}' that:
- Hooks the reader with a relevant statistic or question
- Establishes why this topic matters
- Previews what the post will cover"""
        
        with st.spinner("Writing introduction..."):
            intro = call_claude(prompt3)
            st.code(prompt3, language="text")
            st.success(intro)

# TAB 4: Chain-of-Thought
with tab4:
    st.header("🧠 Chain-of-Thought Reasoning")
    st.markdown("""
    Chain-of-thought prompting asks the AI to show its reasoning process step-by-step.
    This improves accuracy on complex problems.
    """)
    
    problem_type = st.selectbox(
        "Problem Type:",
        ["Math Word Problem", "Logic Puzzle", "Decision Analysis"]
    )
    
    if problem_type == "Math Word Problem":
        default_problem = "A store sells notebooks for $3 each. If you buy 5 or more, you get 20% off. How much would 7 notebooks cost?"
        problem = st.text_area("Enter problem:", default_problem)
        
        prompt = f"""Solve this problem step by step, showing your reasoning:

{problem}

Please:
1. Identify what we know
2. Determine what we need to find
3. Show each calculation step
4. State the final answer clearly"""

    elif problem_type == "Logic Puzzle":
        default_problem = "Alice is older than Bob. Bob is older than Carol. David is younger than Bob but older than Carol. List the people from oldest to youngest."
        problem = st.text_area("Enter puzzle:", default_problem)
        
        prompt = f"""Solve this logic puzzle by reasoning through it step by step:

{problem}

Please:
1. List what we know
2. Draw logical conclusions from each statement
3. Show your reasoning for each step
4. Present the final answer"""

    else:  # Decision Analysis
        default_problem = "Should a small business invest in AI automation tools? Budget: $10k/year. Team size: 8 people."
        problem = st.text_area("Enter decision scenario:", default_problem)
        
        prompt = f"""Analyze this decision systematically:

{problem}

Please:
1. Identify key factors to consider
2. Analyze pros and cons
3. Consider implementation challenges
4. Provide a reasoned recommendation"""
    
    st.code(prompt, language="text")
    
    col1, col2 = st.columns(2)
    
    if col1.button("🚀 Get OpenAI Reasoning", key="cot_openai"):
        with st.spinner("Reasoning through problem..."):
            result = call_openai(prompt)
            st.success(result)
    
    if col2.button("🚀 Get Claude Reasoning", key="cot_claude"):
        with st.spinner("Reasoning through problem..."):
            result = call_claude(prompt)
            st.success(result)

# Footer
st.markdown("---")
st.markdown("""
### 📚 Learn More About Prompt Engineering

**Key Takeaways:**
- ✅ Be specific and provide context
- ✅ Use examples (few-shot learning)
- ✅ Break complex tasks into steps (chaining)
- ✅ Ask for reasoning (chain-of-thought)
- ✅ Specify format, length, and audience
- ✅ Compare outputs from different models

**Resources:**
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
""")

st.sidebar.markdown("---")
st.sidebar.markdown("Built by Josephine Dorado")
st.sidebar.markdown("[GitHub](https://github.com) • [LinkedIn](https://linkedin.com/in/funksoup)")
