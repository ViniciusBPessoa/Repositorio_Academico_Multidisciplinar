import pygame
import math
import sys

# --- Constantes ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

GRAVITY = pygame.math.Vector2(0, 250)  # Pixels/s^2
BALL_RADIUS = 15
BALL_COLOR = RED
BALL_RESTITUTION = 0.7  # Coeficiente de restituição (elasticidade da colisão)
BALL_FRICTION = 0.15    # Coeficiente de atrito cinético
BALL_MASS = 1.0         # Massa da bola (simplificada para 1 nos cálculos de impulso)

HEXAGON_CENTER = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
HEXAGON_SIZE = 250  # Distância do centro ao vértice
HEXAGON_COLOR = BLUE
HEXAGON_LINE_THICKNESS = 3
HEXAGON_ANGULAR_SPEED = math.radians(25)  # Radianos por segundo

# --- Funções Auxiliares ---
def closest_point_on_segment(p_vec, a_vec, b_vec):
    """Encontra o ponto mais próximo ao ponto p_vec no segmento de reta [a_vec, b_vec]."""
    ap = p_vec - a_vec
    ab = b_vec - a_vec
    ab_len_sq = ab.length_squared()

    if ab_len_sq == 0:  # Segmento é um ponto
        return a_vec

    t = ap.dot(ab) / ab_len_sq
    if t < 0.0:
        return a_vec
    elif t > 1.0:
        return b_vec
    else:
        return a_vec + t * ab

def get_hexagon_vertices(center, size, angle_offset_rad):
    """Calcula os vértices de um hexágono regular."""
    vertices = []
    for i in range(6):
        angle = angle_offset_rad + (i * math.pi / 3.0)  # 2*pi/6 = pi/3
        x = center.x + size * math.cos(angle)
        y = center.y + size * math.sin(angle)
        vertices.append(pygame.math.Vector2(x, y))
    return vertices

# --- Jogo Principal ---
def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bola Quicando em Hexágono Giratório")
    clock = pygame.time.Clock()

    ball_pos = pygame.math.Vector2(HEXAGON_CENTER.x, HEXAGON_CENTER.y)
    ball_vel = pygame.math.Vector2(70, -50)  # Velocidade inicial

    hexagon_current_angle = 0.0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time em segundos
        if dt == 0: continue # Evita divisão por zero se o frame for muito rápido

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Atualizações ---
        # 1. Atualizar hexágono
        hexagon_current_angle += HEXAGON_ANGULAR_SPEED * dt
        hexagon_vertices_world = get_hexagon_vertices(HEXAGON_CENTER, HEXAGON_SIZE, hexagon_current_angle)

        # 2. Atualizar bola
        # Aplicar gravidade
        ball_vel += GRAVITY * dt
        
        # Posição tentativa da bola (antes da colisão)
        # ball_pos_tentative = ball_pos + ball_vel * dt # Usaremos ball_pos diretamente para detecção

        # Detecção e resposta de colisão
        for i in range(6):
            p1 = hexagon_vertices_world[i]
            p2 = hexagon_vertices_world[(i + 1) % 6]

            closest_pt_on_wall = closest_point_on_segment(ball_pos, p1, p2)
            
            # Vetor do ponto mais próximo na parede para o centro da bola
            vec_wall_to_ball = ball_pos - closest_pt_on_wall
            distance_to_wall = vec_wall_to_ball.length()

            if distance_to_wall < BALL_RADIUS:
                # Normal da colisão (aponta da parede para o centro da bola)
                if distance_to_wall < 1e-6: # Bola está (quase) exatamente na superfície
                    edge_vec = p2 - p1
                    # Normal "externa" para um polígono CCW
                    collision_normal = pygame.math.Vector2(edge_vec.y, -edge_vec.x)
                    if collision_normal.length_squared() > 0:
                        collision_normal.normalize_ip()
                    else: # Fallback improvável
                        collision_normal = pygame.math.Vector2(0, -1) 
                else:
                    collision_normal = vec_wall_to_ball.normalize()

                # Resolução de penetração (move a bola para fora da parede)
                penetration_depth = BALL_RADIUS - distance_to_wall
                ball_pos += collision_normal * penetration_depth
                
                # Calcular velocidade do ponto de colisão na parede
                # r_collision é o vetor do centro do hexágono ao ponto de colisão
                r_collision = closest_pt_on_wall - HEXAGON_CENTER
                v_wall_at_collision_point = pygame.math.Vector2(
                    -HEXAGON_ANGULAR_SPEED * r_collision.y,
                     HEXAGON_ANGULAR_SPEED * r_collision.x
                )

                # Velocidade relativa da bola em relação à parede
                v_relative = ball_vel - v_wall_at_collision_point

                # Componente da velocidade relativa ao longo da normal
                vel_along_normal = v_relative.dot(collision_normal)

                if vel_along_normal < 0:  # Bola está se movendo em direção à parede
                    # Impulso normal (restituição)
                    # j_n = -(1 + BALL_RESTITUTION) * vel_along_normal / (1/BALL_MASS) (se massa não for 1)
                    j_n_scalar = -(1 + BALL_RESTITUTION) * vel_along_normal
                    impulse_normal_vec = j_n_scalar * collision_normal
                    
                    ball_vel += impulse_normal_vec / BALL_MASS

                    # Impulso de atrito
                    # Recalcular velocidade relativa tangencial após impulso normal
                    v_relative_after_norm_impulse = (ball_vel - v_wall_at_collision_point)
                    tangent_vec = v_relative_after_norm_impulse - v_relative_after_norm_impulse.dot(collision_normal) * collision_normal
                    
                    if tangent_vec.length_squared() > 1e-6:
                        tangent_dir = tangent_vec.normalize()
                        
                        # Magnitude do impulso normal (escalar)
                        # j_n_scalar já calculado
                        
                        # Máximo impulso de atrito (modelo de Coulomb)
                        jt_max = BALL_FRICTION * abs(j_n_scalar)
                        
                        # Impulso necessário para parar o movimento tangencial (relativo à parede)
                        # (massa * velocidade tangencial)
                        jt_to_stop = tangent_vec.length() * BALL_MASS 
                        
                        jt_applied = min(jt_max, jt_to_stop)
                        impulse_friction_vec = -jt_applied * tangent_dir
                        
                        ball_vel += impulse_friction_vec / BALL_MASS
                
                # Processar apenas uma colisão por frame para simplificar
                # Em cenários mais complexos, múltiplas colisões podem precisar ser resolvidas iterativamente
                break 
        
        # Atualização final da posição da bola
        ball_pos += ball_vel * dt

        # --- Desenho ---
        screen.fill(BLACK)
        # Desenhar hexágono
        pygame.draw.polygon(screen, HEXAGON_COLOR, hexagon_vertices_world, HEXAGON_LINE_THICKNESS)
        # Desenhar bola
        pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos.x), int(ball_pos.y)), BALL_RADIUS)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game()
