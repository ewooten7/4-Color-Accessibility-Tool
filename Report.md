# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you use the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)


1. Correct the following loop.
   ```python
   value = None
   while value == "quit":
       value = input("Enter a value or quit: ")
       print(value)
   ```
# Correction:
    ```python
    value = ""
    while value != "quit":
        value = input("Enter a value or quit: ")
        print(value)

    ```

2. The above code uses a None value to initialize the input variable. This works because python can let a variable be multiple types, but in some languages, you would have to match the type. Assuming you had to match the type (str), what would be a good default input value, that could never cause the loop to not run at least once? Provide reasoning for your logic as there are multiple correct answers. With that said, there is one that is more 'standard' than the rest, so feel free to openly discuss options that come to mind (you do not have to come up with the standard answer, but try to!). 

# If making a while loop that required your input to match a specific value type (like a "string"), an easy way to go about this is to place an empty string "", like I did above. This works because it matches the expected value type. Many language have a similar style (like C# in my experience) have similar conventions. You would have to declare the type explicitly and give the string an initial value before entering the loop. So this is a good practice!
   

3. Write a small loop that will keep repeating until someone 
   enters a number greater than 0, and less than 5. It has to be
   whole numbers (hint: look up .isnumeric() from the team activity).

   ```python
    while True:
        value = input("Enter a number b/t 0 and 4. Whole Numbers only, please! ")

        if value.isnumeric():
            num = int(value)
            if 0 < num < 5:
                print("Thanks for following directions, lol. You entered:", num)
                break
            else:
                print("Bro, you gotta give a number GREATER than 0 but LESS than 5.")
        else:
            print("Yo mama raised you better >:( Enter a WHOLE number please. I'm not mad, just disappointed...")

   ```



4. Draw a flow diagram for your solution to #3
[Flow chart of simple Loop:](<images/Small Loop1_chart.png>)

5. Looking back at homework #2, we actually had a type of 'loop' in the provided code (look near the main function). First copy the bit of code that causes the loop.
    ```python
    def main():
    """
    Asks the client for two temperatures. Based on the values, it provides cities
    that meets the conditions. Temperatures are whole numbers only.   
    """
    temp1 = get_number("Enter a temperature: ")
    temp2 = get_number("Enter a second temperature: ")

    if check_lower(temp1, temp2):
        low = temp1 
        high = temp2
    else:
        high = temp1
        low = temp2

    cities = get_cities(low, high)

    print(cities.strip())  # .strip() removes leading and trailing whitespace

    again = input("Run again (y or n)? ")
    if again.strip().lower() == 'y':
        main() 
    else: 
        print("Good luck on the move!")

    ```

    Now: what would be some of the pros and cons of looping in such a way (think about 'frames' you see in the python visualizer)?

# I think one of the pros of running it this way is that the control flow is easy to follow and the syntax is simple. However, when I checked the Python visualizer, I saw it takes about 34 steps before reaching the “Run again (y or n)?” line. Each time the program repeats, a new frame for main() is created instead of reusing the same one, which slowly builds up memory usage. So while this recursive loop works, it’s less efficient than using a regular while loop that keeps everything in one frame.

# Helpful references:
## https://docs.python.org/3/tutorial/controlflow.html#defining-functions

## https://realpython.com/python-recursion/

6. Thinking about edge cases, it is very common to get an off-by-one (OB1) error with loops. 
   Create two test cases (just as examples/inputs) for the following code. They 
   should both be 'correct' cases, but one of them should uncover the error in the code.

   ```python
    def count_backwards(value: int) -> None:
        """ Counts from value to 0, printing even values until 10 (including 10), and 
        then odd values."""
       counter = value
       while counter >= 0:
          if counter > 10:
            if counter % 2 == 0:
                print(counter)
          else:
            if counter % 2 == 1:
                print(counter)
          counter -= 1
   ```
   * Example test one:
   >>> count_backwards(12)
   # Expected Output:
   12
   10
   9
   7
   5
   3
   1 

   # What I got instead:
   12
    9 #Right here.
    7
    5
    3
    1

   * Example test two:
   >>> count_backwards(9)
    # Output I got:
    9
    7
    5
    3
    1

    Seems to work! Trying different numbers showed issues when number > 10.



 7. When thinking of these edge cases and OB1 errors, it is common to say one should test
    every condition plus-minus 1. In your opinion, is this beneficial? Why or why not?
    # This is generally benefecial, but you may not be able to do it with EVERY plus-minus 1. Theoretically, if it were possible to try EVERY single case, but this is unrealistic and ultimately unpractical. There are a universe-size of possibilities to test on one function alone. That is why edge cases are designed to try to capture as many fringe scenarios that are also the most commonplace (that is, issues most likely to impact the functionality of an app or whatever it is you are making.) So trying to employ a plus-minus one on many cases is ideal, but test case must NOT be restricted to these kind of tests alone. There are countless other edge cases that may take presedence over this simple test alone, such as when working with large numbers or other things like this.


## Application Runs
The following questions will require you run the Accessibility Analyzer to generate results. 

