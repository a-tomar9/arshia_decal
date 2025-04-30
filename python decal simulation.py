import pygame
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Habitable World Builder")
clock = pygame.time.Clock() #used to control frame rate

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (100, 32, 89)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)

# Constants used
SIGMA = 5.67e-8  # Stefan-Boltzmann constant
T_STAR = 5778  # Sun temperature in Kelvin
R_STAR = 6.96e8  # Sun radius in meters
AU = 1.496e11  # Astronomical Unit in meters
HABITABLE_MIN = 0.95  # AU
HABITABLE_MAX = 1.37  # AU

# Star and planet settings
star_pos = (width // 2, height // 2)
star_radius = 30
planet_radius = 15
angle = 0

# Planet characteristics
planet_data = {
    "distance": 200,  # in pixels, wil be converted to au
    "surface": "rocky"
}

# Convert pixel distance to AU w/ linear approximation
def pixel_to_au(pixel_dist):
    return 0.5 + (pixel_dist - 100) / 300 * 2  #  0.5 AU to 2.5 AU

def get_temperature(distance_au):
    d_m = distance_au * AU
    temp = T_STAR * math.sqrt(R_STAR / (2 * d_m))
    return round(temp - 273.15, 1)  # conversion from Kelvin to Celsius

def get_surface_and_status(temp, distance_au):
    if HABITABLE_MIN <= distance_au <= HABITABLE_MAX and 0 <= temp <= 50:
        return "rocky", "Rocky with possible presence of water"
    elif temp < 0:
        return "icy", "Too cold - likely icy surface"
    else:
        return "gaseous", "Too hot - likely gaseous or scorched"

# Main game characteristics 
running = True
while running:
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, star_pos, star_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Slider interaction
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_pressed[0] and 540 < mouse_y < 560 and 100 < mouse_x < 400:
        planet_data["distance"] = mouse_x  # slider range

    # Draw slider bar and knob
    pygame.draw.rect(screen, GRAY, (100, 550, 300, 10))  
    pygame.draw.circle(screen, WHITE, (planet_data["distance"], 555), 8)  


    # Calculate distance in AU and temperature
    distance_au = pixel_to_au(planet_data["distance"])
    temperature = get_temperature(distance_au)

    # Update surface type and status
    planet_data["surface"], status = get_surface_and_status(temperature, distance_au)

    # Orbit & planet
    angle += 0.01
    planet_x = int(star_pos[0] + planet_data["distance"] * math.cos(angle))
    planet_y = int(star_pos[1] + planet_data["distance"] * math.sin(angle))
    pygame.draw.circle(screen, PINK, (planet_x, planet_y), planet_radius)

    # Render characteristics
    font = pygame.font.SysFont(None, 24)
    lines = [
        f"Use slider to change distance!",
        f"Distance from star: {distance_au:.2f} AU",
        f"Temperature: {temperature}°C",
        f"Surface: {planet_data['surface']}",
        f"Status: {status}"
    ]
    for i, line in enumerate(lines):
        color = GREEN if "presence of water" in line else RED if "Too" in line else WHITE
        text = font.render(line, True, color)
        screen.blit(text, (10, 10 + i * 25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
