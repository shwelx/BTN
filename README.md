# Name to Binary convertor - სახელის ორობით სისტემაში გადამყვანი აპლიკაცია.

**for English scroll down.**
---
აღნიშნული აპლიკაცია არის საგანმანათლებლო ხასიათის გრაფიკული აპლიკაცია, რომელიც მომხმარებლის მიერ შეყვანილ ტექსტს ორობით სისტემაში გარდაქმნის და შესაბამისად მომხმარებელს შედეგად ორობით კოდს უბრუნებს. მისი მიზანია აჩვენოს, თუ როგორ იწერება სიმბოლოები კომპიუტერში ორობითი ფორმატით და გაამარტივოს კოდირების ძირითადი პრინციპების გაგება.

## მთავარი ფუნქციონალი

- [x] იღებს მომხმარებლის მიერ შეყვანილ სახელსა და არჩეულ ენას.
- [x] ამოწმებს შეყვანილ ტექსტს არჩეული ენის მიხედვით.
- [x] შეყვანილი ტექსტი გადაჰყავს ორობით სისტემაში (8-ბიტიანი Unicode მნიშვნელობები).
- [x] შედეგის ჩვენება.

## დამატებითი ფუნქციონალი & შეზღუდვა

- 💡 მიმდინარე დროის ჩვენება ორობით სისტემაში.
- 💡 მხოლოდ ქართული (მხედრული) ან ლათინური (ინგლისური) ასობგერების დაშვება არჩეული ენის შესაბამისად (დამატებით უშვებს space-ებს რათა გათვალისწინებული იყოს ისეთი სახელები რომლებიც შეიცავენ ერთზე მეტ სიტყვას).

## გამოყენებული ტექნოლოგია

- [**Python3**](https://www.python.org) - ობიექტზე ორიენტირებული პროგრამირება : ლოგიკური ნაწილისთვის.
- **Python3 ReGex** : შეყვანილი მონაცემების ვალიდაციისთვის.
- [**PyQt5**](https://pypi.org/project/PyQt5/) : გრაფიკული ინტერფეისისთვის.
- [**Qt Designer**](https://www.pythonguis.com/installation/install-qt-designer-standalone/) : UI დიზაინის შესაქმნელად.

## გამოყენება

### მოთხოვნები:

1. დაინსტალირებული გქონდეთ **Python3**
\
იმ შემთხვევაში თუ არ გაქვთ დაინსტალირებული, გადადით ოფიციალურ საიტზე და დააყენეთ Python 3-ის ვერსია თქვენი ოპერაციული სისტემის შესაბამისი ინსტალერით.

2. დაინსტალირებული გქონდეთ **PyQt5**
\
თუ არ გაქვთ დაყენებული, გახსენით ტერმინალი და ჩაწერეთ შემდეგი ბრძანება:
\
ლინუქსი/მაკი - `sudo pip3 install PyQt5`
\
ვინდოუსი - `pip install PyQt5`

### პროგრამის გაშვება

- გადმოწერეთ ZIP ფაილი და დააექსტრაქტეთ (extract), გახსენით ტერმინალი და გადადით ამავე დაესტრაქტებულ საქაღალდეში და დაწერეთ შემდეგი ბრძანება პროგრამის გასაშვებად: `python3 main.py`

ან

- გახსენით ტერმინალი თქვენს კომპიუტერში, შედით იმ საქაღალდეში, სადაც გსურთ პროექტის ჩამოტვირთვა. ამავე ადგილას დაწერეთ Git ბრძანება: `git clone https://github.com/borderlineping/BTN.git`, შემდეგ შედით პროექტის საქაღალდეში: `cd BTN` და გაუშვით პროგრამა: `python3 main.py`

### გატესტვა

პროგრამის გაშვების შემდეგ, თქვენ მომენტალურად დაინახავთ მიმდინარე დროს ორობით სისტემაში. აირჩიეთ სასურველი ენა და ჩაწერეთ თქვენი სახელი ტექსტის ველში. ღილაკზე დაწკაპების შემდეგ კი თქვენ იხილავთ შედეგს ორობითი კოდის სახით :))


---


# Name to Binary convertor.

**for Georgian scroll up.**
---
This application is an educational graphical application that converts the text entered by the user into the binary system and returns the resulting binary code to the user. Its purpose is to show how characters are written in binary format on a computer and to simplify the understanding of the basic principles of coding.

## The main functionality

- [x] accepts the name entered by the user and the language selected.
- [x] checks the input text based on the selected language.
- [x] converts the entered text into the binary system (8-bit Unicode values).
- [x] displays the result.

## Bonus Functionality & Limitation

- 💡 Current time display in binary system.
- 💡 Allow only Georgian (Mkhedruli) or Latin (English) characters depending on the selected language (additionally allows spaces to accommodate names that contain more than one word).

## Technology Used

- [**Python3**](https://www.python.org) - Object-Oriented Programming : for the logical part.
- **Python3 ReGex** : for validating input data.
- [**PyQt5**](https://pypi.org/project/PyQt5/) : for the graphical interface.
- [**Qt Designer**](https://www.pythonguis.com/installation/install-qt-designer-standalone/) : to create UI design.

## Usage

### Requirements:

1. Have **Python3** installed
\
If you don't have it installed, go to the official website and install the version of Python 3 using the installer appropriate for your operating system.

2. Have **PyQt5** installed
\
If you don't have it installed, open a terminal and type the following command:
\
Linux/Mac - `sudo pip3 install PyQt5`
\
Windows - `pip install PyQt5`

### Running the program

- Download the ZIP file and extract it, open a terminal and go to the same extracted folder and type the following command to run the program: `python3 main.py`

or

- Open a terminal on your computer, go to the folder where you want to download the project. In the same place, type the Git command: `git clone https://github.com/borderlineping/BTN.git`, then enter the project folder: `cd BTN` and run the program: `python3 main.py`

### Testing

After running the program, you will instantly see the current time in binary. Select your preferred language and enter your name in the text field. After clicking the button, you will see the result in binary code :))
