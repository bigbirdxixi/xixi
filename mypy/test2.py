import sys

Zero = [" * * * ",
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        " * * * ",]

One = ["   *   ",
       "  **   ",
       " * *   ",
       "   *   ",
       "   *   ",
       "   *   ",
       " * * * "]

Two = [" * * * ",
       "*     *",
       "*     *",
       "    *  ",
       "  *    ",
       "*      ",
       "* * * *"]

Three = ["* * * *",
         "      *",
         "      *",
         "* * * *",
         "      *",
         "      *",
         "* * * *"]

Four = ["    *  ",
        "   **  ",
        "  * *  ",
        " *  *  ",
        "* * * *",
        "    *  ",
        "    *  "]

Five = ["* * * *",
        "*      ",
        "*      ",
        "* * * *",
        "      *",
        "      *",
        "* * * *"]

Six = ["    *  ",
       "   *   ",
       "  *    ",
       " *     ",
       "* * * *",
       "*     *",
       "* * * *"]

Seven = ["* * * *",
         "      *",
         "     * ",
         "    *  ",
         "   *   ",
         "  *    ",
         " *     "]

Eight = ["* * * *",
         "*     *",
         "*     *",
         "* * * *",
         "*     *",
         "*     *",
         "* * * *"]

Nine = ["* * * *",
        "*     *",
        "*     *",
        "* * * *",
        "      *",
        "      *",
        "* * * *"]

Digits = [Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]


try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
#            line += digit[row] + "  "
            cc = 0
            while cc < 7:
                if digit[row][cc] is not "*":
                    line += digit[row][cc]
                else:
                    line += str(number)
                cc +=1
            line += "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage:test2.py <number>")
except ValueError as err:
    print(err,"in",digits)
