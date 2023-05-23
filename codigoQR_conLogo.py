import qrcode
from PIL import Image

def create_qr_code_with_logo(url, output_path, qr_fill_color="black", qr_back_color="white", logo_path=None, logo_width=None, qr_version=1, qr_border=4, qr_box_size=10, qr_pixel_size=500):
    # Crea el código QR sin el logotipo
    qr = qrcode.QRCode(
        version=qr_version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=qr_box_size,
        border=qr_border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=qr_fill_color, back_color=qr_back_color)

    if logo_path:
        # Abre el logotipo de la empresa con transparencia
        logo = Image.open(logo_path).convert("RGBA")

        # Redimensiona el logotipo con el ancho deseado, manteniendo la proporción
        if logo_width:
            logo_width = min(logo_width, qr_img.size[0])  # Limita el ancho máximo del logotipo
            logo_height = int(logo_width * logo.size[1] / logo.size[0])
            logo = logo.resize((logo_width, logo_height))

        # Calcula la posición del logotipo en el centro del código QR
        qr_img = qr_img.convert("RGBA")
        pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

        # Fusiona el logotipo con el código QR sin cambiar el fondo transparente del logotipo
        qr_img.paste(logo, pos, logo)

    # Redimensiona el código QR al tamaño deseado en píxeles
    qr_img = qr_img.resize((qr_pixel_size, qr_pixel_size), resample=Image.LANCZOS)

    # Guarda el código QR con o sin logotipo en un archivo
    qr_img.save(output_path, format='PNG', compress_level=1, dpi=(600, 600))

# Ejemplo de uso
url = "https://bordafax.com/"
logo_path = "logo1.png"
output_path = "codigo.png"
qr_fill_color = "#383f44"  # Color de relleno del código QR
qr_back_color = "#e2e2e2"  # Color de fondo del código QR
logo_width = 100  # Ancho deseado del logotipo (ajústalo según tus necesidades)
qr_version = 1  # Versión del código QR (controla el tamaño y la capacidad de almacenamiento)
qr_border = 2  # Tamaño del margen del código QR
qr_box_size = 12  # Tamaño de cada caja del código QR
qr_pixel_size = 40000  # Tamaño del código QR en píxeles

print(f"CREANDO CODIGO QR CON LINK WEB A: {url}\n \n")
create_qr_code_with_logo(url, output_path, qr_fill_color, qr_back_color, logo_path, logo_width, qr_version, qr_border, qr_box_size, qr_pixel_size)

print(f'Codigo QR terminado. Archivo creado: {output_path} \n \nFIN DEL PROCESO')