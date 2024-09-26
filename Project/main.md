
# Project Unit 1: A Simple Typing Practice Software

## Criteria A
### Problem definition

My client is an owner of an educational institution that conducts academic proficiency tests among high school tests. They have a database where they store exam problems and answers, which its folder and file requires individual passwords to access for security. Her employees have been using hand-written notes to store the passwords, but because they handle many paperwork such as exam papers, they sometimes accidentally get lost. Also, hand-written passwords are prone to misreading, which is problematic for precision required for passwords. Along side, the owner of the company has a concern where generally the literacy towards digital technology is low amongst employees, which is unideal in an increasingly digitalizing world.

### Proposed Solution

I propose a software that can run on multiple platforms, mainly windows and iOS, which behaves like a typing practice appication, but has a hidden functionality of a encrypted password manager for the database the institution uses. By digitalizing the storage of passwords, it is largely less likely that the passwords become unreachable, or get misread or miswritten due to flaws in handwriting. The password manager will only open when the secret code is entered within a specific time span, which works as a strong countermeasure towards unauthorized access. The password manager stores data in a csv file, because it is capable of holding an infinitely large sets of data if a hardware has enough space, and there is clear structural correspondance between keys and values which minimizes the risk of turmoil of important passwords. Within the files, the programs store encrypts data using Japanese kanji which has no association with its original letters, 

resonable explanation for software details (e.g. filetypes)
- multi-platform

### Success criteria
Basic Tool Functionality

Typing practice:
1.  Gives user a random word from large volume word list
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

### Design cycle
| **Task number** | **Planned action**                     | **Planned outcome**          | **Time estimated** | **Target completion date** | **Criterion** |
|-----------------|----------------------------------------|------------------------------|--------------------|----------------------------|---------------|
| 1               | Consider the  necessity of the project | Get approval from the client | 25 minutes         | Sep 12th                   | A             |
|                 |                                        |                              |                    |                            |               |
|                 |                                        |                              |                    |                            |               |

## Criteria B
### System diagram
![image](https://github.com/user-attachments/assets/931ef831-0cad-4143-af34-04cc203f6994)
### Flow diagrams
![image](https://github.com/user-attachments/assets/2e251154-744a-48e0-84fe-6c07a47215d2)




## Criteria C