> Do display colors in the markdown, you will have to switch to standard html and built in styles. For example, the code below, will generate a 'teal' block with black text. Feel free to copy and past the block, only modifying the color values as you need.   
> ![#4ECDC4](https://placehold.co/15x15/4ECDC4/4ECDC4.png) `#4ECDC4`

1. Check WCAG contrast compliance - pick two colors to run with the WCAG option (1) in the color app.
   
   1.1  What two colors did you pick (use the color block but update values)
      * ![#F5C518](https://placehold.co/15x15/F5C518/F5C518.png) `#F5C518`
      * ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) `#FFFFFF`

# White and a Bright Yellow color

   1.2  What was the result, use the block below to copy and paste the result of the test

   ```
Enter background color:
Hex color (e.g., #FF8040 or FF8040): FFFFFF

==================================================
        CONTRAST RESULTS
==================================================
Text: #f5c518 | RGB(245, 197, 24) | View Color
  Brightness: 191/255 (Bright)
  Luminance: 0.594
Background: #ffffff | RGB(255, 255, 255) | View Color
  Brightness: 255/255 (Very Bright)
  Luminance: 1.000

Contrast Ratio: 1.6:1

WCAG COMPLIANCE:
✗ AA Normal Text (4.5:1) - FAIL
✗ AA Large Text (3:1) - FAIL
✗ AAA Normal Text (7:1) - FAIL
✗ AAA Large Text (4.5:1) - FAIL
   ```

   1.3 Did the results show what you though?  

   RECOMMENDATION:
Significant contrast improvement needed - consider much darker or lighter colors. 
# Obviously bright yellow and White are very hard to see, even with people who do NOT have colorblindness! Not accessible.

   1.4 Explore colors until you can find two that pass all the WCAG compliance categories.  What two did you find?
       
      * ![#0D3B66](https://placehold.co/15x15/0D3B66/0D3B66.png) `#0D3B66`
      * ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) `#FFFFFF`
  
==================================================
        CONTRAST RESULTS
==================================================
Text: #0d3b66 | RGB(13, 59, 102) | View Color
  Brightness: 50/255 (Very Dark)
  Luminance: 0.042
Background: #ffffff | RGB(255, 255, 255) | View Color
  Brightness: 255/255 (Very Bright)
  Luminance: 1.000

Contrast Ratio: 11.4:1

WCAG COMPLIANCE:
✓ AA Normal Text (4.5:1) - PASS
✓ AA Large Text (3:1) - PASS
✓ AAA Normal Text (7:1) - PASS
✓ AAA Large Text (4.5:1) - PASS

OUTSTANDING: Exceeds all accessibility standards!

2.  Analyze color properties - pick a color to run with this option

    2.1 What color did you pick?
    
       * ![#06D6A0](https://placehold.co/15x15/06D6A0/06D6A0.png) `#06D6A0`
    
    2.2 What are the results, copy and paste them below.
     ```
==================================================
        ANALYSIS RESULTS
==================================================
Color: #06d6a0 | RGB(6, 214, 160) | View Color
  Brightness: 145/255 (Medium)
  Luminance: 0.507

WEB ACCESSIBILITY ANALYSIS:
Gray backgrounds meeting WCAG AA: 16 out of 52
Darkest accessible gray: #000000 | View Color

WEB DESIGN SUGGESTIONS:
- Versatile mid-tone color
- Test contrast with intended backgrounds
     ```

3. Test colorblind accessibility - pick two colors to analyze. You need to find two that would end up being the same color (or close to the same color) depending on the type of color blindness. 

    3.1 What colors did you pick?

     * ![#FF0000](https://placehold.co/15x15/FF0000/FF0000.png) `#FF0000`
     * ![#00FF00](https://placehold.co/15x15/00FF00/00FF00.png) `#00FF00`

    3.2 What were the results for each of them - copy and paste below in each block
    ```
==================================================
        SIMULATION RESULTS
==================================================
Original: #00ff00 | RGB(0, 255, 0) | View Color

How this appears to colorblind users:
Protanopia (Red-Green Type 1): #7f7f00 | RGB(127, 127, 0) | View Color
Deuteranopia (Red-Green Type 2): #3f3f00 | RGB(63, 63, 0) | View Color
Tritanopia (Blue-Yellow): #00ff7f | RGB(0, 255, 127) | View Color

    ```
    ```
==================================================
        SIMULATION RESULTS
==================================================
Original: #ff0000 | RGB(255, 0, 0) | View Color

How this appears to colorblind users:
Protanopia (Red-Green Type 1): #7f7f00 | RGB(127, 127, 0) | View Color
Deuteranopia (Red-Green Type 2): #bfbf00 | RGB(191, 191, 0) | View Color
Tritanopia (Blue-Yellow): #ff0000 | RGB(255, 0, 0) | View Color
    ```

    3.3 Now run modified (by the colorblindness type) colors through the Check WCAG contrast compliance option. Spoiler, at least one should fail, but there may be rare cases it passes. You should also run the original colors through the Check WCAG.
 
     * ![#3f3f00](https://placehold.co/15x15/3f3f00/3f3f00.png) `#3f3f00`
     * ![#bfbf00](https://placehold.co/15x15/bfbf00/bfbf00.png) `#bfbf00`

    3.4 What were the results for that test
    ```
==================================================
        CONTRAST RESULTS
==================================================
Text: #7f7f00 | RGB(127, 127, 0) | View Color
  Brightness: 112/255 (Medium)
  Luminance: 0.197
Background: #7f7f00 | RGB(127, 127, 0) | View Color
  Brightness: 112/255 (Medium)
  Luminance: 0.197

Contrast Ratio: 1.0:1

WCAG COMPLIANCE:
✗ AA Normal Text (4.5:1) - FAIL
✗ AA Large Text (3:1) - FAIL
✗ AAA Normal Text (7:1) - FAIL
✗ AAA Large Text (4.5:1) - FAIL

RECOMMENDATION:
Significant contrast improvement needed - consider much darker or lighter colors


    ```

    3.5 Did your your original colors pass better than the modified color blindness ones?

# No, they all failed on both side.

4. Did running this application help you learn anything new about html / web colors? If so, what?

# Yes, this taught me a lot about color blindness and its different types. I knew of different types of color-blindness, but I never had to consider it on any kind of project I have ever worked on before. Not just in tech-related work, but any kind of collaborative project where colors are considered! I knew about hexadecimals since I was a kid, but I see their necessity now for not just creative quantifiable/calculative changes to colors, but also using that to help with accessibility.

> Make sure to look at your rendered document in github!  
> Before you turn it in for grading.


## Deeper Thinking

Human Computer Interaction (HCI) is a field within computer science that focuses on how people interact with technology systems. It involves designing interfaces and experiences by continuously communicating with stakeholders, conducting research into effective design patterns, and questioning assumptions about user behavior and needs. 

HCI emphasizes inclusive design - creating systems that work for people across different abilities, backgrounds, and contexts. This approach extends beyond basic accessibility compliance to consider the full spectrum of human diversity. Whether designing web applications, operating systems, VR/AR experiences, or video games, HCI practitioners integrate user research and inclusive principles throughout the development process.

HCI intersects with virtually all domains of computer science and relies heavily on collaboration between designers, developers, researchers, and clients to build systems that better serve diverse communities.

**Assignment:**

Research HCI and UX design to understand the field better. Find at least three credible sources (academic articles, professional publications, or reputable industry resources) and provide links to them. 

After reviewing your sources, write a reflection addressing these questions:

1. Based on your research, how would you define HCI and its core principles?

# I would define the HCI as the study of how humans interact with computer systems. It is fascinating to be because this field is intentionally interdisciplinary, understanding the many elements involved with how human beings interact with technological mediums, and the necessity of incorporating fields like computer science, psychology, and design into its focuses. It focuses on crucial areas within UI and UX, like usability, feedback, consistency, and everything under the umbrella of 'inclusive design' (i.e. this entire WCAG accessibility analyzer experiment.)


2. Why is inclusive design particularly important in computer science and HCI? Consider both ethical and practical implications.

# Inclusive design is essential for computer science and HCI because people all over the world and with all kinds of conditions and situations will be interfacing with computers, or things created with this technology. Emphasizing inclusive design is clearly ethical and humanitarian, but there is also has a concrete financial and practical price for failing to consider it as well. The humanitarian angle is clear in considering peoples' different disabilities, like color-blindness. But on the financial and practical side, failing to make a WCAG compliant website could cost a company significant money for hindering all people's ability to interface with their site, and money and time to correct it.  

3. How might the accessibility concepts you learned in this assignment (color contrast, colorblindness considerations) connect to broader HCI principles?

This assignment’s focus on color contrast and colorblindness illustrates core HCI ideas: perceptibility, feedback, and universal usability. Testing color accessibility mirrors the HCI process of iterative evaluation, improving interfaces based on measurable user experience outcomes. Designing for visibility and readability is one of the most direct ways computer scientists practice inclusive human-centered design. This is also used in other design principles across all fields. For example, stop signs are both red AND octagonal for this reason, along with other signs. When working on any kind of project, it is important to fully consider all possibilities of how we can make it accessible to everyone using it.

# References:

1. Codacy. (2025, October 9). What is clean code? A guide to principles and best practices. https://blog.codacy.com/what-is-clean-code 

2. What is Human-Computer Interaction (HCI)? (2016, June 6). The Interaction Design Foundation; Interaction Design Foundation. https://www.interaction-design.org/literature/topics/human-computer-interaction?srsltid=AfmBOorG2ljpIm02okt3c2gVyeVplhRMl7khqcXv8B18s4I0mAxI6dAF

3. U.S. Access Board. Chapter 7: Signs. (n.d.). https://www.access-board.gov/ada/guides/chapter-7-signs/ 

4. World Wide Web Consortium (W3C). (n.d.). Introduction to accessibility. Web Accessibility Initiative (WAI). https://www.w3.org/WAI/fundamentals/accessibility-intro/


Your reflection should demonstrate understanding of the field while incorporating insights from your research sources. Write in paragraph form rather than bullet points, and aim for thoughtful analysis rather than simple summaries.


