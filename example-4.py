
import panel as pn

pn.extension()

# Text input for name
name_input = pn.widgets.TextInput(
    name="Your Name",
    placeholder="Enter your name"
)

# Slider for selecting a value
value_slider = pn.widgets.IntSlider(
    name="Choose a value",
    start=0,
    end=100,
    step=1,
    value=50,
    bar_color="blue"
)

# Output area
output = pn.pane.Markdown("Enter your name and move the slider.")

# Update function
def update_output(event):
    name = name_input.value.strip()
    value = value_slider.value

    if name:
        output.object = f"👋 Hello **{name}**! Your selected value is **{value}**."
    else:
        output.object = f"📊 Current value: **{value}** (enter your name to personalize this message)."

# Watch both widgets
name_input.param.watch(update_output, "value")
value_slider.param.watch(update_output, "value")

# Layout
app = pn.Column(
    "# 🎚️ Slider + Text Input Example",
    "Type your name and move the slider to see a dynamic response.",
    name_input,
    value_slider,
    output
)

app.servable()
