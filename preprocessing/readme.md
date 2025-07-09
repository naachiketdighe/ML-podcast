# Unapologetic Man Podcast Transcripts Dataset

## Overview

This repository contains a comprehensive JSON dataset of podcast transcript segments from the **Unapologetic Man** podcast, featuring Mark Singh. The data has been parsed into machine-readable JSON segments, each segment capturing a portion of the transcript along with metadata (ID, topic, speaker role, etc.).

## Data Source

- Original transcripts were obtained via the YouTube Transcript API service at [https://www.youtube-transcript.io/](https://www.youtube-transcript.io/).
- Each episode's raw transcript was fetched programmatically using the API endpoints provided by the service.

## Conversion Process

1. **Fetch Transcripts**  
   Episode transcripts were retrieved as plain text using the YouTube Transcript API.
2. **Segment Parsing**  
   The raw text was split into logical segments, with each segment containing:
   - `text`: The transcript snippet including system/user/assistant markers.
   - `id`: A unique segment identifier (e.g., `ep001_seg001`).
   - `topic`: A short topic label for quick reference.
3. **Machine-Readable JSON**  
   The segments were formatted into a valid JSON array. This conversion and cleanup were performed using ChatGPT, ensuring consistent annotation and metadata.

## File Structure

- `data.json` — The primary dataset file containing all transcript segments.
- `README.md` — This documentation file.

## Usage

You can load `data.json` in your application or analysis environment for tasks like:

- Natural language processing and topic modeling
- Training or fine-tuning conversational AI
- Building searchable transcript viewers

Example (Python):

```python
import re

input_file = "data.json"
output_file = "data_preprocessed.json"

with open(input_file, "r") as f:
    content = f.read()

objects = re.findall(r'(\{.*?\})(?=\s*\{|\s*$)', content, re.DOTALL)

# Join with commas and wrap in brackets
json_array = "[\n" + ",\n".join(objects) + "\n]"

with open(output_file, "w") as f:
    f.write(json_array)

print(f"Fixed JSON written to {output_file}")
```
