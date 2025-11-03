""" 
Application to help analyze the accessibility of different colors.

Students you are free to look through the application, but you do not need to make
changes. For your final report, you will need to run the application,
and get results from your run. 

"""
from color_tools import *


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB values to hex format.

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)

    Returns:
        str: Hex color code in format #RRGGBB
    """
    return f"#{r:02x}{g:02x}{b:02x}"


def hex_to_rgb(hex_color: str) -> tuple:
    """
    Convert hex color to RGB values.

    Arguments:
        hex_color (str): Hex color code (with or without #)

    Returns:
        tuple: (r, g, b) values as integers
    """
    # Remove # if present
    hex_color = hex_color.lstrip('#')

    # Convert each pair of hex digits to decimal
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)


def create_color_swatch_link(r: int, g: int, b: int) -> str:
    """
    Create a color viewing link with terminal compatibility detection.

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)

    Returns:
        str: Either a terminal link or external URL for viewing the color
    """
    hex_color = rgb_to_hex(r, g, b).lstrip('#')

    # Try to detect if terminal supports links
    import os
    terminal_program = os.environ.get('TERM_PROGRAM', '')
    wt_session = os.environ.get('WT_SESSION', '')

    # External URL (works universally)
    external_url = f"https://www.color-hex.com/color/{hex_color}"

    # Check for terminals known to support hyperlinks
    if terminal_program in ['iTerm.app', 'vscode'] or wt_session:
        # Create simple terminal hyperlink to external site
        return f"\033]8;;{external_url}\033\\View Color\033]8;;\033\\"
    else:
        # Fallback to plain URL
        return external_url


def get_hex_input(color_description: str) -> tuple:
    """
    Get hex color from user with validation.

    Arguments:
        color_description (str): Description of the color being requested

    Returns:
        tuple: (r, g, b) values as integers
    """
    print(f"\nEnter {color_description} color:")

    while True:
        try:
            hex_input = input("Hex color (e.g., #FF8040 or FF8040): ").strip()
            r, g, b = hex_to_rgb(hex_input)

            # Validate RGB range
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return r, g, b
            else:
                print("Invalid hex color. Please try again.")
        except (ValueError, IndexError):
            print("Invalid hex format. Use format like #FF8040 or FF8040.")


def display_color_info(r: int, g: int, b: int, label: str = "Color") -> None:
    """
    Display comprehensive information about a color including visual swatch link.

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)
        label (str): Label to display for this color
    """
    hex_color = rgb_to_hex(r, g, b)
    brightness = calculate_brightness(r, g, b)
    luminance = calculate_luminance(r, g, b)
    color_link = create_color_swatch_link(r, g, b)

    # Create brightness description
    if brightness > 200:
        bright_desc = "Very Bright"
    elif brightness > 150:
        bright_desc = "Bright"
    elif brightness > 100:
        bright_desc = "Medium"
    elif brightness > 50:
        bright_desc = "Dark"
    else:
        bright_desc = "Very Dark"

    print(f"{label}: {hex_color} | RGB({r}, {g}, {b}) | {color_link}")
    print(f"  Brightness: {brightness}/255 ({bright_desc})")
    print(f"  Luminance: {luminance:.3f}")


def check_contrast() -> None:
    """
    Check contrast ratio between two colors for WCAG compliance.
    Displays detailed accessibility analysis and recommendations.
    """
    print("\n" + "="*50)
    print("        WCAG CONTRAST CHECKER")
    print("="*50)

    # Get foreground and background colors
    fg_r, fg_g, fg_b = get_hex_input("text")
    bg_r, bg_g, bg_b = get_hex_input("background")

    # Calculate contrast
    ratio = contrast_ratio(fg_r, fg_g, fg_b, bg_r, bg_g, bg_b)

    # Display results
    print("\n" + "="*50)
    print("        CONTRAST RESULTS")
    print("="*50)
    display_color_info(fg_r, fg_g, fg_b, "Text")
    display_color_info(bg_r, bg_g, bg_b, "Background")
    print(f"\nContrast Ratio: {ratio:.1f}:1")
    print()

    # Check WCAG compliance
    print("WCAG COMPLIANCE:")
    wcag_tests = [
        ("AA Normal Text (4.5:1)", WCAG_AA_NORMAL),
        ("AA Large Text (3:1)", WCAG_AA_LARGE),
        ("AAA Normal Text (7:1)", WCAG_AAA_NORMAL),
        ("AAA Large Text (4.5:1)", WCAG_AAA_LARGE)
    ]

    for test_name, test_level in wcag_tests:
        if passes_wcag_level(ratio, test_level):
            print(f"✓ {test_name} - PASS")
        else:
            print(f"✗ {test_name} - FAIL")

    # Provide recommendations
    print()
    if ratio < WCAG_AA_NORMAL_RATIO:
        print("RECOMMENDATION:")
        print(recommend_adjustment(ratio, WCAG_AA_NORMAL_RATIO))
    elif ratio >= WCAG_AAA_NORMAL_RATIO:
        print("OUTSTANDING: Exceeds all accessibility standards!")
    else:
        print("GOOD: Meets basic web accessibility requirements.")


def analyze_color() -> None:
    """
    Analyze properties and web compatibility of a single color.
    Provides comprehensive analysis using while loop functions.
    """
    print("\n" + "="*50)
    print("        COLOR ANALYZER")
    print("="*50)

    r, g, b = get_hex_input("the")

    print("\n" + "="*50)
    print("        ANALYSIS RESULTS")
    print("="*50)
    display_color_info(r, g, b)

    # Web-focused analysis using while loop functions
    gray_count = calculate_contrast_with_grays(r, g, b)
    best_gray = find_accessible_gray_background(r, g, b)
    best_gray_hex = rgb_to_hex(best_gray, best_gray, best_gray)
    best_gray_link = create_color_swatch_link(best_gray, best_gray, best_gray)

    print(f"\nWEB ACCESSIBILITY ANALYSIS:")
    print(f"Gray backgrounds meeting WCAG AA: {gray_count} out of 52")
    print(f"Darkest accessible gray: {best_gray_hex} | {best_gray_link}")

    # Web usage suggestions
    print(f"\nWEB DESIGN SUGGESTIONS:")
    brightness = calculate_brightness(r, g, b)
    if brightness > 180:
        print("- Good for page backgrounds")
        print("- Pair with dark text colors")
    elif brightness < 80:
        print("- Ideal for text and headings")
        print("- Use on light backgrounds")
    else:
        print("- Versatile mid-tone color")
        print("- Test contrast with intended backgrounds")


def simulate_colorblind_view() -> None:
    """
    Show how a color appears to users with different types of colorblindness.
    Demonstrates accessibility considerations for inclusive web design.
    """
    print("\n" + "="*50)
    print("        COLORBLIND SIMULATOR")
    print("="*50)

    r, g, b = get_hex_input("the")

    print("\n" + "="*50)
    print("        SIMULATION RESULTS")
    print("="*50)

    original_hex = rgb_to_hex(r, g, b)
    original_link = create_color_swatch_link(r, g, b)
    print(f"Original: {original_hex} | RGB({r}, {g}, {b}) | {original_link}")

    print(f"\nHow this appears to colorblind users:")

    # Test each condition
    conditions = [
        (PROTANOPIA, "Protanopia (Red-Green Type 1)"),
        (DEUTERANOPIA, "Deuteranopia (Red-Green Type 2)"),
        (TRITANOPIA, "Tritanopia (Blue-Yellow)")
    ]

    for condition, name in conditions:
        sim_r, sim_g, sim_b = simulate_colorblindness(r, g, b, condition)
        sim_hex = rgb_to_hex(sim_r, sim_g, sim_b)
        sim_link = create_color_swatch_link(sim_r, sim_g, sim_b)
        print(f"{name}: {sim_hex} | RGB({sim_r}, {sim_g}, {sim_b}) | {sim_link}")


def test_gray_compatibility() -> None:
    """
    Test how many gray backgrounds are compatible with a given text color.
    Demonstrates the while loop functions for finding accessible combinations.
    """
    print("\n" + "="*50)
    print("      GRAY COMPATIBILITY TESTER")
    print("="*50)

    r, g, b = get_hex_input("text")

    # Run analysis using while loop functions
    gray_count = calculate_contrast_with_grays(r, g, b)
    best_dark_gray = find_accessible_gray_background(r, g, b)
    brightness_steps = find_minimum_brightness_steps(r, g, b, 128)

    print("\n" + "="*50)
    print("      COMPATIBILITY RESULTS")
    print("="*50)
    display_color_info(r, g, b, "Text Color")

    best_gray_hex = rgb_to_hex(best_dark_gray, best_dark_gray, best_dark_gray)
    best_gray_link = create_color_swatch_link(
        best_dark_gray, best_dark_gray, best_dark_gray)

    print(f"\nGRAY BACKGROUND COMPATIBILITY:")
    print(f"Compatible grays: {gray_count} out of 52 tested")
    print(f"Darkest usable: {best_gray_hex} | {best_gray_link}")

    if brightness_steps == 0:
        print(f"Text brightness: Already above medium (128)")
    else:
        print(f"Steps to medium brightness: {brightness_steps}")

    # Web design recommendations
    print(f"\nWEB DESIGN RECOMMENDATIONS:")
    if gray_count > 35:
        print("- Highly versatile text color")
        print("- Works with wide range of backgrounds")
    elif gray_count > 20:
        print("- Good text color with decent flexibility")
        print("- Test specific gray combinations")
    elif gray_count > 10:
        print("- Limited gray compatibility")
        print("- Consider alternative text colors")
    else:
        print("- Poor gray compatibility")
        print("- Use with carefully chosen backgrounds only")


def display_menu() -> None:
    """
    Display the main menu options for the application.
    Shows available analysis tools for web accessibility testing.
    """
    print("\n" + "="*50)
    print("     WEB ACCESSIBILITY ANALYZER")
    print("="*50)
    print("1. Check WCAG contrast compliance")
    print("2. Analyze color properties")
    print("3. Test colorblind accessibility")
    print("4. Find compatible gray backgrounds")
    print("5. Exit")
    print("="*50)


def main() -> None:
    """
    Main application loop for the web accessibility analyzer.
    Provides a menu-driven interface for testing color accessibility compliance
    and analyzing color properties for inclusive web design.
    """
    print("WEB ACCESSIBILITY COLOR ANALYZER")
    print("Ensure your website colors meet accessibility standards!")
    print("Enter all colors in hex format (e.g., #FF8040)")
    print("Note: Color links work in modern terminals like Windows Terminal, iTerm2")

    while True:
        display_menu()

        try:
            choice = input("\nSelect option (1-5): ").strip()

            if choice == "1":
                check_contrast()
            elif choice == "2":
                analyze_color()
            elif choice == "3":
                simulate_colorblind_view()
            elif choice == "4":
                test_gray_compatibility()
            elif choice == "5":
                print("\nThanks for using the Web Accessibility Analyzer!")
                print("Build inclusive websites that work for everyone!")
                break
            else:
                print("Please enter 1, 2, 3, 4, or 5.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        # Continue prompt
        print("\n" + "-"*50)
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
