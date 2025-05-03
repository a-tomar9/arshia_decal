
import pygame
import math

# starting pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Habitable World Builder")

'''used for steady animation?? and frame rate??'''
clock = pygame.time.Clock() 

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
PINK = (100, 32, 89)

# Constants
AU = 1.496e11  # Astronomical Unit in meters
R_STAR_SUN = 6.96e8  # Radius of the Sun in meters
HABITABLE_MIN = 0.95  # Inner edge of habitable zone (AU)
HABITABLE_MAX = 1.37  # Outer edge of habitable zone (AU)

# Star type data (simplified)
STAR_TYPES = {
    "O": {"temp": 30000, "radius": 10 * R_STAR_SUN},
    "B": {"temp": 20000, "radius": 5 * R_STAR_SUN},
    "A": {"temp": 8500,  "radius": 2 * R_STAR_SUN},
    "F": {"temp": 6500,  "radius": 1.3 * R_STAR_SUN},
    "G": {"temp": 5778,  "radius": R_STAR_SUN},
    "K": {"temp": 4500,  "radius": 0.7 * R_STAR_SUN},
    "M": {"temp": 3200,  "radius": 0.2 * R_STAR_SUN}
}

# Star colors by type
STAR_COLORS = {
    "O": (100, 100, 255),
    "B": (170, 191, 255),
    "A": (202, 215, 255),
    "F": (248, 247, 255),
    "G": (255, 244, 100),
    "K": (255, 210, 161),
    "M": (255, 100, 100)
}

# Start: Sun
current_star_type = "G"

# Star and orbit positions
star_pos = (width // 2, height // 2)
star_radius = 30
planet_radius = 15
angle = 0  # orbit angle

# Planet data (starts at 200 pixels)
planet_data = {
    "distance": 200,
    "surface": "rocky"
}

# Converting pixel distance to AU
def pixel_to_au(pixel_distance):
    return 0.1 + (pixel_distance - 100) / 300 * 2.4  


# Estimate temperature 
def get_temperature(distance_au, star_type):
    d_meters = distance_au * AU
    temp_star = STAR_TYPES[star_type]["temp"]
    radius_star = STAR_TYPES[star_type]["radius"]
    temp_kelvin = temp_star * math.sqrt(radius_star / (2 * d_meters))
    return round(temp_kelvin - 273.15, 1)  # Convert K to °C

# Determine surface type and status
def get_surface_and_status(temp, distance_au):
    if HABITABLE_MIN <= distance_au <= HABITABLE_MAX and 0 <= temp <= 50:
        return "rocky", "Rocky with possible presence of water"
    elif temp < 0:
        return "icy", "Too cold - likely icy surface"
    else:
        return "gaseous", "Too hot - likely gaseous or scorched"

# Map number keys to star types
key_map = {
    pygame.K_1: "O",
    pygame.K_2: "B",
    pygame.K_3: "A",
    pygame.K_4: "F",
    pygame.K_5: "G",
    pygame.K_6: "K",
    pygame.K_7: "M"
}

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Draw the star 
    star_color = STAR_COLORS[current_star_type]
    pygame.draw.circle(screen, star_color, star_pos, star_radius)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in key_map:
                current_star_type = key_map[event.key]

    # Slider fucntions
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_pressed[0] and 540 < mouse_y < 560 and 100 < mouse_x < 400:
        planet_data["distance"] = mouse_x

    # Drawing slider bar and knob
    pygame.draw.rect(screen, GRAY, (100, 550, 300, 10))
    pygame.draw.circle(screen, WHITE, (planet_data["distance"], 555), 8)

    # Calculate planet position in orbit
    angle += 0.01
    planet_x = int(star_pos[0] + planet_data["distance"] * math.cos(angle))
    planet_y = int(star_pos[1] + planet_data["distance"] * math.sin(angle))
    pygame.draw.circle(screen, PINK, (planet_x, planet_y), planet_radius)

    # Calculate distance and temperature
    distance_au = pixel_to_au(planet_data["distance"])
    temperature = get_temperature(distance_au, current_star_type)
    planet_data["surface"], status = get_surface_and_status(temperature, distance_au)

    # The info on screen
    font = pygame.font.SysFont(None, 24)
    info_lines = [
        "Use slider to change distance!",
        "Use keys 1–7 to change star type (O to M)",
        f"Star Type: {current_star_type} ({STAR_TYPES[current_star_type]['temp']}K)",
        f"Distance from star: {distance_au:.2f} AU",
        f"Temperature: {temperature}°C",
        f"Surface: {planet_data['surface']}",
        f"Status: {status}"
    ]

    for i, line in enumerate(info_lines):
        color = GREEN if "presence of water" in line else RED if "Too" in line else WHITE
        text = font.render(line, True, color)
        screen.blit(text, (10, 10 + i * 25))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
