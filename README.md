# AI Coding Agent 🤖
An autonomous coding assistant that leverages the Gemini API to interact directly with your local file system.

# ✨ Features
The agent interprets natural language prompts to perform complex file operations within a controlled sandbox:

File Discovery: List files and directories.

Content Retrieval: Read and analyze file contents.

Code Generation: Create or overwrite files with new logic.

Execution: Run Python scripts and observe output in real-time.

🚀 Quick Start
1. Installation
Bash
# Clone and sync dependencies
uv sync 
2. Configuration
Create a .env file in the root directory:

Bash
echo "GEMINI_API_KEY=your_actual_key_here" > .env
3. Usage
Bash
# Basic prompt
python main.py "list all Python files"

# Detailed execution
python main.py "read main.py and explain the logic" --verbose
🛠 Project Structure
main.py – The primary entry point.

call_function.py – Logic for tool routing and API responses.

prompts.py – System instructions and AI personality.

config.py – Settings for WORKING_DIR and MAX_CHARS limits.

functions/ – Implementation of the core agent tools.

calculator/ – The default sandbox workspace (safe zone).

🧠 How It Works
Input: You provide a natural language task.

Reasoning: Gemini determines which tool is needed (e.g., list_files).

Action: The agent executes the Python function locally.

Feedback: Results are fed back to the model to determine the next step.

Completion: The loop continues until the goal is met.

📋 Requirements
Python: 3.12+

API Key: Valid Google Gemini API Key

Environment: Best used within a virtual environment (uv or venv)