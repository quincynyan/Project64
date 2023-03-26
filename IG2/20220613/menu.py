import curses

classes = ["Bike", "Car", "SUV"]


def ride(stdscr):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr(
            "Use arrow keys to select and enter to choose\n", curses.A_UNDERLINE)
        for i in range(len(classes)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(classes[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1

    selected_vehicle = classes[option]
    stdscr.addstr("You have selected {0}".format(selected_vehicle))

    # Call your desired function here
    if selected_vehicle == "Bike":
        num_riders = 1
    elif selected_vehicle == "Car":
        num_riders = 4
    elif selected_vehicle == "SUV":
        num_riders = 7
    stdscr.addstr("\n{0} riders can ride the {1}".format(
        num_riders, selected_vehicle))

    stdscr.getch()


curses.wrapper(ride)
