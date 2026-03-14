from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(input_path, output_path, text, position, opacity):

    image = Image.open(input_path).convert("RGBA")

    txt_layer = Image.new("RGBA", image.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)

    width, height = image.size

    font_size = min(45, max(18, width // 50))

    font = ImageFont.truetype("fonts/SpaceMono-Regular.ttf", font_size)

    bbox = draw.textbbox((0,0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    padding = int(min(width, height) * 0.04)

    if position == "bottom-right":
        x = width - text_width - padding
        y = height - text_height - padding

    elif position == "bottom-left":
        x = padding
        y = height - text_height - padding

    elif position == "top-right":
        x = width - text_width - padding
        y = padding

    elif position == "top-left":
        x = padding
        y = padding

    elif position == "center":
        x = width // 2 - text_width // 2
        y = height // 2 - text_height // 2

    else:
        x = width - text_width - padding
        y = height - text_height - padding

    draw.text((x+1, y+1), text, fill=(0,0,0,80), font=font)

    draw.text((x, y), text, fill=(255,255,255,120), font=font)

    result = Image.alpha_composite(image, txt_layer)

    result.convert("RGB").save(output_path)
