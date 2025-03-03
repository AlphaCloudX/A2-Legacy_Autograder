import subprocess
import calendar
import re

"""
This uses the default python library for the calendar to check your year ranges
"""
def generate_calendar(year):
    calendar.setfirstweekday(calendar.SUNDAY)  # Set Sunday as the first day of the week
    month_names = [calendar.month_name[month] for month in range(1, 13)]
    calendar_str = ""

    for row in range(0, 12, 3):
        # Append month names
        calendar_str += f"{month_names[row]:^22}  {month_names[row + 1]:^22}  {month_names[row + 2]:^22}\n"
        # Append weekdays headers
        calendar_str += ("Su Mo Tu We Th Fr Sa  " * 3).strip() + "\n"

        # Get month calendars with proper starting weekday
        month1 = calendar.monthcalendar(year, row + 1)
        month2 = calendar.monthcalendar(year, row + 2)
        month3 = calendar.monthcalendar(year, row + 3)
        max_weeks = max(len(month1), len(month2), len(month3))

        # Ensure all months have equal number of weeks by appending empty weeks
        while len(month1) < max_weeks:
            month1.append([0] * 7)
        while len(month2) < max_weeks:
            month2.append([0] * 7)
        while len(month3) < max_weeks:
            month3.append([0] * 7)

        # Append each week for the three months side by side
        for week in range(max_weeks):
            for week_days in (month1[week], month2[week], month3[week]):
                calendar_str += " ".join(f"{day:2}" if day != 0 else "  " for day in week_days) + "  "
            calendar_str = calendar_str.rstrip() + "\n"
        calendar_str += "\n"

    return calendar_str

def run_cal(input_data):
    # Run the local ./cal program
    process = subprocess.Popen(['./cal'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Send input and get the output + error
    output, error = process.communicate(input=input_data)

    if process.returncode != 0:
        print(f"Error: {error}")
    
    return output

print("Welcome To A2 Legacy Autograder")
print("This program will automatically navigate your menu by answering the questions.")
print("Tested only on a linux environment! May Not Work On Other Platforms!")
print("Instructions:")
print("- Answer each question as if you were interacting with your program.")
print("- *IMPORTANT* If a question expects a year, enter the word 'year'.")
print("- Type 'done' when you've finished answering all questions.")
print("- Watch the video if you are confused :)")
print("--------------------------------------------------")

counter = 1
answers = []


while True:
    answer = input(f"Question {counter} answer: ")
    
    if answer.lower() == "done":
        break
    
    answers.append(answer)
    counter += 1

print("Now Enter A Range Of Years To Test, They Must Be Valid!")
start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

enable_debug_output = input("Would you like to enable debug output if a test case fails? (yes/no): ").strip().lower() == 'yes'
stop_on_failure = input("Would you like to stop testing if a test case fails? (yes/no): ").strip().lower() == 'yes'

# Results will be stored as booleans
print(f"Debug output enabled: {enable_debug_output}")
print(f"Stop testing on failure: {stop_on_failure}")







# ANSI escape codes for colors
RED = "\033[31m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BLUE = "\033[34m"
WHITE = "\033[37m"
BRIGHT = "\033[1m"
RESET = "\033[0m"

# Additional colors for the rainbow effect
COLORS = [
    RED,  # Red
    "\033[38;5;214m",  # Orange (using 256-color mode)
    YELLOW,  # Yellow
    GREEN,  # Green
    CYAN,  # Cyan
    BLUE,  # Blue
    MAGENTA,  # Magenta
    "\033[38;5;13m",  # Violet (using 256-color mode)
    "\033[38;5;81m",  # Indigo (using 256-color mode)
    WHITE,  # White
]

# Assuming 'start_year', 'end_year', 'answers', 'run_cal', 'generate_calendar', 'enable_debug_output', and 'stop_on_failure' are defined

print("\nRunning the program...\n")

color_index = 0.0  # Initialize the color index for the wave effect

# A new variable to control how many times a color is repeated before it transitions
color_repeats = 3  # Increase this to make each color last longer

for year in range(start_year, end_year):
    print(f"Checking {year} | ", end="")

    # Convert answers into a single input string with newlines
    input_data = "\n".join([str(year) if a == "year" else a for a in answers]) + "\n"

    # Split the output into individual lines that we will compare against
    user_output_pre = run_cal(input_data)
    answer_output_pre = generate_calendar(year)

    user_output = user_output_pre.split('\n')
    answer_output = answer_output_pre.split('\n')

    # Find where the calendar actually begins to skip any previous lines
    index_user = next((i for i, word in enumerate(user_output) if "january" in word.lower()), -1)
    index_answer = next((i for i, word in enumerate(answer_output) if "january" in word.lower()), -1)

    # Slide to only get the Months and onwards
    sliced_user = user_output[index_user:]
    sliced_answer = answer_output[index_answer:]

    # Remove all empty lines or spaces
    cleaned_user = [word for word in sliced_user if word.strip()]
    cleaned_answer = [word for word in sliced_answer if word.strip()]

    # Combine the list, we will then begin to compare the cleaned string
    combined_user = ''.join(cleaned_user)
    combined_answer = ''.join(cleaned_answer)

    # Remove all whitespace using regular expression
    user = re.sub(r'\s+', '', combined_user)
    answer = re.sub(r'\s+', '', combined_answer)

    if user == answer:
        # Apply rainbow wave effect only for passes
        print(f"{COLORS[int(color_index) % len(COLORS)]}{BRIGHT}Pass!{RESET}")
        color_index += 0.1  # Move to the next color for the next pass

    else:
        # Fail remains red
        print(f"{RED}{BRIGHT}Fail! <------{RESET}")

        if enable_debug_output:
            print(f"{YELLOW}{BRIGHT}YOUR PROGRAM OUTPUT!!!{RESET}")
            print(user_output_pre)
            print(f"\n{YELLOW}{BRIGHT}ANSWER PROGRAM OUTPUT!!!{RESET}")
            print(answer_output_pre)

        if stop_on_failure:
            print(f"{MAGENTA}{BRIGHT}Terminating!!!{RESET}")
            break

print(f"\n{CYAN}{BRIGHT}Program Finished{RESET}")

