import random
import re
import copy
from database import *
if exists():
    spam = get("Player","spam")
    over = get("Player","over")
else:
    spam = 0
    over = 0
last_ip = []
def pin(attempts,length,breaker=False):
    in_at = attempts
    pin = ""
    pin1 = ""
    for x in range(0,length):
        pin += str(random.randint(0,9))
    print("Guess the pin '#' next to a number - means you are close to guessing it '*' next to a number - means the number is right")
    if breaker:
        print("Got pin code: {}?".format(pin[:-1]))
    pn = ""
    while pn != pin and attempts > 0:
        print(pin1)
        pn = input("Enter pin: ")
        if pn == pin:
            break
        pin1 = ""
        for num in range(0,len(pn)):
            mn = pn[num]
            try:
                rn = pin[num]
            except:
                rn = "-1"
            sign = ""
            if mn == rn:
                sign = "*"
            elif int(mn) in range(int(rn),(int(rn) + 2)) or int(mn) in range((int(rn)-2), int(rn)):
                sign = "#"
            pin1 += mn + sign
        attempts -= 1
        if attempts == 3:
            print("3 more attempts remaining")
    attempts -= 1
    if pn == pin:
        print("Congratz the pin was " + pin)
        print("You guessed it in {}/{} attempts".format(in_at-attempts,in_at))
        return True
    else:
        print("You failed the pin was "+ pin)
        return False
def check(ls):
    if (ls[0][0] == ls[1][1] and ls[1][1] == ls[2][2]) or (ls[0][2] == ls[1][1] and ls[1][1] == ls[2][0]):
        return True
    return False
def magic_square(gone,hard=2):
    square = [[0 for c in range(3)] for b in range(3)]
    while check(square):
        square = [[0 for c in range(3)] for b in range(3)]
        sm = random.randint(1,hard)
        form = ["12","33","21","31","22","13","23","11","32"]
        for seq in form:
            y = int(seq[0])-1
            x = int(seq[1])-1
            square[y][x] = sm
            sm += 1
        adf = copy.deepcopy(square)
        for cac in range(gone):
            x = random.randint(0,2)
            y = random.randint(0,2)
            while square[y][x] == "?":
                x = random.randint(0,2)
                y = random.randint(0,2)
            square[y][x] = "?"

    print("Example '2,3,4' - replaces the number at second row third colomun with the number 4")
    while True:
        for x in square:
            row = ""
            for y in x:
                row += str(y) + " "
            print(row)
        if square == adf:
            print("Victory")
            print("You solved the firewall.")
            return True
        pos = input("Enter coordinates(row,colomun,number to replace with) 'c' to cancel: ")
        if pos == "c":
            print("Bypass canceled.")
            return False
        ps = pos.split(",")
        row = int(ps[0])-1
        col = int(ps[1])-1
        num = int(ps[2])
        del square[row][col]
        square[row].insert(col,num)

        
def catch(charge):
    c = Bitcoin.users[me.ip]
    c.balance -= charge
    print("You were caught hacking and were charged with {}$".format(charge))

def bit_guess(attempts,search,tp):
    put = False
    print("It is one of those: ")
    ch = 60
    for x in range(2):
        if(chance(ch)):
            c = bit_gen(len(search),len(search))
            print(c[tp])
        else:
            if not(put):
                put = True
                ch = 100
                print(search)
            else:
                c = bit_gen(len(search),len(search))
                print(c[tp])
    if put:
        c = bit_gen(len(search),len(search))
        print(c[tp])
    else:
        put = True
        print(search)
    username = ""
    while username != search and attempts > 0:
        username = input("{}: ".format(tp))
        if username != search:
            print("Wrong " + tp)
            print("Try again.")
            attempts -= 1
        else:
            print("Good job you guessed it it was " + search)
            return True
    if attempts == 0:
        print("The " + tp + " got reset, you ran out of attempts")
        return False
            
    
def rand_ip():
    ip = ""
    for x in range(0,4):
        ip += str(random.randint(1,255)) + "."
    return ip[:-1]

def rand_map():
    ips = random.randint(1,random.randint(1,7))
    if len(PC.all_pc) < ips:
        ips = len(PC.all_pc)
    maps = []
    for x in range(0,ips):
        while True:
            ip = PC.all_pc[random.randint(0,len(PC.all_pc)-1)].ip
            if not(ip in maps):
                maps.append(ip)
                break
    return maps

def chance(chance):
    num = random.randint(1,100)
    return num in range(1,chance+1)

def ratio(n1,n2,n3):
    return int((n2*n3)/n1)

