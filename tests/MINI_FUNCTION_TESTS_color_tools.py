# Constants to avoid magic numbers
GAMMA_THRESHOLD = 0.03928
GAMMA_DIVISOR = 12.92
GAMMA_OFFSET = 0.055
GAMMA_MULTIPLIER = 1.055
GAMMA_EXPONENT = 2.4

# WCAG luminance coefficients
RED_LUMINANCE_COEFFICIENT = 0.2126
GREEN_LUMINANCE_COEFFICIENT = 0.7152
BLUE_LUMINANCE_COEFFICIENT = 0.0722

# Brightness calculation coefficients
RED_BRIGHTNESS_COEFFICIENT = 0.299
GREEN_BRIGHTNESS_COEFFICIENT = 0.587
BLUE_BRIGHTNESS_COEFFICIENT = 0.114

# WCAG contrast standards
WCAG_AA_NORMAL_RATIO = 4.5
WCAG_AA_LARGE_RATIO = 3.0
WCAG_AAA_NORMAL_RATIO = 7.0
WCAG_AAA_LARGE_RATIO = 4.5

# Color value limits
RGB_MIN = 0
RGB_MAX = 255
LUMINANCE_OFFSET = 0.05

# Loop function constants
GRAY_STEP_SIZE = 5
RGB_INCREMENT = 1
MAX_RGB_VALUE = 255

# Colorblindness condition strings
PROTANOPIA = "protanopia"
DEUTERANOPIA = "deuteranopia"
TRITANOPIA = "tritanopia"

# WCAG level strings
WCAG_AA_NORMAL = "AA_NORMAL"
WCAG_AA_LARGE = "AA_LARGE"
WCAG_AAA_NORMAL = "AAA_NORMAL"
WCAG_AAA_LARGE = "AAA_LARGE"


def calculate_luminance(r: int, g: int, b: int) -> float:
    """
    Calculate relative luminance for WCAG contrast calculations.

    Examples:
        >>> round(calculate_luminance(255, 255, 255), 3)
        1.0
        >>> round(calculate_luminance(0, 0, 0), 3)
        0.0
        >>> round(calculate_luminance(128, 128, 128), 3)
        0.216

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)

    Returns:
        float: Relative luminance value (0.0-1.0)
    """
    # Convert to 0-1 range
    r_norm = r / RGB_MAX
    g_norm = g / RGB_MAX
    b_norm = b / RGB_MAX

    # Apply gamma correction (WCAG formula)
    def gamma_correct(channel):
        if channel <= GAMMA_THRESHOLD:
            return channel / GAMMA_DIVISOR
        else:
            return ((channel + GAMMA_OFFSET) / GAMMA_MULTIPLIER) ** GAMMA_EXPONENT

    r_linear = gamma_correct(r_norm)
    g_linear = gamma_correct(g_norm)
    b_linear = gamma_correct(b_norm)

    # Calculate luminance using WCAG coefficients
    luminance = (
        RED_LUMINANCE_COEFFICIENT * r_linear
        + GREEN_LUMINANCE_COEFFICIENT * g_linear
        + BLUE_LUMINANCE_COEFFICIENT * b_linear
    )
    return luminance


def simulate_colorblindness(r: int, g: int, b: int, condition: str) -> tuple:
    """
    Simulate how colors appear with different types of colorblindness.
    Uses simplified transformations for educational purposes.

    Examples:
        >>> simulate_colorblindness(255, 128, 64, "protanopia")
        (191, 191, 64)
        >>> simulate_colorblindness(255, 128, 64, "deuteranopia")
        (223, 223, 64)
        >>> simulate_colorblindness(255, 128, 64, "tritanopia")
        (255, 128, 96)

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)
        condition (str): "protanopia", "deuteranopia", or "tritanopia"

    Returns:
        tuple: (r, g, b) values as perceived by colorblind person
    """
    if condition == PROTANOPIA:
        # Red-green colorblind (missing L-cones): blend red and green
        new_rg = int((r + g) / 2)
        return (new_rg, new_rg, b)
    elif condition == DEUTERANOPIA:
        # Red-green colorblind (missing M-cones): blend red and green differently
        new_rg = int((r * 0.75 + g * 0.25))
        return (new_rg, new_rg, b)
    elif condition == TRITANOPIA:
        # Blue-yellow colorblind (missing S-cones): blend blue with others
        new_b = int((g + b) / 2)
        return (r, g, new_b)
    else:
        # Unknown condition, return original
        return (r, g, b)

