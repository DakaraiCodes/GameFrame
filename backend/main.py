import cv2
import pytesseract
import json
from io_utils import save_game_data
from models import build_game_data
from ocr import extract_text
from vision import analyze_scoreboard

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def main():
    image_path = "../data/sample_game_2.jpg"
    output_path = "../data/sample_game_data.json"

    regions = analyze_scoreboard(image_path)
    ocr_data = extract_text(regions)
    game_data = build_game_data(ocr_data)
    save_game_data(game_data, output_path)

    print(game_data)

def save_game_data(game_data, output_path):
    with open(output_path, "w") as file:
        json.dump(game_data, file, indent=4)

    print(f"Saved game data to: {output_path}")

image_path = "../data/sample_game_2.jpg"

regions = analyze_scoreboard(image_path)
ocr_data = extract_text(regions)
game_data = build_game_data(ocr_data)

print(ocr_data)
print(game_data)

output_path = "../data/sample_game_data.json"
save_game_data(game_data, output_path)

if __name__ == "__main__":
    main()

