# Cotisation-manager

This script will be a tool to manage a contribution program
in some cases some people paid more or less so this tool can be used to balance obligations between members

## Installation
just download the cotisaionManager.py in your machine

## Usage
run the script
```bash
python cotisaionManager.py
```
and you well be invited to tape commands

```bash
===============================================
=
=    Welcome to contributions equilibrator
=    By Samir EL KHYATI
=
===============================================
equilibrator>
```

## Commad line
this script provides the following commands

>**addcontributor**
>```bash
>equilibrator>addcontributor name amount
>```
>result : the contributor will be added to the list of contributions

>**showcontributors**
>```bash
>equilibrator>showcontributors
>```
>result : the list of contributions will be displayed


>**total**
>```bash
>equilibrator>total
>```
>result : the total amount of contributions will be displayed


>**resolve**
>```bash
>equilibrator>resolve
>```
>result : the contributions will be equilabred and the program will the display for each person how much he must take or give


>**quit**
>```bash
>equilibrator>quit
>```
>result : the program will be closed


## Exemple
```bash
PS C:\Users\Samir EL KHYATI\Desktop\Cotisation Manager> python .\cotisaionManager.py
===============================================
=
=    Welcome to contributions equilibrator
=    By Samir EL KHYATI
=
===============================================
equilibrator>addcontributor samir 23
equilibrator>addcontributor alice 10
equilibrator>addcontributor bobe 5
equilibrator>addcontributor tony 35
equilibrator>total
> 73.0
equilibrator>showcontributors
> samir gives23.0
> alice gives10.0
> bobe gives5.0
> tony gives35.0
equilibrator>resolve
>Total price: 73.0
>Obligation: 18.25
>
>
> samir take 4.75
> alice give 8.25
> bobe give 13.25
> tony take 16.75
equilibrator>quit
PS C:\Users\Samir EL KHYATI\Desktop\Cotisation Manager>

```

## License