# --- 1 ---#


def calculate_brightness(r: int, g: int, b: int) -> int:
    """
    Calculate perceived brightness of a color.

    Implementation:
    Use the standard luminance formula but return the result as an integer from 0-255.
    The formula weights the RGB components differently because human eyes are more
    sensitive to green than red, and more sensitive to red than blue. Multiply each
    RGB component by its coefficient, sum them, and convert to integer. Use the
    brightness coefficient constants defined at the top of the file.

    Examples:
        >>> calculate_brightness(255, 255, 255)
        255
        >>> calculate_brightness(0, 0, 0)
        0
        >>> calculate_brightness(255, 0, 0)
        76

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)

    Returns:
        int: Perceived brightness (0-255)
    """
    brightness = (RED_BRIGHTNESS_COEFFICIENT * r) + \
        (GREEN_BRIGHTNESS_COEFFICIENT * g) + (BLUE_BRIGHTNESS_COEFFICIENT * b)
    return int(round(brightness))


print("White (255,255,255):", calculate_brightness(
    255, 255, 255))  # should be 255
print("Black (0,0,0):", calculate_brightness(
    0, 0, 0))              # should be  0
print("Red (255,0,0):", calculate_brightness(
    255, 0, 0))            # should be  ~76
print("Green (0,255,0):", calculate_brightness(
    0, 255, 0))          # should be  ~150
print("Blue (0,0,255):", calculate_brightness(
    0, 0, 255))           # should be  ~29
print("Gray (128,128,128):", calculate_brightness(
    128, 128, 128))   # should be  ~128

# --- 2 ---#


def contrast_ratio(fg_r: int, fg_g: int, fg_b: int,
                   bg_r: int, bg_g: int, bg_b: int) -> float:
    """
    Calculate contrast ratio between foreground and background colors.

    Implementation:
    The contrast ratio is calculated using WCAG standards. First, calculate the relative
    luminance for both colors using the calculate_luminance() function. Then apply the
    WCAG contrast formula: (L1 + 0.05) / (L2 + 0.05), where L1 is the luminance of
    the lighter color and L2 is the luminance of the darker color. You'll need to
    determine which color is lighter and ensure it's used as the numerator.

    Examples:
        >>> round(contrast_ratio(0, 0, 0, 255, 255, 255), 1)
        21.0
        >>> round(contrast_ratio(255, 255, 255, 255, 255, 255), 1)
        1.0
        >>> round(contrast_ratio(128, 128, 128, 255, 255, 255), 1)
        3.9

    In the examples, the round is used to make the returned result easier to compare.
    As a student you are free to use that for your example.

    Arguments:
        fg_r (int): Foreground red (0-255)
        fg_g (int): Foreground green (0-255)
        fg_b (int): Foreground blue (0-255)
        bg_r (int): Background red (0-255)
        bg_g (int): Background green (0-255)
        bg_b (int): Background blue (0-255)

    Returns:
        float: Contrast ratio (1.0-21.0)
    """
    fg_Lumin = calculate_luminance(fg_r, fg_g, fg_b)
    bg_Lumin = calculate_luminance(bg_r, bg_g, bg_b)

    lighter = max(fg_Lumin, bg_Lumin)
    darker = min(fg_Lumin, bg_Lumin)

    ratio = (lighter + LUMINANCE_OFFSET) / (darker + LUMINANCE_OFFSET)

    return ratio


print(round(contrast_ratio(0, 0, 0, 255, 255, 255), 1))       # Should be 21.0
print(round(contrast_ratio(255, 255, 255, 255, 255, 255), 1))  # Should be 1.0
print(round(contrast_ratio(128, 128, 128, 255, 255, 255), 1))  # Should be 3.9
print(round(contrast_ratio(255, 255, 255, 136, 0, 0), 1))  # Should be 10.3


# --- 3 ---#

