# Imports
import sys, pygame
import game_params as G
pygame.init()


# Updates window after every fps
def update_window():
    # Add background Color
    pygame.draw.rect(G.WINDOW, (255,255,255), G.BACKGROUND)
    # Draw Pipes
    pygame.draw.rect(G.WINDOW, (0, 0, 0), G.PIPE_UP)
    pygame.draw.rect(G.WINDOW, (0, 0, 0), G.PIPE_DOWN)
    # Update the window
    pygame.display.update()



# Main function, which combines all the logic above
def main():
    # This is needed to set fps limiter
    clock = pygame.time.Clock()
    # Main loop of the game
    while True:
        # FPS limiter
        clock.tick(G.FPS)
        # We collect all the events between loops
        for event in pygame.event.get():
            # Handle closing of the window
            if event.type == pygame.QUIT:
                sys.exit()
                break
            # Check if player pressed Space
            if event.type == pygame.K_SPACE:
                pass

        # After checking all events update window
        update_window()


    # If the loop above has broken, then we just call main()
    #  again and restart the game
    # main()


# Makes sure this code can only be run, when this file is references
if __name__ == "__main__":
    main()