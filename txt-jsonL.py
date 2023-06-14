import json

# Generate a list of dictionaries
lines = []
with open("SHOE_SENTENCES.txt", encoding="utf8") as f:
    for line in f.read().splitlines():
        if line:
            lines.append({"text": line})

# Convert to a list of JSON strings
json_lines = [json.dumps(l) for l in lines]

# Join lines and save to .jsonl file
json_data = '\n'.join(json_lines)
with open('my_file.jsonl', 'w') as f:
    f.write(json_data)