def passes_wcag_level(ratio: float, level: str) -> bool:
    """
    Check if contrast ratio meets WCAG standards.

    Implementation:
    Use conditional statements to check the input level string against the defined
    WCAG level constants. For each level, compare the ratio against the appropriate
    threshold constant. Return True if the ratio meets or exceeds the threshold,
    False otherwise. Handle unknown level strings by returning False.

    Examples:
        >>> passes_wcag_level(4.5, "AA_NORMAL")
        True
        >>> passes_wcag_level(4.0, "AA_NORMAL")
        False
        >>> passes_wcag_level(7.0, "AAA_NORMAL")
        True

    Arguments:
        ratio (float): Contrast ratio to check
        level (str): WCAG level ("AA_NORMAL", "AA_LARGE", "AAA_NORMAL", "AAA_LARGE")

    Returns:
        bool: True if ratio meets the specified level
    """
    if level == WCAG_AA_NORMAL:
        if ratio >= WCAG_AA_NORMAL_RATIO:
            return True
        else:
            return False

    elif level == WCAG_AA_LARGE:
        if ratio >= WCAG_AA_LARGE_RATIO:
            return True
        else:
            return False

    elif level == WCAG_AAA_NORMAL:
        if ratio >= WCAG_AAA_NORMAL_RATIO:
            return True
        else:
            return False

    elif level == WCAG_AAA_LARGE:
        if ratio >= WCAG_AAA_LARGE_RATIO:
            return True
        else:
            return False

    else:
        # Handling unknowns and everything else.
        return False


print(passes_wcag_level(4.5, WCAG_AA_NORMAL))  # Should be True
print(passes_wcag_level(3.0, WCAG_AA_LARGE))   # Should be True
print(passes_wcag_level(7.0, WCAG_AAA_NORMAL))  # Should be True
print(passes_wcag_level(6.0, WCAG_AAA_NORMAL))  # Should be False
print(passes_wcag_level(5.0, "TOMATOES"))        # Should be False


# Pseudocode: What I think this should look like
"""
    IF level == "AA_NORMAL":
        IF ratio >= 4.5: #Two-layer If statement check for two important things
        RETURN True
    ELSE:
        return False
...
...
And so on.

Basically:
SET threshold to 0

IF level == "AA_NORMAL": threshold = 4.5
ELSE IF level == "AA_LARGE": threshold = 3.0
ELSE IF level == "AAA_NORMAL": threshold = 7.0
ELSE IF level == "AAA_LARGE": threshold = 4.5
ELSE: RETURN False

RETURN ratio >= threshold
"""


# --- 4 ---#

def recommend_adjustment(current_ratio: float, target_ratio: float) -> str:
    """
    Suggest how to improve contrast ratio.

    Implementation:
    Calculate the gap (target_ratio - current_ratio). Use conditional
    statements to categorize the gap: if current >= target, success; if gap <= 1.5,
    minor improvement needed; if gap > 1.5, major improvement needed. The threshold
    of 1.5 represents the boundary between minor and major adjustments. Return
    specific recommendation strings for each category.

    Examples:
        >>> recommend_adjustment(3.0, 4.5)
        'Increase contrast by making colors more different'
        >>> recommend_adjustment(5.0, 4.5)
        'Contrast ratio already meets target'
        >>> recommend_adjustment(2.0, 7.0)
        'Significant contrast improvement needed - consider much darker or lighter colors'

    Arguments:
        current_ratio (float): Current contrast ratio
        target_ratio (float): Desired contrast ratio

    Returns:
        str: Recommendation message
    """
    improvement_threshold = 1.5
    gap = target_ratio - current_ratio

    if current_ratio >= target_ratio:
        return "Contrast ratio already meets target"

    elif gap <= improvement_threshold:
        return "Increase contrast by making colors more different"

    else:
        return "Significant contrast improvement needed - consider much darker or lighter colors"


print(recommend_adjustment(5.0, 4.5))
# Should be "Contrast ratio already meets target"

print(recommend_adjustment(3.0, 4.5))
# Should be minor improvement: "Increase contrast..."

print(recommend_adjustment(3.1, 4.5))
# Should be minor improvement: "Increase contrast..."

print(recommend_adjustment(2.9, 4.5))
# Should be minor improvement: "Significant contrast..."


# Thoughts:
"""
So the Ratios above are:
AA Normal = 4.5
AA Large = 3.0
AAA Normal = 7.5
AAA Large = 4.5

It’s not calculating. It’s checking the output to the target values, and returning easy-to-read feedback.

EQ: Function asks
“Does this already meet the goal ratio?” Y/N
If N, “Is it close?” Y = give minor feedback
If N, “Or is it way off?”. Give major feedback

EQ: How to make the function to DECIDE what is Good ratio, what needs a little adjustment, or major adjustment (based on sample outputs)?

* Implementation gives HINTS:
Gap = (target_ratio - current_ratio)
if current >= target, success;
if gap <= 1.5,
    minor improvement needed;
    if gap > 1.5, major improvement needed.
    1.5 key float number for MINOR and MAJOR determination.

    Return = string: word statement

"""

