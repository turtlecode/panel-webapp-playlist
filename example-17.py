
import panel as pn
import tempfile

pn.extension()

video_pane = pn.pane.Video(
    None,
    width=640,
    height=360,
    loop=False
)

file_input = pn.widgets.FileInput(
    name="Upload a video file",
    accept=".mp4"
)

title = pn.pane.Markdown("## 🎬 Upload and Play Video in Panel")
info = pn.pane.Markdown(
    """
Upload an MP4 video using the file uploader below.
Once uploaded, the video will automatically appear and start playing.
"""
)

def update_video(event):
    if file_input.value:
        # Save uploaded file temporarily
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_file.write(file_input.value)
        temp_file.close()

        # Update video source
        video_pane.object = temp_file.name

file_input.param.watch(update_video, "value")

app = pn.Column(
    title,
    info,
    file_input,
    video_pane
)

app.servable()
