# A2-Legacy_Autograder

This project is an auto-grader tool that helps evaluate certain outputs based on calendar functionality. Below is a guide to setting up and running the program.

## Setup

### 1. Clone the repository
First, you need to clone the repository to your local machine. Open your terminal and run the following command:
```bash
git clone https://github.com/AlphaCloudX/A2-Legacy_Autograder.git
```

### 2. Place the Python file in the executable folder
Copy the Python file into the same directory where your executable is located.

### 3. Run the Python program
Once the Python file is in the correct location, run the following command in the terminal to start the program:
```bash
python3 runCal.py
```
If python3 doesn't work, try python but you must have python version 3 installed.

```bash
python runCal.py
```

or

```bash
py runCal.py
```

or

```bash
py -3 runCal.py
```


## How to Use the Program

When you run the program which then runs your program, it doesn't automatically know what questions it will ask, what kind of answers it expects, or in what order.

Your job is to provide the answers to each question in the order they appear. The script will use your answers to run the program.

For example, if your program asks these questions and expects the following inputs:
```bash
Enter a year:
1950
Enter 0 for English, 1 for French:
0
program runs...
```

Then, when filling out the script, your answers will look like this:
```bash
Question 1:
year
Question 2:
0
Question 3:
done
```

This way, the script knows how to respond to each question based on the answers you provide.

## Program Functionality

The program works by skipping over the banner section of a calendar and finding the location of January. It then removes all the white space below and compares it to the expected output based on the Python standard library calendar.

**Key Features:**
- The program removes unnecessary white space and outputs only the calendar data for comparison.
- RGB output has been added to enhance the display.


