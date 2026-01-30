import panel as pn

pn.extension()

# Text input
name_input = pn.widgets.TextInput(
    name="Your Name",
    placeholder="Enter your name"
)

# Button
submit_button = pn.widgets.Button(
    name="Submit",
    button_type="primary"
)

# Output area
output = pn.pane.Markdown("Please enter your name and click submit.")

# Button event
def on_submit(event):
    if name_input.value.strip():
        output.object = f"👋 Hello **{name_input.value}**, welcome to Panel!"
    else:
        output.object = "⚠️ Please enter a name first."

submit_button.on_click(on_submit)

# Layout
app = pn.Column(
    "# 📝 User Input Example",
    "In this example, we read user input and respond dynamically.",
    name_input,
    submit_button,
    output
)

app.servable()
