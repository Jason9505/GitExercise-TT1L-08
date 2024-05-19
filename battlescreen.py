class BattleScreen:
    def __init__(self, game):
        self.game = game
        self.running = True

    def run(self):
        while self.running:
            self.game.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.running = False

    def update(self):
        pass  # Update battle screen elements

    def draw(self):
        self.game.screen.fill((50, 50, 50))  # Fill with a different color for battle screen
        pygame.display.flip()
