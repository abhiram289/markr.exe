from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(input_path, output_path, text):

    image = Image.open(input_path).convert("RGBA")

    txt_layer = Image.new("RGBA", image.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)

    width, height = image.size

    font = ImageFont.load_default()

    bbox = draw.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # bottom-right position
    x = width - text_width - 20
    y = height - text_height - 20

    # make it VERY visible
    draw.text((x,y), text, fill=(255,0,0,255), font=font)

    result = Image.alpha_composite(image, txt_layer)

    result.convert("RGB").save(output_path)
