# YouTube Video Summarizer

This project is a Flask web application that summarizes YouTube videos. It extracts the transcript of a video using the `YouTubeTranscriptApi`, then uses the `transformers` library to summarize the text using the "facebook/bart-large-cnn" model.

## Features
- Extracts transcript from YouTube videos that have captions.
- Summarizes long YouTube transcripts into concise summaries.
- Simple, user-friendly web interface.

## Requirements

To run this project locally, you'll need the following dependencies:

- Python 3.x
- Flask
- transformers
- youtube-transcript-api
- [Huggingface model](https://huggingface.co/) - `facebook/bart-large-cnn`
