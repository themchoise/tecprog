import json

def read_pseudocode(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def generate_excalidraw_json(steps):
    excalidraw_elements = []
    y_position = 100
    x_position = 500
    width = 150
    height = 50
    element_id = 1

    # Generate elements for each step
    for step in steps:
        text = step.replace(",", "\n")  # Replace commas with newlines for better formatting
        element = {
            "id": f"element_{element_id}",
            "type": "rectangle",
            "x": x_position,
            "y": y_position,
            "width": width,
            "height": height,
            "angle": 0,
            "strokeColor": "#000000",
            "backgroundColor": "#00ccff",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "seed": 1,
            "version": 1,
            "versionNonce": 1,
            "isDeleted": False,
            "boundElementIds": None,
            "updated": 1,
            "link": None,
            "locked": False,
            "text": text,
            "fontSize": 16,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "baseline": 25,
            "containerId": None,
            "originalText": text
        }
        excalidraw_elements.append(element)

        # Add arrow between elements
        if element_id > 1:
            arrow = {
                "id": f"arrow_{element_id - 1}",
                "type": "arrow",
                "x": x_position + width / 2,
                "y": y_position - height,
                "width": 0,
                "height": height,
                "angle": 0,
                "strokeColor": "#000000",
                "backgroundColor": "#00ccff",
                "fillStyle": "solid",
                "strokeWidth": 1,
                "strokeStyle": "solid",
                "roughness": 1,
                "opacity": 100,
                "groupIds": [],
                "seed": 1,
                "version": 1,
                "versionNonce": 1,
                "isDeleted": False,
                "boundElementIds": None,
                "updated": 1,
                "link": None,
                "locked": False,
                "points": [[0, 0], [0, height]],
                "lastCommittedPoint": None,
                "startBinding": None,
                "endBinding": None,
                "startArrowhead": None,
                "endArrowhead": "arrow"
            }
            excalidraw_elements.append(arrow)

        y_position += 100
        element_id += 1

    excalidraw_json = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": excalidraw_elements
    }

    return excalidraw_json

def save_excalidraw_json(json_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=2)

def main():
    # Path to the input pseudocodigo file
    input_file = 'pseudocodigo.txt'
    # Path to the output Excalidraw JSON file
    output_file = 'excalidraw_output.json'

    # Read pseudocode from file
    pseudocode_steps = read_pseudocode(input_file)

    # Generate Excalidraw JSON
    excalidraw_json = generate_excalidraw_json(pseudocode_steps)

    # Save Excalidraw JSON to file
    save_excalidraw_json(excalidraw_json, output_file)

    print(f"Excalidraw JSON saved to {output_file}")

if __name__ == '__main__':
    main()
