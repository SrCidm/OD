import reflex as rx  # Importing the reflex library

def navbar():
    # Creating GitHub and YouTube links with icons
    github_link = rx.link(rx.icon("github", size=40, color="white", background_color="black", border_radius="50px", border="1px solid"), href="https://github.com/srcidm", target="_blank", style={"margin-right": "10px"})
    youtube_link = rx.link(rx.icon("youtube", size=40, color="black", background_color="red", border_radius="50px", border="1px solid"), href="https://www.youtube.com/@ofertasdestacadas", target="_blank")

    # Styling the navigation bar
    return rx.hstack(
        rx.container(
            rx.image(
                src="/titulo.png",
                width="600px",
                height="auto",
                border_radius="15px 50px",
                border="5px solid #16161d",
                box_shadow="0px 0px 10px 0px rgba(0,0,0,0.75)"
            ),
            align="center",
            flex="none",
            width="100%",
            height="100%",
            background_color="#fe0090",
            padding="1em",
            top="0px",
            z_index="5",
            border_radius="5px",
        ),
        rx.container(
            github_link,
            youtube_link,
            align="center",
            justify_content="space-between",
            position="fixed",
            top="90px",
            right="10px",
            z_index="100",
            flex="display",
        ),
        position="sticky",
        top="0px",
        border_radius="7px",
        border="2px solid #fff",
        z_index="100",
        margin_right="auto"
    )

videos_info = [
    {"title": "Funda Jacquard para Sofa", "description": "La funda de sofá jacquard de Elabore es la respuesta a sus necesidades.", "product_link": "https://amzn.to/3RrJvfU", "youtube_link": "https://www.youtube.com/shorts/3-6okwEVo7k"},
    {"title": "Dispensador de Enjuague Bucal", "description": " Ingenioso dispositivo, equipado con tecnología de detección magnética.", "product_link": "https://amzn.to/3NzIEbQ", "youtube_link": "https://www.youtube.com/shorts/Z23iD6McpCE"},
    {"title": "Cereales Lacor - 62597", "description": "Diseño inteligente y funcional, este dispensador doble ofrece una capacidad total de 7 litros.", "product_link": "https://amzn.to/3NAuHKV", "youtube_link": "https://www.youtube.com/shorts/bg54QsafXWM"},
    {"title": "HOVERAir X1", "description": "Cámara de vuelo automático que redefine la portabilidad y la simplicidad.", "product_link": "https://amzn.to/3v4P4cR", "youtube_link": "https://www.youtube.com/shorts/4NWx1pMd0ZA"},
    {"title": "Ivation EZ-Bed", "description": "¿Tu primo del otro lado del mundo ha decidido hacer una parada sorpresa en tu casa? No te preocupes, porque el Ivation EZ-Bed es tu solución con estilo.", "product_link": "https://amzn.to/41k2vkQ", "youtube_link": "https://www.youtube.com/shorts/7ve3bb79h5Y"},
    {"title": "Gadget para Envolver Regalos", "description": " Descubre la ventaja de ahorro de tiempo que estos clips aportan a tu rutina de embalaje, convirtiéndola en una tarea rápida y eficiente. ", "product_link": "https://amzn.to/47FSbpJ", "youtube_link": "https://www.youtube.com/shorts/hZ1PJzq1FYg"},
    {"title": "Caja de Almacenamiento Impermeable para Ducha", "description": "ofrece una solución innovadora y práctica para quienes desean disfrutar de su teléfono mientras se bañan o cocinan sin preocuparse por el agua.", "product_link": "https://amzn.to/47U5F0Y", "youtube_link": "https://www.youtube.com/shorts/1s1aSmHU6Yo"},
    {"title": "Aspirador portátil 3 en 1", "description": "Este dispositivo compacto y ligero pesa solo 0,45 kg, haciéndolo extremadamente portátil y fácil de manejar.", "product_link": " https://amzn.to/40Y7jwk", "youtube_link": "https://www.youtube.com/shorts/sqd80hB-pzA"},
    {"title": "Bandeja para hielo portátil", "description": " Con una capacidad de 700 ml cuando está cerrada y 1,4 litros cuando está abierta, esta botella versátil se adapta a tus necesidades en cualquier lugar.", "product_link": "https://amzn.to/3N5Jahz", "youtube_link": "https://www.youtube.com/shorts/z9jw_pYQ6Yc"},
]

def video_component(title, description, product_link, youtube_link):
    # Creating a video component with title, description, and links
    return rx.container(
        rx.video(
            url=youtube_link,
            width="400px",
            height="300px",
            z_index="1"
        ),
        rx.container(
            rx.heading(title, size="3", color="white", marginLeft="10px"),  # Heading for video title
            rx.text(description, color="white", marginLeft="20px"),  # Text description
            rx.link(rx.button("Ver en Amazon"), color_scheme="orange", cursor="pointer", href=product_link, color="white", target="_blank", marginLeft="20px"),  # Link to Amazon product
            spacing="2",
            padding="auto",
            background_color="#760de9",
            width="400px",
            border_bottom_left_radius="10px",
            border_bottom_right_radius="10px"
        ),
        height="auto",
        margin_top="6em",
        margin_left="3em",
    )

def generate_video_rows(videos_info):
    # Generating rows of video components
    video_rows = []
    for i in range(0, len(videos_info), 3):
        videos_row = videos_info[i:i+3]
        video_components = [video_component(video["title"], video["description"], video["product_link"], video["youtube_link"]) for video in videos_row]
        video_row = rx.hstack(*video_components)
        video_rows.append(video_row)
    return video_rows

def index():
    # Creating the index page
    return rx.fragment(
        navbar(),  # Adding the navbar
        *generate_video_rows(videos_info),  # Adding video rows
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="pink",
    )
)

app.add_page(index)  # Adding the index page to the app