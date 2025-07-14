import pygame

class ButtonTheme:
    def __init__(self, source_image: str, corners_size: tuple[tuple[int]], step_size: int = 16, fill_color: tuple[int] = (0, 0, 0)):
        """
        Defines the theme for buttons:
        - source_image (str) is the path of the image
        - corner_size is a tuple of 4 tuples, each containing the x and y of every corner
            - corners_size[0] is the top-left corner
            - corners_size[1] is the top-right corner
            - corners_size[2] is the bottom-right corner
            - corners_size[3] is the bottom-left corner
        """
        self.source_image = source_image
        self.corners_size = corners_size
        self.step_size = step_size
        self.fill_color = fill_color
        if len(corners_size) != 4:
            raise ValueError("corners_size must be a tuple of four tuples, each containing two integers.")

        image = pygame.image.load(source_image)
        self.top_left_corner = image.subsurface((0, 0, corners_size[0][0], corners_size[0][1]))
        self.top_right_corner = image.subsurface((image.get_width() - step_size, 0, corners_size[1][0], corners_size[1][1]))
        self.bottom_right_corner = image.subsurface((image.get_width() - step_size, image.get_height() - step_size, corners_size[2][0], corners_size[2][1]))
        self.bottom_left_corner = image.subsurface((0, image.get_height() - step_size, corners_size[3][0], corners_size[3][1]))

        self.top_edge= image.subsurface((step_size, 0, 1, step_size))
        self.left_edge= image.subsurface((0, step_size, step_size, 1))
        self.bottom_edge= image.subsurface((step_size, step_size*2, 1, step_size))
        self.right_edge = image.subsurface((step_size*2, step_size, step_size, 1))


class BasicButton:
    def __init__(self, size: tuple[int, int], theme: ButtonTheme, size_caching= True):
        self.button_surface = None
        self.size = size
        self.theme = theme
        self.size_caching = size_caching
        self.sized_surfaces = dict()  # Cache for sized surfaces

    
    def set_size(self, size: tuple[int, int]):
        self.size = size
        
    def generate_button_surface(self):
        if self.size_caching and self.size in self.sized_surfaces:
            self.button_surface = self.sized_surfaces[self.size]
            return
        width, height = self.size
        button_surface = pygame.Surface((width, height), pygame.SRCALPHA)

        # We draw the inner rect
        inner_rect_size = (width - self.theme.corners_size[0][0] - self.theme.corners_size[1][0],
                           height - self.theme.corners_size[0][1] - self.theme.corners_size[3][1])
        inner_rect_surface = pygame.Surface(inner_rect_size, pygame.SRCALPHA)
        inner_rect_surface.fill(self.theme.fill_color)
        button_surface.blit(inner_rect_surface, (self.theme.corners_size[0][0], self.theme.corners_size[0][1]))

        # We draw the top left corenr
        button_surface.blit(self.theme.top_left_corner, (0, 0))

        # We draw the top right corner
        button_surface.blit(self.theme.top_right_corner, (width - self.theme.corners_size[1][0] , 0))

        # We draw the bottom right corner
        button_surface.blit(self.theme.bottom_right_corner, (inner_rect_size[0] + self.theme.corners_size[0][0], inner_rect_size[1] + self.theme.corners_size[0][1]))

        # We draw the bottom left corner
        button_surface.blit(self.theme.bottom_left_corner, (0, inner_rect_size[1] + self.theme.corners_size[0][1]))

        # We draw the top edge (OLD METHOD)
        #for i in range(inner_rect_size[0]):
        #    button_surface.blit(self.theme.top_edge, (self.theme.corners_size[0][0]+ i,0))

        # We draw the right edge (OLD METHOD)
        #for i in range(inner_rect_size[1]):
        #    button_surface.blit(self.theme.right_edge, (inner_rect_size[0] + self.theme.corners_size[0][0], self.theme.corners_size[0][1] + i))

        # We draw the bottom edge (OLD METHOD)
        #for i in range(inner_rect_size[0]):
        #    button_surface.blit(self.theme.bottom_edge, (self.theme.corners_size[0][0]+ i, inner_rect_size[1] + self.theme.corners_size[0][1]))

        # We draw the left edge (OLD METHOD)
        #for i in range(inner_rect_size[1]):
        #    button_surface.blit(self.theme.left_edge, (0, self.theme.corners_size[0][1] + i))

        # We draw the top edge scaling it appropriately
        top_edge_scaled = pygame.transform.scale(self.theme.top_edge, (inner_rect_size[0], self.theme.step_size))
        button_surface.blit(top_edge_scaled, (self.theme.corners_size[0][0], 0))


        # We draw the right edge scaling it appropriately
        right_edge_scaled = pygame.transform.scale(self.theme.right_edge, (self.theme.step_size, inner_rect_size[1]))
        button_surface.blit(right_edge_scaled, (inner_rect_size[0] + self.theme.corners_size[0][0], self.theme.corners_size[0][1]))


        # We draw the bottom edge scaling it appropriately
        bottom_edge_scaled = pygame.transform.scale(self.theme.bottom_edge, (inner_rect_size[0], self.theme.step_size))
        button_surface.blit(bottom_edge_scaled, (self.theme.corners_size[0][0], inner_rect_size[1] +self.theme.corners_size[0][1]))

        # We draw the left edge scaling it appropriately
        left_edge_scaled = pygame.transform.scale(self.theme.left_edge, (self.theme.step_size, inner_rect_size[1]))
        button_surface.blit(left_edge_scaled, (0, self.theme.corners_size[0][1]))

        self.button_surface = button_surface

        if self.size_caching:
            self.sized_surfaces[self.size] = button_surface

    def draw(self, surface, position: tuple[int, int]):
        if self.button_surface is None:
            return
        
        surface.blit(self.button_surface, position)
