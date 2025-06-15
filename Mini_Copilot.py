
# 👇 Install dependencies before running anything else
!pip install ipywidgets openai --quiet

# ✨ Import libraries
from IPython.display import display, Markdown
import ipywidgets as widgets
import openai

# 🔐 OpenAI API key placeholder
openai.api_key = "YOUR_API_KEY_HERE"  # Replace with your actual OpenAI key

# ⚙️ Function to call OpenAI API
def query_openai(prompt, role="user"):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": role, "content": prompt}],
            max_tokens=600,
            temperature=0.5
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- Feature 1: Code Generator ---
desc_input = widgets.Textarea(
    placeholder="Describe what code you want...",
    layout=widgets.Layout(width='100%', height='100px')
)
desc_button = widgets.Button(description="Generate Code", button_style='success')
desc_output = widgets.Output()
def on_desc_click(b):
    desc_output.clear_output()
    prompt = f"Write Python code for: {desc_input.value}"
    with desc_output:
        print(query_openai(prompt))
desc_button.on_click(on_desc_click)

# --- Feature 2: Code Explainer ---
explain_input = widgets.Textarea(
    placeholder="Paste your code here...",
    layout=widgets.Layout(width='100%', height='100px')
)
explain_button = widgets.Button(description="Explain Code", button_style='info')
explain_output = widgets.Output()
def on_explain_click(b):
    explain_output.clear_output()
    prompt = f"Explain the following Python code line-by-line:
{explain_input.value}"
    with explain_output:
        print(query_openai(prompt))
explain_button.on_click(on_explain_click)

# --- Feature 3: Bug Fixer ---
bug_input = widgets.Textarea(
    placeholder="Paste buggy code here...",
    layout=widgets.Layout(width='100%', height='100px')
)
bug_button = widgets.Button(description="Fix Code", button_style='warning')
bug_output = widgets.Output()
def on_bug_click(b):
    bug_output.clear_output()
    prompt = f"Find and fix the bugs in this Python code:
{bug_input.value}"
    with bug_output:
        print(query_openai(prompt))
bug_button.on_click(on_bug_click)

# --- Feature 4: Documentation Generator ---
doc_input = widgets.Textarea(
    placeholder="Paste code to add docstrings/comments...",
    layout=widgets.Layout(width='100%', height='100px')
)
doc_button = widgets.Button(description="Generate Docs", button_style='primary')
doc_output = widgets.Output()
def on_doc_click(b):
    doc_output.clear_output()
    prompt = f"Add docstrings and comments to this Python code:
{doc_input.value}"
    with doc_output:
        print(query_openai(prompt))
doc_button.on_click(on_doc_click)

# --- Display UI ---
display(Markdown("## 🤖 Mini Copilot: Coding & Documentation Help"))
display(Markdown("### ✍️ Code Generator"))
display(desc_input, desc_button, desc_output)
display(Markdown("### 🔎 Code Explanation"))
display(explain_input, explain_button, explain_output)
display(Markdown("### 🐛 Bug Fixing Assistant"))
display(bug_input, bug_button, bug_output)
display(Markdown("### 📄 Documentation Generator"))
display(doc_input, doc_button, doc_output)
