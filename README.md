**Repository Documentation Tool**

---

**Description:**
The Repository Documentation Tool is a versatile application designed to simplify the process of documenting the structure and contents of GitHub repositories. It offers both a Graphical User Interface (GUI) and a command-line interface, catering to users with different preferences and requirements. Whether you prefer a user-friendly interface or command-line efficiency, this tool has you covered.

---

**Features:**

1. **Graphical User Interface (GUI):**
   - Intuitive interface for easy navigation and usage.
   - Input fields for specifying the repository path, output file, and optional settings.
   - Browse buttons for selecting directories and files.
   - Option to ignore settings files for a cleaner output.
   - Progress bar for visual feedback during documentation generation.
   - Generate Report button to initiate the documentation process.
   
2. **Command-Line Interface (CLI):**
   - Flexibility to run documentation generation from the command line.
   - Supports various command-line arguments for customization.
   - Ability to specify repository path, output file, ignored files/types, and more.
   - Suitable for automation and integration into scripts or workflows.

3. **Repository Documentation Generation:**
   - Comprehensive documentation of repository structure and contents.
   - Tree-like representation of directory structure for easy visualization.
   - Inclusion of file contents with proper formatting and indentation.
   - Support for both plain text and DOCX output formats.
   - Error handling for file reading and processing.

4. **PyQt5 Text Editor:**
   - Simple text editor with Python syntax highlighting.
   - Line numbering for better code navigation and reference.
   - Based on QsciScintilla for advanced text editing features.
   - Provides a convenient environment for viewing and editing code files.

---

**Usage:**

1. **Graphical User Interface (GUI):**
   - Run the application and fill in the required fields (repository path, output file, etc.).
   - Optionally, select the "Ignore Settings Files" checkbox to exclude common settings files from documentation.
   - Click the "Generate Report" button to start the documentation process.
   - Monitor the progress using the progress bar, and wait for the completion message.

2. **Command-Line Interface (CLI):**
   - Navigate to the directory containing the `repo2txt.py` script.
   - Use the command `python repo2txt.py` followed by appropriate arguments to customize documentation generation.
   - Refer to the provided usage instructions and examples for guidance on command-line usage.

3. **PyQt5 Text Editor:**
   - Run the text editor application and start editing Python code or any text files.
   - Enjoy syntax highlighting, line numbering, and other text editing features provided by the editor.

---

**Requirements:**

- Python 3.x
- tkinter (for GUI)
- PyQt5 (for text editor)
- docx (for DOCX file handling)
- QScintilla (for text editor functionality)
- Other dependencies as specified in the code

---

**Authors:**

- Miguel Oliveira

---

---

**Disclaimer:**

This application is provided as-is, without any warranty or guarantee of its performance or suitability for any specific purpose. Users are advised to use it responsibly and verify its results before relying on them for critical tasks.
