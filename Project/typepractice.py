import time
from my_lib import validate_int, validate_alphabet, validate_password
from wordlist import word_list
import random

quit_game = False
quit_manager = False
quit_program = False
total_words_typed = 0
total_time = 0
mistakes = 0

#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def get_action(type):
    if type == "menu":
        print("Type N for a new note. Type file number for details. Type /exit to exit manager-mode.")
    if type == "further":
        print("Type D to delete, E to edit, R to resume.")

    action_key = input()
    if len(action_key) != 0:
        if validate_int(action_key) is not None and validate_int(action_key) <= len(list(manager)):
            return "number", int(action_key)
        elif validate_alphabet(action_key) is not None and validate_alphabet(action_key) in "NDER":
            return "letter", str(action_key)
        elif len(action_key) > 0:
            if action_key[0] == "/":
                return "command", str(action_key)
        else:
            print("\033[91mPlease enter a valid command\033[0m")
            return "", ""
    else:
        print("\033[91mPlease enter a valid command\033[0m")
        return "", ""

def encryption(data):
    result = ""
    raw = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@;:`-^$%&'!#_?>< "
    enc = "亜哀挨愛曖悪握圧扱宛嵐安案暗以衣位囲医依委威為畏胃尉異移萎偉椅彙意違維慰遺緯域育一壱逸茨芋引印因咽姻員院淫陰飲隠韻右宇羽雨唄鬱畝浦運雲永泳英映栄営詠影鋭衛易 "
    for i in range(len(data)):
        result += enc[raw.index(data[i])]
    return result

def decryption(data):
    result = ""
    raw = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@;:`-^$%&'!#_?>< "
    enc = "亜哀挨愛曖悪握圧扱宛嵐安案暗以衣位囲医依委威為畏胃尉異移萎偉椅彙意違維慰遺緯域育一壱逸茨芋引印因咽姻員院淫陰飲隠韻右宇羽雨唄鬱畝浦運雲永泳英映栄営詠影鋭衛易 "
    for i in range(len(data)):
        result += raw[enc.index(data[i])]
    return result


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
while quit_program is False:
    quit_manager = False
    quit_program = False
    total_words_typed = 0
    mistakes = 0

    print("\033[96m===============================\033[0m")
    print("\033[96m Welcome to TyPra,             \033[0m")
    print("\033[96m       typing practice for you \033[0m")
    print("\033[96m===============================\033[0m")
    print("Once you start, a timer will start.")
    print("Type \033[91m/exit\033[0m while practicing to exit and see your results.")
    initiate = input("\033[33mType anything to start.\033[0m")
    print("Starts in")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    while quit_game is False:
        word = word_list[random.randint(0,len(word_list)-1)]
        print("___________________")
        print(word)
        start = time.time()
        time_taken = 0
        command = input()
        if command == word:
            end = time.time()
            time_taken = round(end-start, 2)
            wps = len(word)/time_taken
            total_words_typed += len(word)
            total_time += time_taken

            if wps < 80/60:
                print("\033[33mLEVEL: Beginner\033[0m")
            elif wps < 120/60:
                print("\033[33mLEVEL: Intermediate\033[0m")
            else:
                print("\033[33mLEVEL: Expert\033[0m")

            print("\033[96mcorrect\033[0m")
            print("<time taken: ", time_taken, ">")
        elif command == "/exit":
            print("+++++++++++++++++++++++++++++++")
            print("Thank you for playing, keep it up!")
            if total_time > 0:
                print("Today's average words per second: ", round(total_words_typed/total_time,2))
                if total_words_typed/total_time < 80/60:
                    print("LEVEL: Beginner")
                elif total_words_typed/total_time < 120/60:
                    print("LEVEL: Intermediate")
                else:
                    print("LEVEL: Expert")
            print("Total mistakes: ", mistakes)
            print("+++++++++++++++++++++++++++++++")
            time.sleep(5)
            exit()
        elif command == "shortcut":
            end = time.time()
            time_taken = round(end - start, 2)
            if 0 <= time_taken <= 20: # change the first one to 15 when finishing the product
                print("time taken: ", round(end - start, 2))
                print("\033[35m<<<secret procedure entered>>>\033[0m")
                print("\033[35minitiating password manager...\033[0m")
                quit_game = True
            else:
                print("\033[91mincorrect\033[0m")
                mistakes += 1
        else:
            print("\033[91mincorrect\033[0m")
            mistakes += 1

    while quit_manager is False:
        with open('wordlist_backup.csv', 'r') as f:
            data = f.readlines()

        manager = {}

        for line in data:
            stripped_lines = line.strip()
            tool, password = stripped_lines.split(",")
            manager[decryption(tool)] = decryption(password)

        print("===============================")
        print("Saved passwords:")
        for i in range(len(list(manager))):
            print(f"[{i + 1}] {list(manager)[i]}")

        command_type, command = get_action("menu")

        if command_type == "number":
            temp = command
            print(f"Tool: {list(manager)[command-1]}     Password: {manager[list(manager)[command-1]]}")
            command_type, command = get_action("further")
            if command == "D":
                manager.pop(list(manager)[temp-1])
                with open('wordlist_backup.csv', 'w') as f:
                    f.writelines("")
                for i in list(manager.keys()):
                    with open('wordlist_backup.csv', 'a') as f:
                        f.writelines(f"{encryption(i)},{encryption(manager[i])}\n")
            elif command == "E":
                manager.update({list(manager)[temp-1]: input("New password: ")})
                with open('wordlist_backup.csv', 'w') as f:
                    f.writelines("")
                for i in list(manager.keys()):
                    with open('wordlist_backup.csv', 'a') as f:
                        f.writelines(f"{encryption(i)},{encryption(manager[i])}\n")
            elif command == "R":
                continue
        elif command_type == "letter":
            if command == "N":
                new_tool = validate_alphabet(input("What is the new tool you want to save a password for?: "))
                new_password = validate_password(input("What is the password? available characters: a-z A-Z 0-9 @;:`-^$%&'!#_?>< : "))
                if new_tool is not None and new_password is not None and new_tool not in manager and len(new_tool.strip()) != 0 and len(new_password.strip()) != 0 and " " not in new_password:
                    manager.update({new_tool: new_password})
                    with open('wordlist_backup.csv', 'a') as f:
                        f.writelines(f"{encryption(new_tool)},{str(encryption(new_password))}\n")
                        print(f"\033[96mnew tool {new_tool} is added with the password of {new_password}\033[0m")
                else:
                    print("\033[91mInvalid input: Unavailable characters / Same name not allowed\033[0m")
                    continue
        elif command_type == "command":
            if command == "/exit":
                quit_game = False
                quit_manager = True
                break

exit()
