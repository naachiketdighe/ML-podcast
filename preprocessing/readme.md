# YouTube Podcast Data Extraction & Q&A Generation Pipeline

This notebook (`get_data.ipynb`) is designed to automate the extraction of podcast transcripts from YouTube channels and convert them into Q&A pairs suitable for LLM (Llama 3) fine-tuning. It leverages the YouTube API, Selenium for transcript scraping, and the Gemini API for Q&A generation.

---

## Features
- **YouTube API Integration:** Fetches channel and video IDs from a given channel name or handle.
- **Automated Transcript Extraction:** Uses Selenium to scrape transcripts from [youtube-transcript.io](https://www.youtube-transcript.io/) for each video.
- **Clipboard Automation:** Handles transcript copying via clipboard (with MacOS support).
- **Q&A Generation:** Sends transcripts to Gemini API to extract Q&A pairs in a format suitable for Llama 3 fine-tuning.
- **ETL Pipeline:** Processes multiple videos in sequence, with error handling and logging of failed attempts.
- **Robust Error Handling:** Skips videos with missing/short/invalid transcripts and logs failed URLs/indices for later review.

---

## Setup

### 1. Environment & Dependencies
- Python 3.8+
- Install required packages:
  - `pip install selenium google-api-python-client python-dotenv pyperclip requests`
  - For Gemini API: `pip install google-generativeai`
- **MacOS only:** Clipboard automation uses `pbcopy`/`pbpaste` (pre-installed on Mac).
- **ChromeDriver:** Download and place the [ChromeDriver](https://sites.google.com/chromium.org/driver/) binary in your PATH.
- **.env file:** Place your API keys in a `.env` file in the root directory:
  ```
  YOUTUBE_API_KEY=your_youtube_api_key
  GEMINI_API_KEY=your_gemini_api_key
  ```

### 2. Notebook Structure
- **YouTube API Section:**
  - Validates API key, fetches channel ID, and retrieves all video IDs from the channel.
- **Transcript Extraction:**
  - Uses Selenium to open [youtube-transcript.io](https://www.youtube-transcript.io/), enters each video URL, and copies the transcript to the clipboard.
  - Handles clipboard via `pyperclip` or subprocess (`pbcopy`/`pbpaste`).
- **Q&A Generation:**
  - Sends transcript to Gemini API with a prompt to extract 15-30 Q&A pairs.
  - Saves the output as JSON files for each video.
- **ETL Loop:**
  - Iterates over all video URLs, processes each, and logs failures.

---

## Usage
1. **Set up your `.env` file** with the required API keys.
2. **Install dependencies** and ensure ChromeDriver is available.
3. **Run the notebook** step by step:
   - Fetch video URLs from the target channel.
   - Run the Selenium-based transcript extraction for each video.
   - Generate Q&A pairs using Gemini API.
   - Outputs are saved in the `data/` directory.
4. **Review failed indices/URLs** (printed/logged) for any videos that could not be processed (e.g., too short, no transcript, Selenium errors).

---

## Troubleshooting
- **Clipboard Issues:**
  - If transcripts are not copied, try running Chrome in non-headless mode.
  - Ensure `pbcopy`/`pbpaste` are available (MacOS only).
  - On other OS, adapt clipboard handling as needed.
- **Selenium/ChromeDriver Errors:**
  - Ensure ChromeDriver version matches your Chrome browser.
  - If you see `stale element reference` or similar errors, try increasing wait times or running in visible (non-headless) mode.
- **API Errors:**
  - Check your API keys and quota.
  - Ensure `.env` is loaded correctly.
- **Transcript Quality:**
  - Some videos may not have transcripts or may be too short; these are skipped and logged.

---

## Customization
- **Word Count Threshold:**
  - The script skips transcripts with fewer than 170 words (adjustable in the code).
- **Output Location:**
  - Change the output directory as needed (currently `data/`).
- **Prompt/Template:**
  - Modify the Gemini prompt for different Q&A extraction styles or LLM formats.

---

## Credits
- [youtube-transcript.io](https://www.youtube-transcript.io/) for transcript scraping.
- Google Gemini API for Q&A generation.
- YouTube Data API for video metadata.

---

## License
This notebook is for research and educational purposes. Please respect the terms of service of all APIs and websites used. 