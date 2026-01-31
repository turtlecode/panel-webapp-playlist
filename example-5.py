
import panel as pn

pn.extension()

# Select dropdown
color_select = pn.widgets.Select(
    name="Choose your favorite color",
    options=["Red", "Blue", "Green", "Yellow", "Purple"],
    value="Blue"
)

# Output area
output = pn.pane.Markdown("Select a color from the dropdown.")

# Update function
def update_output(event):
    output.object = f"🎨 You selected: **{event.new}**"

# Watch the dropdown
color_select.param.watch(update_output, "value")

# Layout
app = pn.Column(
    "# 📋 Select Dropdown Example",
    "Choose a color to see a dynamic response.",
    color_select,
    output
)

app.servable()
