# Requirements Traceability

## Overview

This script is for the **Requirements Traceability Assignment** in UC Software Engineering Spring 2026.

The program processes `requirements.txt` which contains Non-Functional Requirements (NFRs) and Functional Requirements (FRs), and performs the following operations:

- **Preprocessing**: Tokenization, stop word removal, stemming, etc.
- **Cosine Similarity Analysis**: Calculates and displays how similar each FR is to each NFR

## Installation and Usage

### Method 1: Using UV (Recommended for WSL)

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone https://github.com/Apollo-717/Requirements_Traceability.git
   cd Requirements_Traceability
   ```

2. **Install UV:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Set up the environment:**
   ```bash
   source $HOME/.local/bin/env
   ```

4. **Sync dependencies:**
   ```bash
   uv sync
   ```

5. **Download required NLTK data:**
   ```bash
   uv run python
   ```
   
   Then in the Python interpreter, run:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   exit()
   ```
   
   Type `exit()` to leave the Python interpreter.

6. **Open in VSCode (optional):**
   ```bash
   code .
   ```

7. **Run the program:**
   ```bash
   uv run python main.py
   ```

### Method 2: Using Python venv

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Apollo-717/Requirements_Traceability.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Requirements_Traceability
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

4. **Activate the virtual environment:**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **Linux/WSL:**
   ```bash
   source .venv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip install nltk
   ```

6. **Download required NLTK data:**
   ```bash
   python
   ```
   
   Then in the Python interpreter, run:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   exit()
   ```
   
   Type `exit()` to leave the Python interpreter.

7. **Open in VSCode (optional):**
   ```bash
   code .
   ```

8. **Run the program:**
   ```bash
   python main.py
   ```

## Requirements

- Python 3.x
- NLTK library
- UV (for Method 1)

## Project Structure

```
Requirements_Traceability/
├── main.py
├── requirements.txt
└── README.md
```

## Course Information

- **Course**: Software Engineering
- **Institution**: UC (University of Cincinnati)
- **Semester**: Spring 2026