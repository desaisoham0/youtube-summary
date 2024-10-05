from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Initialize the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([entry['text'] for entry in transcript])
        return full_text
    except Exception as e:
        return None

def summarize_text(text, summarizer, max_chunk_size=1024):
    if len(text) > max_chunk_size:
        chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        summary = ""
        for chunk in chunks:
            summary_chunk = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summary += summary_chunk[0]['summary_text'] + " "
        return summary.strip()
    else:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['youtube_url']
        video_id = video_url.split("v=")[1]
        transcript_text = get_video_transcript(video_id)

        if transcript_text:
            summary = summarize_text(transcript_text, summarizer)
            return render_template('index.html', summary=summary, video_url=video_url)
        else:
            return render_template('index.html', error="Could not fetch transcript. Make sure the video has captions.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
