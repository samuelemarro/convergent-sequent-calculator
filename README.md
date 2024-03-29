# Convergent Sequent Calculator (CSC)
Python prover for [sequent calculus](https://en.wikipedia.org/wiki/Sequent_calculus).

## Features
- Support for modal logic
- Counter-example generator
- Loop checker

## Installing

### The philosopher's way

Download the executable from the [Release page](https://github.com/samuelemarro/convergent-sequent-calculator/releases).

### The programmer's way

```
git clone https://github.com/samuelemarro/convergent-sequent-calculator
pip install -r requirements.txt
```

## Syntax

Sequents are in the form `label1:FORMULA1[, label2:FORMULA2...] => label3:FORMULA3[, label4:FORMULA4...]` (for labelled formulas). Relations can be written as `label1Rlabel2`.

Variables must be single-letter and uppercase (e.g. `A`, `B`...).
Labels must be single-letter and lowercase (e.g. `a`, `b`...).

Allowed symbols:
* `AND` (alternatively `/\`);
* `OR` (alternatively `\/`);
* `NOT` (alternatively `~` or `-`);
* `IMPLIES` (alternatively `->`);
* `BOX` (alternatively `[]`);
* `DIAMOND` (alternatively `<>`);
* `BOT` (alternatively `+`);
* `R` (alternatively `SEES`) for relations.

Note that operators are right-associative.

### Examples

* ```w:A /\ B, w R w => w:B, w:C```
* ```w:[]A /\ B, w R w => w:B, w:C```
* ```w:A AND B, w:A -> B => w:A```
* ```w:DIAMOND A, u: BOX B => u:A```

## Usage

### Standard mode (for programmers)

```python main.py "SEQUENT HERE"```

(double quotes must be included).

### Interactive mode (for programmers)

```python interactive.py```

### Interactive mode (for philosophers)

Double click on the program.