# Pseudocode testing
"""
    SET CONSTANT: improvement_threshold = 1.5
    CALCULATE THE GAP = target_ratio - current_ratio (given from imp. notes)

    IF current_ratio >= target_ratio:
        RETURN "Contrast ratio already meets target"

    ELSE IF gap <= improvement_threshold:
        RETURN "Increase contrast by making colors more different"

    ELSE:
        RETURN "Significant contrast improvement needed - consider much darker or lighter colors"

"""


# --- 5 ---#

def find_minimum_brightness_steps(r: int, g: int, b: int, min_brightness: int) -> int:
    """
    Count steps needed to reach minimum brightness by incrementing RGB values equally.
    Uses while loop to increase brightness until threshold is met.

    Implementation:
    First check if the color is already bright enough using calculate_brightness().
    If so, return 0. Otherwise, use a while loop to increment all three RGB values
    by RGB_INCREMENT each iteration (but don't exceed 255). Count each iteration as a step.
    Continue until calculate_brightness() returns a value >= min_brightness. Include
    a safety check to prevent infinite loops when the target can't be reached.

    Examples:
        >>> find_minimum_brightness_steps(0, 0, 0, 50)
        50
        >>> find_minimum_brightness_steps(100, 100, 100, 50)
        0
        >>> find_minimum_brightness_steps(10, 20, 30, 100)
        82

    Arguments:
        r, g, b (int): Current RGB values
        min_brightness (int): Minimum brightness target (0-255)

    Returns:
        int: Number of steps needed (0 if already bright enough)
    """
    if min_brightness < 0:
        min_brightness = 0
    elif min_brightness > 255:
        min_brightness = 255

    brightness = calculate_brightness(r, g, b)

    if brightness >= min_brightness:
        return 0

    steps = 0

    while brightness < min_brightness:
        r = min(r + RGB_INCREMENT, MAX_RGB_VALUE)
        g = min(g + RGB_INCREMENT, MAX_RGB_VALUE)
        b = min(b + RGB_INCREMENT, MAX_RGB_VALUE)

        # Recalcs after increment
        brightness = calculate_brightness(r, g, b)

        steps += 1

        # Stops infinite Loop w/ BREAK
        if r == MAX_RGB_VALUE and g == MAX_RGB_VALUE and b == MAX_RGB_VALUE:
            break

    return steps


# Testing
# EX 1: Completely dark, target 50
print("ex 1:", find_minimum_brightness_steps(0, 0, 0, 50))  # Expected ~ 50

# EX 2: Already bright enough
print("ex 2:", find_minimum_brightness_steps(100, 100, 100, 50))  # Should be 0

# EX 3: Moderate color aiming for high brightness
print("ex 3:", find_minimum_brightness_steps(
    10, 20, 30, 100))  # Should be ~ 82

# EX 4: Extremely high target
print("ex 4:", find_minimum_brightness_steps(
    240, 240, 240, 300))  # should be 15

# EX 5: Negative target
print("ex 5:", find_minimum_brightness_steps(50, 50, 50, -20))  # Should be 0


# --- 6 ---#

def calculate_contrast_with_grays(color_r: int, color_g: int, color_b: int) -> int:
    """
    Find how many gray levels (0, 5, 10, 15... 255) meet AA contrast standards.
    Uses while loop to test gray values from 0 to 255 in steps of 5.

    Implementation:
    Initialize a counter and a gray value variable. Use a while loop to iterate
    through gray levels from 0 to 255 in steps of 5. For each gray level, create
    a gray color by using the same value for R, G, and B components. Calculate the
    contrast ratio between the input color and this gray using contrast_ratio().
    If the ratio meets AA standards (4.5:1), increment your counter. Return the
    total count of passing gray levels.

    Examples:
        >>> calculate_contrast_with_grays(0, 0, 0)
        28
        >>> calculate_contrast_with_grays(255, 255, 255)
        24
        >>> calculate_contrast_with_grays(128, 128, 128)
        5
        >>> calculate_contrast_with_grays(100, 50, 150)
        14
        >>> calculate_contrast_with_grays(0, 255, 0)
        20
        >>> calculate_contrast_with_grays(255, 0, 0)
        5

    Arguments:
        color_r, color_g, color_b (int): RGB values of the test color

    Returns:
        int: Count of gray levels that provide AA contrast (4.5:1 or better)
    """
    passing_count = 0
    gray = 0

    while gray <= 255:
        contrast = contrast_ratio(color_r, color_g, color_b, gray, gray, gray)

        if contrast >= WCAG_AA_NORMAL_RATIO:
            passing_count += 1  # iterative steps

        gray += GRAY_STEP_SIZE  # iterate thru steps defined above

    return passing_count


