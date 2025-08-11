import sys
import argparse
import os
import google.generativeai as genai
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# This script is part of a Cybersecurity Detection Framework that uses AI
# to provide feedback on detection rules to improve coverage and quality.
# It accepts a YAML file as input containing detection parameters and
# generates AI-powered feedback for detection improvement.
#
# To install the required libraries, run:
# pip install google-generativeai pyyaml python-dotenv
#
# To use this script, create a YAML file like this (e.g., detection_config.yml):
# title: "Suspicious PowerShell Execution with Encoded Commands"
# description: "Detects PowerShell execution with base64 encoded commands"
# sql_search: "SELECT * FROM security_logs WHERE process_name = 'powershell.exe'"
# source_table: "security_logs"
#
# Then run the script from your terminal like this:
# python3 detection_test_script.py --yaml-file detection_config.yml
#
# For authentication, you need to set your Gemini API key:
# 1. Get your API key from https://makersuite.google.com/app/apikey
# 2. Set it as an environment variable: export GEMINI_API_KEY="your-api-key-here"
# 3. Or create a .env file with: GEMINI_API_KEY=your-api-key-here

def validate_api_key(api_key):
    """
    Validate the API key format and length.
    """
    if not api_key:
        return False, "API key is required"
    
    if len(api_key) < 20:
        return False, "API key appears to be too short"
    
    if not api_key.startswith('AI'):
        return False, "API key should start with 'AI'"
    
    return True, "API key format is valid"

def validate_detection_config(config):
    """
    Validate that all required detection parameters are present.
    """
    required_fields = ['title', 'description', 'sql_search', 'source_table']
    missing_fields = []
    
    for field in required_fields:
        if field not in config or not config[field]:
            missing_fields.append(field)
    
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    return True, "All required fields present"

def generate_detection_prompt(config):
    """
    Generate the cybersecurity detection improvement prompt.
    """
    prompt = (
        f"I am a cyber security detection engineer developing a new detection using spark SQL for databricks "
        f"to search across a cyber datalake. I am looking for you to provide the top three most insightful "
        f"feedbacks you can to improve my detections coverage and quality to maximize True positive outcomes. "
        f"Based on the description '{config['description']}' and considering the source log table '{config['source_table']}', "
        f"please help me improve my title from '{config['title']}' and SQL search '{config['sql_search']}' with your top three feedback tips. "
        f"Please keep them under two sentences long."
    )
    return prompt

def main():
    """
    Parses command-line arguments, initializes Gemini AI, and gets AI feedback
    for cybersecurity detection improvement using values from a YAML file.
    """
    # Create an argument parser to handle command-line options
    parser = argparse.ArgumentParser(description="Get AI-powered feedback for cybersecurity detection improvement using a YAML config file.")
    parser.add_argument("--yaml-file", type=str, required=True,
                        help="Path to the YAML file containing detection parameters.")
    parser.add_argument("--model", type=str, default="gemini-1.5-flash",
                        help="Gemini model to use (default: gemini-1.5-flash)")
    parser.add_argument("--api-key", type=str,
                        help="Gemini API key (overrides environment variable)")
    args = parser.parse_args()

    # Get API key from command line argument or environment variable
    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    
    # Validate API key
    is_valid, validation_message = validate_api_key(api_key)
    if not is_valid:
        print(f"Error: {validation_message}")
        print("Please set your Gemini API key:")
        print("1. Get your API key from https://makersuite.google.com/app/apikey")
        print("2. Set it as an environment variable: export GEMINI_API_KEY='your-api-key-here'")
        print("3. Or create a .env file with: GEMINI_API_KEY=your-api-key-here")
        print("4. Or pass it directly: --api-key your-api-key-here")
        sys.exit(1)

    # Configure Gemini AI
    try:
        genai.configure(api_key=api_key)
        print(f"Using Gemini AI model: {args.model}")
    except Exception as e:
        print(f"Error configuring Gemini AI: {e}")
        sys.exit(1)

    # Load and parse the YAML file
    try:
        with open(args.yaml_file, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: YAML file not found at '{args.yaml_file}'.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)

    # Validate detection configuration
    is_valid, validation_message = validate_detection_config(config)
    if not is_valid:
        print(f"Error: {validation_message}")
        print("Please ensure your YAML file contains all required fields:")
        print("- title: Detection rule title")
        print("- description: What the detection is looking for")
        print("- sql_search: The SQL search query")
        print("- source_table: The source log table to search")
        sys.exit(1)

    # Generate the detection improvement prompt
    final_prompt = generate_detection_prompt(config)

    # Initialize the generative model
    try:
        model = genai.GenerativeModel(args.model)
    except Exception as e:
        print(f"Error initializing model '{args.model}': {e}")
        print("Available models: gemini-1.5-flash, gemini-1.5-pro, gemini-1.0-pro")
        sys.exit(1)

    print("🔒 Cybersecurity Detection Framework - AI Feedback Generator")
    print("=" * 60)
    print(f"📋 Detection Title: {config['title']}")
    print(f"📝 Description: {config['description']}")
    print(f"🔍 Source Table: {config['source_table']}")
    print(f"💻 SQL Search: {config['sql_search']}")
    print("=" * 60)
    print(f"\n🤖 Sending prompt to '{args.model}' for AI feedback...")
    print("\n📤 Generated Prompt:")
    print("-" * 40)
    print(final_prompt)
    print("-" * 40)

    try:
        # Generate content from the model
        response = model.generate_content(final_prompt)

        # Print the model's response text
        print("\n🎯 AI Feedback for Detection Improvement:")
        print("=" * 60)
        print(response.text)
        print("=" * 60)
        
        # Print usage information if available
        if hasattr(response, 'usage_metadata'):
            usage = response.usage_metadata
            print(f"\n📊 Token Usage: {usage.prompt_token_count} prompt tokens, {usage.candidates_token_count} response tokens")
            
    except Exception as e:
        print(f"Error getting a response from the model: {e}")
        print("Please check your API key and internet connection.")
        sys.exit(1)

if __name__ == "__main__":
    main()
