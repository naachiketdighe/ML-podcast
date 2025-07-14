# ML-podcast Data Pipeline & Fine-tuning Overview

This project provides a full pipeline for extracting, processing, and fine-tuning large language models (LLMs) on podcast Q&A data, specifically targeting YouTube podcast content.

---

## 1. Data Extraction & Preprocessing (`preprocessing/get_data.ipynb`)

**Purpose:**  
Automates the process of collecting podcast transcripts from YouTube and converting them into Q&A pairs for LLM training.

**Key Steps:**
- **YouTube API Integration:**  
  Fetches channel and video IDs using the YouTube Data API.
- **Transcript Extraction:**  
  Uses Selenium to automate transcript scraping from [youtube-transcript.io](https://www.youtube-transcript.io/).
  Handles clipboard operations (optimized for MacOS).
- **Q&A Generation:**  
  Sends transcripts to the Gemini API to extract 15–30 Q&A pairs per episode, formatted for Llama 3 fine-tuning.
- **ETL Pipeline:**  
  Iterates over all videos, processes each, and logs failures (e.g., missing/short transcripts).
- **Error Handling:**  
  Skips and logs videos with missing, invalid, or too-short transcripts.

**Outputs:**
- Cleaned Q&A JSON files for each video, ready for LLM training.
- Logs of failed video indices/URLs for troubleshooting.

**Dependencies:**
- `selenium`, `google-api-python-client`, `python-dotenv`, `pyperclip`, `requests`, `google-generativeai`
- ChromeDriver (must match your Chrome version)
- MacOS clipboard utilities (`pbcopy`, `pbpaste`)

---

## 2. Model Fine-tuning (`finetuning/finetuning.py`)

**Purpose:**  
Fine-tunes a Llama 3 (or similar) language model on the extracted Q&A data to create a specialized conversational assistant.

**Key Steps:**
- **Environment Setup:**  
  Installs all required libraries (transformers, datasets, bitsandbytes, trl, colored, accelerate, huggingface_hub, etc.).
- **Data Preparation:**  
  Loads the cleaned Q&A data (CSV/JSON).
  Tokenizes and filters samples (e.g., by token count).
  Splits data into train/validation/test sets and saves them as JSON.
- **Model Loading & Configuration:**  
  Loads a pre-trained Llama 3 model with quantization for efficient training.
  Adds special tokens and prepares the model for parameter-efficient fine-tuning (PEFT/LoRA).
- **Training:**  
  Sets up the Trainer and DataCollator for supervised fine-tuning (SFT).
  Trains the model on the Q&A data.
- **Evaluation & Testing:**  
  Provides utilities for evaluating token distributions and testing the model’s outputs.

**Outputs:**
- A fine-tuned Llama 3 model checkpoint.
- Training/validation/test data splits.
- Plots and statistics on token distribution and dataset characteristics.

**Dependencies:**
- `transformers`, `datasets`, `bitsandbytes`, `trl`, `colored`, `accelerate`, `huggingface_hub`, `matplotlib`, `seaborn`, `scikit-learn`, `torch`, `pandas`, `numpy`

---

## Workflow Summary

1. **Extract Q&A Data:**  
   Use `preprocessing/get_data.ipynb` to fetch, transcribe, and convert YouTube podcast episodes into Q&A pairs.
2. **Prepare & Fine-tune Model:**  
   Use `finetuning/finetuning.py` to process the data, split it, and fine-tune a Llama 3 model for conversational Q&A.

---

## Troubleshooting

- **Selenium/Clipboard Issues:**  
  Run Chrome in non-headless mode if clipboard copying fails.  
  Ensure ChromeDriver matches your browser version.
- **API Errors:**  
  Check API keys and quotas in your `.env` file.
- **Data Quality:**  
  Some videos may lack transcripts or be too short; these are logged for review.

---

## Customization

- Adjust word count thresholds, output directories, and prompt templates as needed in the code.
- Swap out the Llama 3 model for another compatible model by changing the model name in `finetuning.py`.

---

## License

For research and educational use. Please respect the terms of service of all APIs and data sources used.