def bit_gen(user_max,pass_max):
    chart = "0123456789qwertyuiopasdfghjklzxcvbnm"
    credit = {"username":"","password":""}
    users = []
    passes = []
    if len(Bitcoin.users) > 0:
        for x in Bitcoin.users.keys():
            x = Bitcoin.users[x]
            users.append(x.user)
            passes.append(x.password)
    for x in range(0,user_max):
        credit['username'] += chart[random.randint(0,len(chart)-1)]
    for y in range(0,pass_max):
        credit['password'] += chart[random.randint(0,len(chart)-1)]
    while (credit['username'] in users and credit['password'] in passes) and users != []:
        credit = {"username":"","password":""}
        for x in range(0,user_max):
            credit['username'] += chart[random.randint(0,len(chart)-1)]
        for y in range(0,pass_max):
            credit['password'] += chart[random.randint(0,len(chart)-1)]
    return credit
def no(number):
    if number < 0:
        return 1
    return number
def nope(number):
    if number == 0:
        return 1
    return number
def access(ip,usr,passw):
    a = Bitcoin.users[ip]
    if a.user == usr and a.password == passw:
        return True
def give():
    hard = []
    if chance(60):
        hard.append("length_scan.exe")
    if chance(20):
        hard.append("attempts_analyzer.exe")
    if chance(30):
        hard.append("bitcoin_cracker.exe")
    if chance(30):
        hard.append("chain_spam.exe")
    if chance(10):
        hard.append("trojan.exe")
    if chance(15):
        hard.append("file_analyzer.exe")
    if chance(8):
        hard.append("balance_analyzer.exe")
    if chance(5):
         hard.append("log_deleter.exe")
    if chance(11):
        hard.append("proxy_disc.exe")
    if chance(2):
        hard.append("proxy_disable.exe")
    if chance(2):
        hard.append("pin_breaker.exe")
    if chance(15):
        hard.append("proxy_over.exe")
    if chance(5):
        hard.append("bit_access.exe")
    if chance(20):
        hard.append("fire_disc.exe")
    if chance(3):
        hard.append("firewall_disable.exe")
    return hard
def comp_gen():
    comps = []
    level = len(me.map) + 4
    for x in range(0,4):
        pins = []
        length = []
        for y in range(0,len(me.map)+2):
            if chance(60) and len(pins) < 3:
                pins.append(random.randint(no(20-level),20))
                ln = random.randint(1,ratio(11,5,level))
                if ln > 4:
                    ln == 4
                length.append(ln)
        comps.append(PC(give(),False,"root"))
        maps = rand_map()
        comps[-1].pins = pins
        comps[-1].len = length
        comps[-1].map = maps
        if level >= 6 and chance(40):
            comps[-1].proxy = True
            comps[-1].overload = random.randint(1,random.randint(1,level-2))
            comps[-1].coms = random.randint(comps[-1].overload+3,(comps[-1].overload+10))
        if level >= 6 and chance(30):
            comps[-1].firewall = True
        balance = random.randint(0,ratio(9,1000,level-2))
        credit = bit_gen(random.randint(4,level+4),random.randint(4,level+4))
        Bitcoin.users[comps[-1].ip] = Bitcoin(credit['username'],credit['password'],balance)
    PC.all_pc += comps
    return comps
def search(ip):
    if ip == me.ip:
        return me
    for comp in PC.all_pc:
        if ip == comp.ip:
            return comp
    return False
class Instance:
    i = 0
