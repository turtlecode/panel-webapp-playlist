
import panel as pn

pn.extension()

# ------------------------
# FILE UPLOAD
# ------------------------
file_input = pn.widgets.FileInput(
    name="Upload a Text File",
    accept=".txt"
)

# Text editor (to modify the file)
text_editor = pn.widgets.TextAreaInput(
    name="Edit your file content",
    rows=10
)

# Download button
download_button = pn.widgets.Button(
    name="Download Modified File",
    button_type="primary"
)

# Output / status message
status = pn.pane.Markdown("Upload a .txt file to begin.")

# When file is uploaded, read and display content
def load_file(event):
    if file_input.value:
        content = file_input.value.decode("utf-8")
        text_editor.value = content
        status.object = "📄 File loaded! You can now edit it."

file_input.param.watch(load_file, "value")

# Download function
def download_file(event):
    modified_text = text_editor.value

    with open("modified_file.txt", "w", encoding="utf-8") as f:
        f.write(modified_text)

    status.object = "✅ File saved as **modified_file.txt** in your working directory."

download_button.on_click(download_file)

# Layout
app = pn.Column(
    "# 📁 File Upload, Edit & Download",
    "Upload a text file, edit it, and download the modified version.",
    file_input,
    text_editor,
    download_button,
    status
)

app.servable()
