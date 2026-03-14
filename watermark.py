from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(input_path, output_path, text, position, opacity):

    image = Image.open(input_path).convert("RGBA")

    txt_layer = Image.new("RGBA", image.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)

    width, height = image.size

    font_size = max(30, width // 20)
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)

    bbox = draw.textbbox((0,0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    if position == "bottom-right":
        x = width - text_width - 20
        y = height - text_height - 20

    elif position == "bottom-left":
        x = 20
        y = height - text_height - 20

    elif position == "top-right":
        x = width - text_width - 20
        y = 20

    elif position == "top-left":
        x = 20
        y = 20

    elif position == "center":
        x = width // 2 - text_width // 2
        y = height // 2 - text_height // 2

    else:
        x = width - text_width - 20
        y = height - text_height - 20

    # shadow
    draw.text((x+2, y+2), text, fill=(0,0,0,opacity), font=font)

    # main text
    draw.text((x, y), text, fill=(255,255,255,opacity), font=font)

    result = Image.alpha_composite(image, txt_layer)

    result.convert("RGB").save(output_path)