class PC:
    all_pc = []
    def __init__(self,harddrive,my,bash):
        self.harddrive = harddrive
        self.ip = rand_ip()
        self.shell = False
        self.tut = False
        self.hacked = False
        self.spam = False
        self.len = []
        self.pins = []
        self.proxy = False
        self.overload = 0
        self.coms = 0
        self.attempts = 0
        self.part = 0
        self.asleep = False
        self.firewall = False
        self.accessed = False
        self.trojan = False
        self.see = False
        self.notes = ""
        self.map = []
        self.my = my
        self.logs = ""
        self.help = "'(q)uit to exit the game'\n(s)ave to save the game'\n'access [username] [password] to access bitcoin account(unlocks commands 'b' and 'trans [money_amount]')'\n'trans [money_amount]' to transfer money when accessed account\n'exit' to return to localhost\n'shop' to purchase programs\n'shell' to open shell on target 'help shell' for more info\n'proxy' to disable proxy\n'dis' to return to previous computer\n'ls' - to list files in harddrive\n'(b)alance' to see your balance\n'(l)ogs' - to see logfile\n'(f)ind' to search for computers to hack\n'(m)ap' to see hacked computers and access them\n'(g)et [file]' to download file\n'(h)elp <program(optional)>' to display help or help with a specific program\n'notes' to add notes"
        self.bash = bash + "> "
    def execute(self,command):
        global spam
        global last_ip
        global over
        command = command.split(" ")
        if command[0] == "admin":
            self.harddrive.append("attempts_analyzer.exe")
            self.harddrive.append("bitcoin_cracker.exe")
            self.harddrive.append("chain_spam.exe")
            self.harddrive.append("trojan.exe")
            self.harddrive.append("file_analyzer.exe")
            self.harddrive.append("balance_analyzer.exe")
            self.harddrive.append("log_deleter.exe")
            self.harddrive.append("proxy_disc.exe")
            self.harddrive.append("pin_breaker.exe")
            self.harddrive.append("bit_access.exe")
            self.harddrive.append("fire_disc.exe")
            self.see = True
            print("Welcome dev!!")
        elif command[0] == "money":
            Bitcoin.users[self.ip].balance += 100000
            print("Money added.")
        elif command[0] == "ls" or command[0] == "dir":
            if self.harddrive == []:
                print("No files")
            else:
                for x in list(enumerate(self.harddrive,start=1)):
                    print("{}. {}".format(x[0],x[1]))
        elif command[0] == "tut":
            self.tut = True
        elif command[0][0] == "b" and self.my:
            print("You have " + str(Bitcoin.users[self.ip].balance) + "$")
            if self.tut and self.part == 2:
                self.part += 1
                print("So you can't really get any good software from the shop huh?")
                print("Alright now check if you have hacked anybody with '(m)ap'")
        elif command[0][0] == "l":
            if self.logs == "":
                print("Logfile empty.")
            else:
                print(self.logs)
        elif command[0] == "exit":
            Instance.i = 0
            last_ip = []
            log = self.logs
            log = log.split("\n")[:-1]
            for x in log:
                ch = re.search(r"Connected",x)
                if ch != None:
                    if chance(5+ratio(6,3,len(me.map))):
                        catch(300)
                elif re.search(r"downloaded",x) != None:
                    if chance(10+ratio(6,3,len(me.map))):
                        catch(300)
                elif re.search(r"found bitcoin password",x) != None:
                    if chance(30+ratio(6,3,len(me.map))):
                        catch(200)
                elif re.search(r"found bitcoin username",x) != None:
                    if chance(20+ratio(6,3,len(me.map))):
                        catch(200)
                elif re.search(r"logged in.",x) != None:
                    if chance(10+ratio(6,3,len(me.map))):
                        catch(300)
                elif re.search(r"transfered",x) != None:
                    a = x.split(" ")
                    tr = int(a[2])
                    if chance(10+int(((tr*5)/100))+ratio(6,3,len(me.map))):
                        catch(int((tr*30)/100))
            print("Disconected")
        elif command[0] == "notes":
            if self.my:
                print(self.notes)
                choice = input("'e' to edit notes 'c' to exit: ")
                if choice == "e":
                    print(self.notes)
                    text = input()
                    self.notes += text + "\n"
                    print("Notes edited")
            else:
                print(me.notes)
                choice = input("'e' to edit notes 'c' to exit")
                if choice == "e":
                    print(me.notes)
                    text = input()
                    me.notes += text
                    print("Notes edited")
        elif command[0][0] == "f":
            comps = comp_gen()
            if self.tut and self.part == 12:
                self.part += 1
                comps = []
                comps.append(PC(give(),False,"root"))
                comps[-1].proxy = True
                comps[-1].firewall = True
                comps[-1].overload = 1
                comps[-1].coms = 10
                comps[-1].pins = [15,15]
                comps[-1].len = [2,3]
                PC.all_pc.append(comps[-1])
                level = len(self.map) + 4
                credit = bit_gen(random.randint(4,level+4),random.randint(4,level+4))
                Bitcoin.users[comps[-1].ip] = Bitcoin(credit['username'],credit['password'],669)
                print("Connect to this.")
            for comp in list(enumerate(comps,start=1)):
                money = ""
                files = ""
                see = ""
                fs = ""
                if "file_analyzer.exe" in self.harddrive:
                    files = "files: " + str(len(comp[1].harddrive))
                if "balance_analyzer.exe" in self.harddrive and not(self.tut):
                    money = "balance: " + str(Bitcoin.users[comp[1].ip].balance)
                if self.see or "proxy_disc.exe" in self.harddrive:
                    see = "Proxy: " + str(comp[1].proxy)
                if self.see or "fire_disc.exe" in self.harddrive:
                    fs = "Firewall: " + str(comp[1].firewall)
                print("{}. {} {} {} {} {}".format(comp[0],comp[1].ip,files,money,see,fs))
            if self.tut and self.part == 4:
                self.part += 1
                print("Each use of (f)ind will give you 4 random computers on the network\nSo select one and let the fun begin.")
            choice = input("Enter number of computer to hack or 'c' to cancel: ")
            if choice != "c":
                comp = comps[int(choice)-1].ip
                comp = search(comp)
                while comp.proxy:
                    if "proxy_over.exe" in self.harddrive:
                        print("The computer nedds {} shells to be overloaded".format(comp.overload))
                    print("""                                                     
                The computer is protected with a proxy                                        
                         .......                                          
                       ...     .\                                         
           ------------.        / Connected.                                        
          |            |         ********                                 
          |            |         *PROXY *.........\ 00000000000000        
          |            |         *ACTIVE*         / 0  TARGET    0        
          |   YOU      |         *      *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
           ------------          ********           00000000000000        
                                                                          
""")
                    print("Overload it by opening shells on other targets")
                    if self.tut and self.part == 13:
                        self.part += 1
                        print("Pretty self-explanatory you will bypass the firewall if you have enough shells opened\nThere are some programs that will help you to see the max of the proxy")
                    use = input("'b' to try to bypass, 'c' - to cancel: ")
                    if "proxy_disable.exe" in self.harddrive:
                        comp.proxy = False
                        print("Disabled proxy via proxy_disable.exe")
                    if use != "c":
                        if over >= comp.overload:
                            print("""                                                     
                The computer is protected with a proxy                                        
                         .......                                          
                       ...     .\                                         
           ------------.        /                                       
          |            |         ********             Connected.                   
          |            |         *PROXY *.........\ 00000000000000        
          |            |         *RESTA-*         / 0  TARGET    0        
          |   YOU      |         *RTING *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
           ------------          ********           00000000000000        
                                                                          
""")
                            print("Proxy bypassed with {}/{} max shells".format(over,comp.overload))
                            comp.proxy = False
                            comp.asleep = True
                        elif comp.proxy:
                            print("Failed to bypass proxy.")
                            print("Disconnected.")
                            break
                        if not(comp.proxy):
                            while comp.asleep:
                                print("You have {} commands remaining before proxy restarts".format(comp.coms))
                                if self.tut and self.part == 14:
                                    self.part += 1
                                    print("The proxy server is temporaly down you can disable it by using 'proxy' command")
                                use = input(comp.bash)
                                if comp.coms > 0:
                                    comp.execute(use)
                                    comp.coms -= 1
                                else:
                                    print("Proxy restarted")
                                    comp.proxy = True
                                    comp.asleep = False
                                    break
                                
                    else:
                        print("Disconnected.")
                        break
                if not(comp.proxy):
                    if self.tut and self.part == 15:
                        self.part += 1
                        print("Well done now crack the pins and proceed")
                    print("The computer is protected with " + str(len(comp.pins)) + " pincodes")
                    pn = len(comp.pins)
                    if pn > 0:
                        if "length_scan.exe" in self.harddrive and len(comp.len) > 0:
                            print("The password is {} digits long".format(comp.len[0]))
                        if "attempts_analyzer.exe" in self.harddrive:
                            print("You have {} attempts".format(comp.pins[0]))
                        if self.tut and self.part == 5:
                            self.part += 1
                            print("Basicly try to guess the pin\nNext to each number that is close to the real one in that position you will see '#'\nNext to right number you will see '*'\nSo try to guess it")
                        
                    while len(comp.pins) > 0:
                        v = False
                        if "pin_breaker.exe" in self.harddrive:
                            v = True
                        if pin(comp.pins[0],comp.len[0],v):
                            print("Good Job")
                            pn -= 1
                            del comp.pins[0]
                            del comp.len[0]
                            print(str(pn) + " more pins remaining")
                            if "length_scan.exe" in self.harddrive and pn > 0:
                                print("The password is {} digits long".format(comp.len[0]))
                        else:
                            print("The pin got reset")
                            break
                    if len(comp.pins) == 0:
                        self.logs += "Connected to {}\n".format(comp.ip)
                        self.map.append(comp.ip)
                        print("You hacked the computer.")
                        if comp.firewall:
                            print("""
                      The computer has a active Firewall.
                      
                                  Connected                                           
     --------------               +^^^^^^^^+          00000000000000000      
    |              |              |]]]]]]]]|          0   TARGET      0      
    |              |              |        |          0               0      
    |              |.............\|        |          0               0      
    |  LOCALHOST   |............./|FIREWALL|.........\0               0      
    |              |              | ACTIVE |         /0               0      
    |              |              |        |          0               0      
    |              |              |        |          0               0      
    |              |              |]]]]]]]]|          0               0      
    |              |              +^^^^^^^^+          0               0      
     --------------                                   00000000000000000      
                                                                          
""")
                            print("Firewalls are the last layer of protection")
                            print("Solve the magic square to proceed")
                            if self.tut and self.part == 16:
                                self.part += 1
                                print("To solve this the 3 numbers from each row,colomun and diagonal should have the same sum.")
                            if "firewall_disable.exe" in self.harddrive or magic_square(random.randint(1,4),nope(ratio(6,4,len(self.map)))):
                                if "firewall_disable.exe" in self.harddrive:
                                    print("Firewall disabled via firewall_disable.exe")
                                print("""
                         The computer has an inactive Firewall.
                         
                                                         Connected.                
     --------------               +^^^^^^^^+          00000000000000000      
    |              |              |]]]]]]]]|          0   TARGET      0      
    |              |              |        |          0               0      
    |              |.............\|        |          0               0      
    |  LOCALHOST   |             /|FIREWALL|.........\0               0      
    |              |              |DISABLED|........./0               0      
    |              |              |        |          0               0      
    |              |              |        |          0               0      
    |              |              |]]]]]]]]|          0               0      
    |              |              +^^^^^^^^+          0               0      
     --------------                                   00000000000000000      
                                                                          
""")
                                print("FIREWALL DISABLED")
                                comp.firewall = False
                                if self.tut and self.part == 17:
                                    print("Good work you completed the tutorial now i will let you play alone")
                                    Bitcoin.users[self.ip].balance = 0
                                    self.harddrive.remove("bitcoin_cracker.exe")
                                    self.tut = False
                                    self.part = 0
                        if not(comp.firewall):        
                            if "chain_spam.exe" in self.harddrive:
                                Bitcoin.users[self.ip].balance += spam*50
                            last_ip = []
                            last_ip.append(self.ip)
                            if self.tut and self.part == 6:
                                comp.part = 6
                                comp.tut = True
                            Instance.i = comp.ip
                            
                        
        elif command[0] == "shop":
            if self.tut and self.part == 1:
                self.part += 1
                print("Good job.")
                print("You can buy and sell programs from here")
                print("You can learn what each program does by using 'help [program_name]'")
                print("Now exit the shop and check your balance.")
            prices = {"firewall_disable.exe":3450,"fire_disc.exe":700,"bit_access.exe":3000,"proxy_over.exe":2300,"length_scan.exe":10,"attempts_analyzer.exe":200,"bitcoin_cracker.exe":500,"chain_spam.exe":700,"trojan.exe":1220,"file_analyzer.exe":150,"balance_analyzer.exe":1000,"log_deleter.exe":1500,"proxy_disc.exe":1080,"proxy_disable.exe":2000,"pin_breaker.exe":4000}
            inc = ratio(4,100,len(self.map))
            for x in prices.keys():
                prices[x] += int(inc)
            acc = Bitcoin.users[self.ip]
            what = ""
            while what != "e":
                what = input("(b)uy or (s)ell 'e' to exit?: ")
                if what[0] == "b":
                    print("You have {}$".format(acc.balance))
                    for x in enumerate(prices.keys(),start=1):
                        print("{}. {} : {}$".format(x[0],x[1],prices[x[1]]))
                    buy = input("Type program number to purchase 'e' to exit: ")
                    if buy != "e":
                        prog = list(prices.keys())[int(buy)-1]
                        price = prices[prog]
                        confirm = input("Are you sure you want to purchase {} y/n: ".format(prog))
                        if confirm == "y":
                            if acc.balance >= price:
                                acc.balance -= price
                                self.harddrive.append(prog)
                                print("Purchase completed")
                            else:
                                print("You need {} more $".format(price-acc.balance))
                        else:
                            print("Purchase canceled.")
                if what[0] == "s":
                    print("You have {}$".format(acc.balance))
                    print("Available programs for you to sell.")
                    for x in enumerate(self.harddrive,start=1):
                        print("{}. {} : {}$".format(x[0],x[1], prices[x[1]]))
                    sell = input("Type program number 'e' to exit: ")
                    if sell != "e":
                        prog = self.harddrive[int(sell)-1]
                        confirm = input("Are you sure you want to sell {} y/n: ".format(prog))
                        if confirm == "y":
                            del self.harddrive[int(sell)-1]
                            acc.balance += prices[prog]
                        else:
                            print("Selling canceled.")
                            print("Now you have {}$".format(acc.balance))
        elif command[0] == "shell":
            if not(self.my):
                if not(self.shell):
                    self.shell = True
                    over += 1
                    print("Shell opened.")
                    if self.tut and self.part == 10:
                        self.part += 1
                        print("They are used to overload proxy's\nIf you have more shells than the proxy max\nYou overload it.")
                        print("Disconnect when ready.")
                        self.logs = ""
                else:
                    print("Shell already opened on this system.")
            else:
                print("You can't open shell on your system")
                print("You have opened " + str(over) + " shells.")
        elif command[0][0] == "m":
            if len(self.map) == 0:
                print("No computers hacked")
                if self.tut and self.part == 3:
                    self.part += 1
                    print("OK,ok, i will tell you how to hack other computers")
                    print("Just search for them first, lol")
                    print("Use 'help' if you don't know what i mean")
            else:
                print("Those are the computers you already hacked.")
                for x in list(enumerate(self.map,start=1)):
                    comp = x[1]
                    money = ""
                    see = ""
                    shell = "Shell: "
                    fire = ""
                    if search(comp).shell:
                        shell += "Opened"
                    else:
                        shell += "Closed"
                    if (self.my and (self.see or "fire_disc.exe" in self.harddrive)) or (not(self.my) and "fire_disc.exe" in me.harddrive):
                        fire = "Firewall: " + str(search(comp).firewall)
                    if (self.my and (self.see or "proxy_disc.exe" in self.harddrive)) or (not(self.my) and "proxy_disc.exe" in me.harddrive):
                        see = "Proxy: " + str(search(comp).proxy)
                    if "balance_analyzer.exe" in self.harddrive or search(comp).accessed or "balance_analyzer.exe" in me.harddrive:
                        money = "Balance: " + str(Bitcoin.users[comp].balance)
                    print("{}. {} files: {} {} {} {} {}".format(x[0],comp,len(search(comp).harddrive),money,see,shell,fire))
                chose = input("Type computer number to access it and 'e' to exit: ")
                if chose != "e":
                    last_ip.append(self.ip)
                    Instance.i = self.map[int(chose)-1]
        elif command[0] == "proxy" and not(self.my):
            if self.asleep:
                ln = random.randint(1,2)
                att = random.randint(4,9)
                v = False
                if "pin_breaker.exe" in me.harddrive:
                    v = True
                if "length_scan.exe" in me.harddrive:
                    print("The password is {} digits long".format(ln))
                if "attempts_analyzer.exe" in me.harddrive:
                    print("You have {} attempts".format(att))
                if pin(att,ln,v):
                   print("""                                                     
                       The computer's proxy is disabled                                        
                                                                   
                                                                     
           ------------                                              
          |            |         ********             Connected.                   
          |            |........\*PROXY *.........\ 00000000000000        
          |            |        /*      *........./ 0  TARGET    0        
          |   YOU      |         *DISAB-*           0            0        
          |            |         *LED   *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
          |            |         *      *           0            0        
           ------------          ********           00000000000000        
                                                                          
""")
                   self.asleep = False
                   self.proxy = False
                   print("PROXY DISABLE")
        elif command[0][0] == "g" and not(self.my):
            file = command[1]
            if file in self.harddrive:
                me.harddrive.append(file)
                self.harddrive.remove(file)
                print(file + " successfully downloaded.")
                self.logs += me.ip + " downloaded " + file + "\n"
            elif not(file in self.harddrive):
                print("File " + file + " does not exist.")
                
        elif command[0] == "help":
            cm = command
            if self.tut and self.part == 0:
                self.part += 1
                print("You can use help on all programs and comands to see additional info")
                print("Let's try entering in the shop. Type 'shop'")
            if len(cm) == 2:
                file = cm[1]
                if file == "length_scan.exe":
                    print("The program automatically determines the lenght of the pin")
                elif file == "attempts_analyzer.exe":
                    print("The program automatically determines the max attempts of the pin")
                elif file == "bitcoin_cracker.exe":
                    print("You can use it in other systems by running the command 'bit' to hack bitcoin accounts use 'help bit' for more info")
                elif file == "file_analyzer.exe":
                    print("The program shows the amount of files on each system when using the '(f)ind' command")
                elif file == "chain_spam.exe":
                    print("Install this on other systems by using 'spam' command to generate money each time you hack a computer use 'help spam' for more info")
                elif file == "trojan.exe":
                    print("use command 'bit_pas' to install trojan on other systems and instantly find their bitcoin password")
                elif file == "balance_analyzer.exe":
                    print("Use '(b)alance' on other systems to see thir balance even if you haven't hacked their bitcoin account\nalso shows balance when using '(f)ind'")
                elif file == "bit":
                    print("Use command on other computers to try to find their username and password then use 'access [username] [password]' to access in their account, 'trans [amount]' to transfer money from their account,'(b)alance' to get their balance")
                elif file == "spam":
                    print("Use 'spam' to install spam on other systems the more systems that you install spam to the more money you will get per hack.")
                elif file == "log_deleter.exe":
                    print("Use 'del' to clear logs on system")
                elif file == "proxy_disc.exe":
                    print("Shows if there is active Proxy by using '(f)ind' or '(m)ap'")
                elif file == "proxy_disable.exe":
                    print("Can bypass and immediately disable any proxy")
                elif file == "shell":
                    print("Use it on other systems to open shells which are then used in overloading proxys")
                elif file == "shop":
                    print("Use to purchase programs from the shop in exchange for bitcoins 'b' to check balance")
                elif file == "pin_breaker.exe":
                    print("Shows all numbers from a pin except the last one.")
                elif file == "proxy_over.exe":
                    print("Show the amount of shells you need to overload a proxy.")
                elif file == "bit_access.exe":
                    print("Directly accesses bitcoin accounts when you run 'bit'")
                elif file == "fire_disc.exe":
                    print("Shows firewall state on '(f)ind' and '(m)ap'")
                elif file == "firewall_disable.exe":
                    print("Directly disables firewall.")
            else:
                print(self.help)

        elif (command[0] == "bit_pas" and not(self.my)) and "trojan.exe" in me.harddrive:
            self.trojan = True
            print("Got password use 'bit' to hack the username and see the password.")

        elif (command[0] == "bit" and not(self.my)) and "bitcoin_cracker.exe" in me.harddrive:
            user = Bitcoin.users[self.ip].user
            password = Bitcoin.users[self.ip].password
            if "bit_access.exe" in me.harddrive:
                self.execute("access {} {}".format(user,password))
                print("Account accessed with bit_access.exe. You can now exit.")
            if self.trojan:
                print("The password is " + password)
            if self.tut and self.part == 7:
                self.part += 1
                print("Ok whatever you select the method is identical\nYou will get 4 usernames/passwords one of them is the real one\nYou have two attempts after that the username/password resets\nBut you can still try to crack it again\nAfter you got the user and pass use 'access [username] [password]'")
                print("Also remember that you can use 'notes' to write down important info.")
            choice = input("Type 'u' to start hacking the username 'p' to start with the password and 'c' to cancel: ")
            if choice == "u":
                if not(bit_guess(2,user,"username")):
                    c = bit_gen(len(user),len(password))
                    Bitcoin.users[self.ip].user = c['username']
                else:
                    self.logs += me.ip + " found bitcoin username\n"
            elif choice == "p":
                if not(bit_guess(2,password,"password")):
                    c = bit_gen(len(user),len(password))
                    Bitcoin.users[self.ip].password = c['password']
                else:
                    self.logs += me.ip + " found bitcoin password\n"
        elif command[0] == "access" and not(self.my):
            user = command[1]
            password = command[2]
            if access(self.ip,user,password):
                self.accessed = True
                print("Successfully logged in.")
                self.logs += me.ip + " logged in.\n"
                if self.tut and self.part == 8:
                    self.part += 1
                    print("Ok now you can use the commands '(b)alance' and 'trans [money_amount]' here\nI say let's get some cash, man")
            else:
                print("Wrong username/password.")
        elif command[0][0] == "b" and not(self.my):
            if self.accessed or "balance_analyzer.exe" in me.harddrive:
                print("Balance: " + str(Bitcoin.users[self.ip].balance))
            else:
                print("First log in your account using access [username] [password]")
        elif command[0] == "trans" and not(self.my):
            amount = int(command[1])
            user = Bitcoin.users[self.ip]
            if self.accessed:
                if user.balance >= amount:
                    user.balance -= amount
                    Bitcoin.users[me.ip].balance += amount
                    print("Transfer successfull.")
                    self.logs += me.ip + " transfered " + str(amount) + " from account.\n"
                    if self.tut and self.part == 9:
                        self.part += 1
                        print("Awesome but becareful with the logs though.")
                        print("Now install a shell.")
            else:
                print("First log in your account using access [username] [password]")
        elif command[0] == "dis" and not(self.my):
            Instance.i = last_ip[-1]
            del last_ip[-1]
            print("Disconnected.")
            log = self.logs
            log = log.split("\n")[:-1]
            for x in log:
                ch = re.search(r"Connected",x)
                if ch != None:
                    if chance(5+ratio(6,3,len(me.map))):
                        catch(300)
                elif re.search(r"downloaded",x) != None:
                    if chance(10+ratio(6,3,len(me.map))):
                        catch(300)
                elif re.search(r"found bitcoin password",x) != None:
                    if chance(30+ratio(6,3,len(me.map))):
                        catch(200)
                elif re.search(r"found bitcoin username",x) != None:
                    if chance(20+ratio(6,3,len(me.map))):
                        catch(200)
                elif re.search(r"logged in.",x) != None:
                    if chance(10+ratio(6,3,len(me.map))):
                        catch(300)
                elif re.search(r"transfered",x) != None:
                    a = x.split(" ")
                    tr = int(a[2])
                    if chance(10+int(((tr*5)/100))+ratio(6,3,len(me.map))):
                        catch(int((tr*30)/100))
            if self.tut and self.part == 11:
                self.part += 1
                me.part = self.part
                self.tut = False
                self.part = 0
                print("If you check now your balance you should have the money :D.\nAlright now use '(f)ind' again to see the other two ways of defence you will encounter")
        elif command[0] == "spam" and not(self.my) and "chain_spam.exe" in me.harddrive:
            if not(self.spam):
                spam += 1
                self.spam = True
                print("Spam installed")
            else:
                print("Already installed spam.")
        elif command[0] == "del" and ("log_deleter.exe" in self.harddrive or "log_deleter.exe" in me.harddrive):
            self.logs = ""
            print("Logs deleted.")
        elif command[0][0] == "q":
            print("Warning any unsaved progress will be lost(use '(s)ave' to save)")
            end = input("Do you really want to exit y/n?: ")
            if end == "y":
                exit()
        elif command[0][0] == "s":
            print("Saving...")
            delete()
            dat = {}
            dat["Player"] = {}
            dat["Player"]["harddrive"] = self.harddrive
            dat["Player"]["map"] = self.map
            dat["Player"]["bash"] = self.bash[:-2]
            dat["Player"]["ip"] = self.ip
            dat["Player"]["balance"] = Bitcoin.users[self.ip].balance
            dat["Player"]["spam"] = spam
            dat["Player"]["over"] = over
            dat["Player"]["my"] = True
            for x in PC.all_pc:
                ip = x.ip
                dat[ip] = {}
                dat[ip]["harddrive"] = x.harddrive
                dat[ip]["map"] = x.map
                dat[ip]["bash"] = x.bash
                dat[ip]["my"] = False
                dat[ip]["balance"] = Bitcoin.users[ip].balance
                dat[ip]["firewall"] = x.firewall
                dat[ip]["proxy"] = x.proxy
                dat[ip]["shell"] = x.shell
                dat[ip]["spam"] = x.spam
                dat[ip]["len"] = x.len
                dat[ip]["pins"] = x.pins
                dat[ip]["overload"] = x.overload
                dat[ip]["coms"] = x.coms
                dat[ip]["attempts"] = x.attempts
                dat[ip]["accessed"] = x.accessed
                dat[ip]["trojan"] = x.trojan
                dat[ip]["ip"] = ip
            f = open("db.txt","w")
            f.write(str(dat))
            f.close()
        else:
            print("Unrecognized command.")
