from PIL import Image, ImageDraw, ImageFont
import string

# Список ASCII-символов, которые будут использоваться для рисования

ascii_chars = "*:'#.,- "
def scale_image(img, new_width=100):
    # Изменяем размер изображения
    width, height = img.size
    ratio = height / width / 1 # 1.65 - это коэффициент, чтобы сохранить пропорции
    new_height = int(new_width * ratio)
    return img.resize((new_width, new_height))


def grayify(img):
    # Конвертируем изображение в оттенки серого
    return img.convert('L')


def pixels_to_ascii(img):
    # Преобразуем пиксели в ASCII-символы
    pixels = img.getdata()
    ascii_str = ''.join([ascii_chars[pixel // 36] for pixel in pixels])
    return ascii_str


def draw_ascii_text(ascii_str, img_width, font_size=5):
    # Создаем новое изображение для рисования ASCII-текста
    img_height = len(ascii_str) // img_width
    image = Image.new('RGB', (img_width * font_size, img_height * font_size),
                      color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Рисуем ASCII-текст на изображении
    for i, char in enumerate(ascii_str):
        x = (i % img_width) * font_size
        y = (i // img_width) * font_size
        draw.text((x, y), char, font=font, fill=(255, 255, 255))

    return image


def main(image_path, output_path, width=100):
    try:
        # Открываем исходное изображение
        img = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Масштабируем изображение
    img = scale_image(img, width)
    # Конвертируем в оттенки серого
    img = grayify(img)
    # Преобразуем пиксели в ASCII-символы
    ascii_str = pixels_to_ascii(img)
    # Рисуем ASCII-текст на новом изображении
    ascii_img = draw_ascii_text(ascii_str, img.width)
    # Сохраняем новое изображение
    ascii_img.save(output_path)
    print(f"Изображение успешно сохранено как {output_path}")


if __name__ == "__main__":
    image_path = '1.png'  # Замените на путь к вашему изображению
    output_path = 'ascii_art.png'  # Путь для сохранения нового изображения
    main(image_path, output_path)