print(calculate_contrast_with_grays(
    0, 0, 0))       # Expected ~ 28
print(calculate_contrast_with_grays(
    255, 255, 255))  # Expected ~ 24
print(calculate_contrast_with_grays(
    128, 128, 128))  # Expected ~ 5
print(calculate_contrast_with_grays(
    100, 50, 150))  # Expected: 14
print(calculate_contrast_with_grays(
    0, 255, 0))         # Expected: 20
print(calculate_contrast_with_grays(
    255, 0, 0))           # Expected: 5


# Thinking Space
"""
From Implement Notes: I follow it as saying
-1 Start w/ a counter (passing_count = 0)

-2 Start the first gray level at 0

-3 While gray ≤ 255:

    -a Make a gray color = (gray, gray, gray). CONST defined so no magic number

    -b Compute contrast = contrast_ratio(color_r, color_g, color_b, gray, gray, gray)

    -c If contrast ≥ 4.5 → add 1 to the count

    -d Increase gray by 5

-8 Return the count at the end.

Note: The implement notes are meticulously written and really help me follow them. It will be a good practice to learn how to write equally meticulous notes like this too for my functions.
"""

# Pseudocode (getting better with this!)
"""
CONSTANT passing_count = 0
CONSTANT gray = 0

WHILE gray <= 255:
    contrast = contrast_ratio(color_r, color_g, color_b, gray, gray, gray)

    if contrast >= WCAG_AA_NORMAL_RATIO:
        passing_count = passing_count + 1
    gray = gray + GRAY_STEP_SIZE

RETURN passing_count

"""

# --- 7 ---#


def find_accessible_gray_background(text_r: int, text_g: int, text_b: int) -> int:
    """
    Find the darkest gray background that still provides AA contrast with given text.
    Uses while loop to test gray values starting from white (255).

    Implementation:
    Start with the lightest gray (255) and work toward darker values (0). Use a
    while loop to decrement the gray value. For each gray level, calculate the
    contrast ratio with the text color using contrast_ratio(). Keep track of the
    darkest gray that still provides AA contrast (4.5:1). The key insight is that
    you want the darkest valid option, so continue testing even after finding
    valid grays. Return the darkest gray that meets the standard.

    Examples:
        >>> find_accessible_gray_background(0, 0, 0)
        117 
        >>> find_accessible_gray_background(255, 255, 255)
        0
        >>> find_accessible_gray_background(100, 100, 100)
        225
        >>> find_accessible_gray_background(128, 128, 128)
        200 
        >>> find_accessible_gray_background(255, 0, 0)
        155
        >>> find_accessible_gray_background(0, 255, 0)
        160

    Arguments:
        text_r, text_g, text_b (int): RGB values of the text color

    Returns:
        int: Darkest gray value (0-255) that provides AA contrast, or 255 if none work
    """

    gray = 255  # It starts white
    darkest_valid_gray = 255

    while gray >= 0:
        contrast = contrast_ratio(text_r, text_g, text_b, gray, gray, gray)
        if contrast >= WCAG_AA_NORMAL_RATIO:
            darkest_valid_gray = gray
        gray -= GRAY_STEP_SIZE  # goes darker

    gray = darkest_valid_gray  # start from last good value
    while gray >= 0:
        contrast = contrast_ratio(text_r, text_g, text_b, gray, gray, gray)
        if contrast < WCAG_AA_NORMAL_RATIO:
            break
        darkest_valid_gray = gray
        gray -= 1

    if darkest_valid_gray == 255:  # My fallback if checks fail
        return 255
    return int(darkest_valid_gray)


# EX 1
print("Test 1:", find_accessible_gray_background(0, 0, 0))  # Should be 117

# EX 2
print("Test 2:", find_accessible_gray_background(
    255, 255, 255))  # Should be 0

# EX 3
print("Test 3:", find_accessible_gray_background(
    100, 100, 100))  # Should be 225

# EX 4
print("Test 4:", find_accessible_gray_background(
    255, 0, 0))  # Should be 155

# EX 5
print("Test 5:", find_accessible_gray_background(
    0, 255, 0))  # Should be 160

# EX 6
print("Test 6:", find_accessible_gray_background(128, 128, 128))  # Should be 200