class Bitcoin:
    users = {}
    def __init__(self,username,password,balance):
        self.user = username
        self.password = password
        self.balance = balance
if exists():
    ch = input("Do you want to load previous save y/n?: ")
    if ch == "n":
        ch = input("Warning! Starting a new game will delete all your progress y/n?: ")
        if ch == "y":
            ch = "n"
    if ch == "y":
        pl = get("Player")
        me = PC(pl["harddrive"],True,pl["bash"])
        me.map = pl["map"]
        me.ip = pl["ip"]
        Bitcoin.users[me.ip] = Bitcoin(me.bash,bit_gen(6,8)['password'],pl["balance"])
        c = get()
        for x in c.keys():
            if x != "Player":
                x = get(x)
                level = len(me.map) + 4
                cmp = PC(x["harddrive"],False,"root")
                cmp.map = x["map"]
                cmp.ip = x["ip"]
                credit = bit_gen(random.randint(4,level+4),random.randint(4,level+4))
                Bitcoin.users[cmp.ip] = Bitcoin(credit['username'],credit['password'],x["balance"])
                cmp.firewall = x["firewall"]
                cmp.proxy = x["proxy"]
                cmp.shell = x["shell"]
                cmp.spam = x["spam"]
                cmp.len = x["len"]
                cmp.pins = x["pins"]
                cmp.overload = x["overload"]
                cmp.coms = x["coms"]
                cmp.attempts = x["attempts"]
                cmp.accessed = x["accessed"]
                cmp.trojan = x["trojan"]
                PC.all_pc.append(cmp)
                
    else:
        delete()
        print("Starting new game...")
        bash = input("Enter your name: ")
        print("Type 'help' to see commands and 'tut' for tutorial.")
        me = PC(["length_scan.exe"],True, bash)
        Bitcoin.users[me.ip] = Bitcoin(bash,bit_gen(6,8)['password'],0)
else:
    bash = input("Enter your name: ")
    print("Type 'help' to see commands and 'tut' for tutorial.")
    me = PC(["length_scan.exe"],True, bash)
    Bitcoin.users[me.ip] = Bitcoin(bash,bit_gen(6,8)['password'],0)
while True:
    i = Instance.i
    if i == 0:
        if me.tut and me.part == 0:
            print("Welcome to run4hackz type 'help' to begin")
        me.execute(input(me.bash))
    else:
        x = search(i)
        if x.tut and x.part == 6:
            x.part += 1
            print("It was'n that hard, was it?")
            print("Anyways now once you hacked this you can do a lot")
            print("Like using 'g' to get files, install spam, look at the computer map(Type '(m)ap') to connect to other computers\nOr you can hack his bitcoin account\nIntressted? Ok let's do that\nI have installed the 'bitcoin_cracker.exe' to your computer")
            print("Remember about the 'help [program_name]'")
            me.harddrive.append("bitcoin_cracker.exe")
        x.execute(input(x.bash))
