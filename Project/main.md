
# Project Unit 1: A Simple Typing Practice Software (typepractice.py)

## Criteria A
### Problem definition

My client is an owner of an educational institution that conducts academic proficiency tests among high school tests. They have a database where they store exam problems and answers, which its folder and file requires individual passwords to access for security. Her employees have been using hand-written notes to store the passwords, but because they handle many paperwork such as exam papers, they sometimes accidentally get lost. Also, hand-written passwords are prone to misreading, which is problematic for precision required for passwords. Along side, the owner of the company has a concern where generally the literacy towards digital technology is low amongst employees, which is unideal in an increasingly digitalizing world.

### Proposed Solution

I propose a software that can run on multiple platforms, mainly windows and iOS, which behaves like a typing practice appication, but has a hidden functionality of a encrypted password manager for the database the institution uses. By digitalizing the storage of passwords, it is largely less likely that the passwords become unreachable, or get misread or miswritten due to flaws in handwriting. The password manager will only open when the secret code is entered within a specific time span, which works as a strong countermeasure towards unauthorized access. The password manager stores data in a csv file, because it is capable of holding an infinitely large sets of data if a hardware has enough space, and there is clear structural correspondance between keys and values which minimizes the risk of turmoil of important passwords. Within the files, the program stores data with encryption using Japanese kanji which has no association with its original letters, functioning as indecipherable, random symbols to avoid leaks of passwords for exam papers by cyber attacks. Its main function as a typing practice software enhances the capability of the employees to handle digital tools, which the owner was anxious about.

### Success criteria
Basic Tool Functionality

Typing practice:
1.  User gets a random word from a large variety of words
2.  User can type the word in and they can know if the input is correct or not
3.  User can know their skill level each answer and when they end the practice based on letters per second
4.  User Interaction:
      - Uses the terminal to interact with the user.

Hidden Functionality:

1.  If the user enters the secret code with a specific time taken, the program will change modes and act as a password manager
2.  In password manager mode, the user should be able to
      - Add a password
      - View the stored passwords
      - Edit the stored passwords
      - Delete the stored passwords
3.  Basic Security Features:
      - Stores passwords in a csv file.
      - Tools and passwords are encrypted into designated random Kanji characters letter by letter
4.  User Interaction:
      - Uses the terminal to interact with the user.


## Criteria B
### System diagram
![image](https://github.com/user-attachments/assets/931ef831-0cad-4143-af34-04cc203f6994)
### Flow diagrams
![image](https://github.com/user-attachments/assets/2e251154-744a-48e0-84fe-6c07a47215d2)
### Test plan
1. Create justification of the proposal (Sep 12th)
2. Check with client (Sep 12th)
3. Develop prototype: Minimal Viable Product on typing practice function (Sep 16th)
   - Evaluation of user input
   - Calculation of time taken for user input
4. Develop prototype: Minimal Viable Product on password manager function (Sep 17th ~ Sep 25th)
   - Validation of user input command, menu function based on command
   - Entry of data from dictionary to csv file
   - Refreshment of data in csv file
   - Encryption and decryption of data entry
5. Finalize product (Sep 26th ~ Sep 27th)
   - Further validation against illegal input such as no string, only spacebar
   - Repetition of menu and mutual accessibility between typing practice and password manager
   - Improve visibility: add colors and bars in the user interface
6. Presentation to the client with the finished product (Sep 27th)

## Criteria C
### Existing tools that had been used
- Python: A widely used comprehensive programming language that is close to human language, and is friendly for the programmer.
- PyCharm: An IDE than can be used to write and compile python, with a virtual environment.
- Function: A programming method that isolates the process from the main flow to avoid complication and repeated notation. In this solution they are used for getting input for commands to manipulate the password manager, and encryption/decryption process, which appear frequently in the code.
- For loop: A programming method that allows the code to apply repeated processes over sequential data. In this solution they are used in many parts where processes on components of a data is required.
- While loop: A programming method that allows the code to apply repeated processes with a set condition. In this solution they are used in the framwork of the main flow of the program, to repeat steps while required.
- Input validation: A programming method that prevents syntax errors in a code by checking if the input is qualified with the correct format and range. In this solution, they are used in every process which requires the user to input string or command.
- If statements: A programming method that allows a program to perform different processes according to a condition. In this solution they are used in every process where the code depends on user input or other conditions that differ from user interaction.
- Encryption: A programming method that strengthens data security by making the data hardly indecipherable. In this solution they are used in processes that writes data on a database as a countermeasure to cyber attacks.
- Random: A tool that allows the code to generate pseudo random numbers for the code to behave randomly. In this solution it is used to give the user a random word to type. Source code: https://github.com/python/cpython/blob/3.12/Lib/random.py
- Time: A tool that allows the code to take time into account for its process. In this solution it is used to calculate the time that requires the user to enter the correct word. Source: https://docs.python.org/3/library/time.html
- NLTK: A tool that allows python to extendedly handle human languages. In this solution it was used to create the 1,000 random words that appear in the type practice. Source: https://www.nltk.org/api/nltk.corpus.html
