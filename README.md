# Ohce kata

The Ohce kata, a short and simple exercise to practice outside-in TDD using test doubles
by [@codesai](https://codesai.com/posts/2016/05/ohce-kata)


## Specs

1. When you start oche, it greets you differently depending on the current time, but only in Spanish:
    - Between 20 and 6 hours, ohce will greet you saying: ¡Buenas noches < your name >!
    - Between 6 and 12 hours, ohce will greet you saying: ¡Buenos días < your name >!
    - Between 12 and 20 hours, ohce will greet you saying: ¡Buenas tardes < your name >!
2. When you introduce a palindrome, ohce likes it and after reverse-echoing it, it adds ¡Bonita palabra!
3. ohce knows when to stop, you just have to write Stop! and it’ll answer Adios < your name > and end.

*Example:*
```bash
$ ohce Pedro
> ¡Buenos días Pedro!
$ hola
> aloh
$ oto
> oto
> ¡Bonita palabra!
$ stop
> pots
$ Stop!
> Adios Pedro
```

## Setup

1. Create a Python 3 virtual environment, e.g.:
```bash
mkvirtualenv -p /usr/bin/python3.10 ohce
```

2. Install dependencies, e.g.:
```bash
pip install -r requeriments.txt
```

## Execution
Use `make` to inspect available commands.