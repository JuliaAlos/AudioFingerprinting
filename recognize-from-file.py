import sys
from libs.reader_file import FileReader  # Ensure this is the correct import path

# Check if the user provided a file path as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 recognize-from-file.py <path_to_audio_file>")
    sys.exit(1)  # Exit the script if no file path is provided

# Get the file path from the command-line arguments
filename = sys.argv[1]

# Optional: You can also prompt for the number of seconds if needed
seconds_input = input("Please enter the number of seconds to limit (or press Enter for no limit): ")
seconds = int(seconds_input) if seconds_input else None  # Convert to int or None if not provided

# Initialize FileReader with the filename
r = FileReader(filename)

# Parse the audio file
audio_info = r.parse_audio(limit=seconds)  # Limit to the first 'seconds' seconds if desired

# Check if audio_info was successfully parsed
if audio_info:
    song = audio_info['songname']  # Extract the song name from the parsed info
    print(f"Recognized song: {song}")
else:
    print("Failed to parse audio.")
