import pygame

class Screen:
    WIDTH: int = 800
    HEIGHT: int = 600
    FPS: int = 60

class Simulation:
    def __init__(self, title: str, points: tuple[int, int]) -> None:
        pygame.init()
        pygame.display.set_caption(f"{title} Simulation")

        self.window: pygame.Surface = pygame.display.set_mode(
            (Screen.WIDTH, Screen.HEIGHT))
        
        self.points = points
        
        self.clock = pygame.time.Clock()
        self.is_running: bool = True
        self.frame = 0

    def run(self) -> None:
        while self.is_running:
            self.handle_events()
            self.render()
            self.clock.tick(Screen.FPS)
        self.shutdown()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def render(self) -> None:
        self.window.fill(pygame.Color("black"))

        if len(self.points) > 1:
            pygame.draw.lines(self.window,
                pygame.Color("white"), False, self.points, 2)

        for point in self.points:
            pygame.draw.circle(self.window,
                pygame.Color("gray"), point, 3)

        pygame.display.flip()

    def shutdown(self) -> None:
        pygame.quit()