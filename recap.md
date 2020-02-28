# TODO

* excel sheet parsen und stats
* grafiken -> ?
* cron: jeden tag um 9 arbeiten
* mails versenden



# project euler:
https://projecteuler.net/problem=1
1	Multiples of 3 and 5
2	Even Fibonacci numbers
4	Largest palindrome product
9	Special Pythagorean triplet


snippets:
https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b

snippets, etwas schwieriger:
https://medium.com/better-programming/20-python-snippets-you-should-learn-today-8328e26ff124
https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172



sudoku (advanced):
http://norvig.com/sudoku.html




### my snippets:

&nbsp;
```python
# nested function calls
def g(a):
    print(a - 1)
    return a + 1


def f(a):
    return g(a * 2)


def main():
    return f(3)

# behavior of:
a = main()
```
&nbsp;
```python
woods = ["eiche", "fichte", "erle"]
preferences = {"Leon": 0, "Anna": 2}

def get_preference(person):
    return woods[ preferences[person] ]

wood = get_preference("Anna")
```
