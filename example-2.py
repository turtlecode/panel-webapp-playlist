
import panel as pn

pn.extension()

# Create a button
button = pn.widgets.Button(
    name="Click Me",
    button_type="primary"
)

# Create a text area for output
output = pn.pane.Markdown("Waiting for a click...")

# Button click event
def on_button_click(event):
    output.object = "🎉 Button clicked! Welcome to Panel."

button.on_click(on_button_click)

# Layout
app = pn.Column(
    "# 🔘 Button Click Interaction",
    "This is our first interactive Panel example.",
    button,
    output
)

app.servable()
