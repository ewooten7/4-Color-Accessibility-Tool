# Homework 4 - Building more with Functions and While Loops

For this assignment, you will explore working with isolated functions, and will include writing while loops in a few of those functions.  The primary goals for this assignment are

* Provide more practice with functions
* Provide practice with while loops
* Critical thinking and problem analysis
* Evaluating provided code 



As you work on this assignment, remember the order:

* define
* document
* implement
* test

For every function, you define it, you document it, you implement it, and then you test it - **Before** moving onto the next function!

## Accessibility Analyzer

A tool has been developed to help analyze colors, especially how they relate to accessibility for color blindness, contrast, and view-ability.  However, the tool needs you to develop the individual functions on how they work.

You will see [../src/color_tools.py](../src/color_tools.py) has the function definition and stubs already provided for you. Additionally, we have completed the two hardest functions, to leave seven functions for you to implement. Each of those seven has an "implementation" section as part of the docstring. While not normal, it seemed the best place to keep your work in once place. 

### Step 1 - Doctests - provided functions
Every function in [../src/color_tools.py](../src/color_tools.py) will need to have six (6) examples. We suggest you start with the two provided functions (`calculate_luminance(int, int, int)` and `simulate_colorblindness(int, int, int, str)`). For each function, analyze the code, run it in an interactive window to better understand it, and then generate three additional examples. 

> [!NOTE]
> Make sure to consistently run the code. You will see any doctest you add will automatically be run. 

### Step 2 - Other Functions

For each remaining function

* Add doctests - This will involve not only understanding what they are supposed to do, but probably work you will  need to do on paper working out solutions given different inputs. 
* implement
* test 

Needless to say, this assignment requires you to develop a deeper understanding of the underlining algorithm before you implement! This is an important skill for a computer scientist, and one that you won't learn right away. It takes practice (often many years), so don't worry if you struggle with it - that is part of the learning process. 



## Running Unit Tests
We have provided unit tests in [tests/test_color_tools.py](../tests/test_color_tools.py) to run after you have finished the application. You can run those tests in VS code or via the command line. Ideally your code should pass all of them. If it does not, you will want to evaluate why not. Looking through them will also help you think of edge cases you may have forgotten in your examples. 

## Running the Larger Application

You will need to run the final application. This is because we will have questions in the report that ask you to run the application, plus it is often more rewarding than just seeing tests pass. Have fun with it. 

To better understand colors, html values, and color blindness, see below!


## Report.md and README.md

👉🏽 **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files. 


As always you are free to ask about the questions in MS Teams, including clarifications on the code. 

## Coding Practice
Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1) 
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file). 

## 🤖 Use of LLMs
You should **not** use LLMs for writing your code. This is about learning the process, and without learning the process you may find it actually more difficult to generate code with LLMs. This is because the prompts for LLMs need to be exact, or they will make faulty assumptions about the code you are trying to generate (often generating incorrect test cases!). 

You are free to use LLMs to help you think of edge cases  **after** you have a working function. An example prompt could be:

> Please evaluate the following function focusing on these specific areas:
>
> 1. **Code correctness**: Does the implementation match the docstring description?
> 2. **Docstring completeness**: Are the parameters, return value, and examples clear and accurate?
> 3. **Edge cases**: What boundary conditions or unusual inputs could cause issues?
>
> For any edge cases you identify:
> - Explain why they're problematic
> - Show what would happen with specific input examples
> - Suggest how to handle them (documentation or code changes)
>
> Focus your feedback on the most important issues first. Assume this is for a beginner programming course at week 4 of our learning. We have not covered error checking yet, 
> nor should I include specialized statements for invalid input.
>
> (then paste in the single function you are looking at)

As part of your learning process, another example prompt could be:

> Can you describe a Python while loop to me, explaining each component: loop structure, condition design, variable initialization, and loop body organization. Use a while loop from basic programming (like counting, searching, or accumulating values) as your example. Assume I am a beginner. I have only covered variables, conditions, functions, and while loops - so do not included lists or other topics in the information.
>
> After your explanation, I want you to ask me THREE questions, but present them ONE AT A TIME. Wait for my response to each question before asking the next one.
> 
> Question requirements:
> 1. First question: Test my understanding of while loop components and common patterns
> 2. Second question: Give me a while loop specification (including purpose, loop condition, variables needed, and expected behavior) and ask me to write ONLY the loop structure with comments explaining the logic - no full implementation needed
> 3. Third question: Ask me to analyze potential problems with a while loop or suggest improvements to loop design
> 
> For question 2, evaluate my loop structure on these criteria:
> - Correct while loop syntax
> - Appropriate condition that will eventually become false
> - Proper variable initialization before the loop
> - Clear logic for updating the loop variable(s)
> - Comments explaining the loop's purpose and key steps
> - Includes safety considerations to prevent infinite loops
> 
> Be specific in your feedback about what's missing or could be improved in the loop design.

