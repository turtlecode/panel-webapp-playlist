import panel as pn

pn.extension()

# Text area widget (CORRECT NAME)
text_area = pn.widgets.TextAreaInput(
    name="Your Message",
    placeholder="Write something here...",
    height=200
)

# Submit button
submit_button = pn.widgets.Button(
    name="Submit",
    button_type="primary"
)

# Output area
output = pn.pane.Markdown("Your message will appear here after you click Submit.")

# Button event
def submit_text(event):
    text = text_area.value.strip()

    if text:
        output.object = f"📝 **Your message:**\n\n{text}"
    else:
        output.object = "⚠️ Please write something in the text area first."

submit_button.on_click(submit_text)

# Layout
app = pn.Column(
    "# ✍️ TextArea Example",
    "Write a message in the box below and click submit.",
    text_area,
    submit_button,
    output
)

app.servable()
