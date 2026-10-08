import curses

def display_curses(stdscr, students, courses):
    curses.curs_set(0)
    stdscr.clear()

    row = 1
    stdscr.addstr(row, 2, "=== KẾT QUẢ ĐIỂM VÀ GPA SINH VIÊN (SẮP XẾP GIẢM DẦN) ===", curses.A_BOLD)
    row += 2

    header = f"{'ID':<10} | {'Tên':<20} | {'GPA':<6}"
    for c in courses:
        header += f" | {c.id:<8}"
    stdscr.addstr(row, 2, header, curses.A_UNDERLINE)
    row += 1

    for s in students:
        line = f"{s.id:<10} | {s.name:<20} | {s.gpa:<6.2f}"
        for c in courses:
            score = s.marks.get(c.id, "N/A")
            score_str = f"{score:.1f}" if isinstance(score, (int, float)) else str(score)
            line += f" | {score_str:<8}"
        stdscr.addstr(row, 2, line)
        row += 1

    row += 2
    stdscr.addstr(row, 2, "Nhấn phím bất kỳ để thoát...", curses.A_DIM)
    stdscr.refresh()
    stdscr.getch()