If you are struggling at translating the implementation paragraph to practice. (1) Message a TA or the instructor! but (2) here is a possible prompt that can help.

> I need help understanding how to implement an algorithm. I'll provide a paragraph describing what the algorithm should do, and I'd like you to help me think through the approach.
>
> Please analyze my algorithm description and provide:
>
> 1. **Key questions to consider**: What important details or clarifications should I think about before implementing?
> 2. **Approach suggestions**: What general strategy or pattern might work well for this type of problem?
> 3. **Potential challenges**: What parts might be tricky to implement or easy to get wrong?
>
> Focus on helping me think through the problem rather than providing step-by-step instructions. I want to develop my problem-solving skills and learn to ask the right questions when approaching algorithms. DO NOT include any code, but you may do formulas or pseudo-code.
>
> Here's my algorithm description:
> [paste algorithm description here]

## 📝 Grading Rubric

You will submit by linking to your github repository (in gradescope). You will need
to resubmit every time you want gradescope updated. 

### Rubric

1. Learning (AG)
   * passes basic tests
2. Approaching  (AG)
   * Passes more difficult tests including edge cases
   * passes PEP8 style check
3. Meets  (MG)
   * Every function in has at least 6 (six!) examples in docstring
   * Coding practice file provided
   * Report questions 1-7 answered correctly
4. Exceeds  (MG)
   * All Report questions answered properly, including links for references
   * Report deeper thinking answered with some thought, including links for references
   * No magic numbers are used in color_tools.py
   * Functions are DRY (make sure to call other functions as needed instead of duplicating code)


AG - Auto-graded  
MG - Manually graded



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Additional Resources


### Understanding Colorblindness

Roughly 8% of Northern European Descent are colorblind. However, application developers often fail to develop applications that can been seen by individuals with colorblindness, or even worse, they use colors to convey information that is not available in any other way. A recent example had a bus route applications that put 
blue on green to indicate a bus was on time. This was not accessible to individuals with colorblindness.

There are many different types of color blindness. The most common is red-green color blindness. This is where the individual has trouble distinguishing between red and green. For this assignment, we will be filtering
colors based on three types of color blindness: Protanopia, Deuteranopia, and Tritanopia.

* Protanopia - Red and Green is reduced in intensity.
* Deuteranopia - Red and Green is reduced in intensity, but more emphasis on Green.
* Tritanopia - Blue is reduced in intensity.

While this assignment over simplifies the testing of these colors (spoiler: this could be a fun final project to improve upon), it will give you a sense of how to use functions to break down a problem into smaller parts.

### Understanding RGB Values

RGB stands for Red, Green, Blue. It is a way of representing colors in a computer. Each color is represented by a number between 0 and 255. For example, the color white is represented by (255, 255, 255) and the color black is represented by (0, 0, 0). For this assignment we will be using RGB values. While true color is often a much wider range, and can include alpha (transparency) values, we will be using the simplified version.

While the code is provided, you will also print out the HTML values for the colors. HTML colors are represented by a # followed by 6 hexadecimal digits. For example, white is #FFFFFF and black is #000000. A hexadecimal digit is a number between 0 and 9, or a letter between A and F. The letters A through F represent the numbers 10 through 15. For example, the number 10 in hexadecimal is A, and the number 15 in hexadecimal is F. As you are covering binary in CS 5002 which is a "base 2" notation of numbers, hexadecimal is a "base 16" notation of numbers compared to our standard "base 10" notation. The reason HTML uses hexadecimal is because it is a more compact way of representing colors, representing 3 bytes (0-255) of information in 6 digits.


### Inclusive Design Resources
The following resources will be helpful in answering the Deeper Thinking in your report. Make sure to
cite them if you use them!

* [Microsoft Inclusive Design](https://inclusive.microsoft.design/)
* [What is Inclusive Design](http://www.inclusivedesigntoolkit.com/whatis/whatis.html)
* [W3Schools Design Tips](https://www.w3.org/WAI/tips/designing/)
* [10 Essential Guidelines for Colorblind Friendly Design](https://www.colorblindguide.com/post/colorblind-friendly-design-3)
* [Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
