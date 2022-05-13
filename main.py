from pyray import *
from random import *


def init():
    set_trace_log_level(TraceLogLevel.LOG_NONE)
    init_window(500, 500, "pi_calculator_visualizer")
    font = load_font_ex("resources/font.ttf", 30, ffi.NULL, 1487)
    set_texture_filter(font.texture, TextureFilter.TEXTURE_FILTER_BILINEAR)
    return font


def main():
    print("\nThis program generates an approximation of π using only random numbers from 0 - 1.")
    font = init()

    scale_factor = 300

    points_circle = 0
    points_square = 0
    points = []
    pi = 0

    start_timer = 0
    amount_increase_timer = 0
    point_amount = 0

    coordinate_origin = Vector2(50, get_screen_height() - 50)

    while not window_should_close():
        dtime = get_frame_time()
        start_timer += dtime
        amount_increase_timer += dtime

        if amount_increase_timer >= 1 and point_amount < 50:
            point_amount += 10
            amount_increase_timer = 0

        if start_timer > 1.5:
            for i in range(1, point_amount):
                x, y = random(), random()
                distance = x ** 2 + y ** 2

                if distance <= 1:
                    points_circle += 1

                points_square += 1
                pi = 4 * points_circle / points_square
                points.append(Vector2(x, y))

        begin_drawing()

        clear_background(WHITE)

        for i in points:
            scaled_point = Vector2(
                i.x * scale_factor + coordinate_origin.x, i.y * scale_factor * -1 + coordinate_origin.y)
            if check_collision_point_circle(i, Vector2(0, 0), 1):
                draw_circle_sector(scaled_point, 2, 0, 360, 10, BLUE)
            else:
                draw_circle_sector(scaled_point, 2, 0, 360, 10, RED)

        draw_text_ex(font, "π = " + str(pi), Vector2(10, 10), 30, 0, BLACK)
        draw_text_ex(font, "points = " + str(len(points)), Vector2(10, 50), 30, 0, BLACK)

        draw_line_ex(Vector2(0, coordinate_origin.y), Vector2(get_screen_width(), coordinate_origin.y), 4, BLACK)
        draw_line_ex(Vector2(coordinate_origin.x, 100), Vector2(coordinate_origin.x, get_screen_height()), 4, BLACK)
        draw_line_ex(Vector2(coordinate_origin.x - 10, 110), Vector2(coordinate_origin.x, 100), 4, BLACK)
        draw_line_ex(Vector2(coordinate_origin.x + 10, 110), Vector2(coordinate_origin.x, 100), 4, BLACK)
        draw_line_ex(Vector2(get_screen_width() - 10, coordinate_origin.y - 10), Vector2(get_screen_width(), coordinate_origin.y), 4, BLACK)
        draw_line_ex(Vector2(get_screen_width() - 10, coordinate_origin.y + 10), Vector2(get_screen_width(), coordinate_origin.y), 4, BLACK)

        draw_line_ex(Vector2(coordinate_origin.x, coordinate_origin.y - 1 * scale_factor), Vector2(coordinate_origin.x + 1 * scale_factor, coordinate_origin.y - 1 * scale_factor), 4, RED)
        draw_line_ex(Vector2(coordinate_origin.x + 1 * scale_factor, coordinate_origin.y - 1 * scale_factor), Vector2(coordinate_origin.x + 1 * scale_factor, coordinate_origin.y), 4, RED)
        draw_ring(coordinate_origin, 1 * scale_factor - 1, 1 * scale_factor + 1, 0, 360, 100, BLUE)

        draw_text_ex(font, "0", Vector2(coordinate_origin.x - 15, coordinate_origin.y), 20, 0, BLACK)
        draw_text_ex(font, "1", Vector2(coordinate_origin.x - 15, coordinate_origin.y - 1 * 300), 20, 0, BLACK)
        draw_text_ex(font, "1", Vector2(coordinate_origin.x - 15 + 1 * 300, coordinate_origin.y), 20, 0, BLACK)

        end_drawing()

    close_window()
    print("\nYour generated π ≈ " + str(pi))


if __name__ == "__main__":
    main()
