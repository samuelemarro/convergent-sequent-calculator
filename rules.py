from base import Atom, Sequent, LabelledFormula
from parsing import preprocess
from rule import Rule, ChildSequent, ExtraMultisetType


# Children:
# w:A, Γ ⇒ Δ
# w:B, Γ ⇒ Δ
# Root:
# w:(A ∧ B), Γ ⇒ Δ

INITIAL_SEQUENT_VARIABLE = Rule(
    'Initial variable',
    Sequent([LabelledFormula('w', 'A')], [LabelledFormula('w', 'A')]),
    []
)

INITIAL_SEQUENT_ATOM = Rule(
    'Initial atom',
    Sequent([Atom('w', 'u')], [Atom('w', 'u')]),
    []
)

L_BOT = Rule(
    'L⊥',
    Sequent([LabelledFormula('w', preprocess('BOT'))], []),
    []
)

L_AND = Rule(
    'L∧', 
    Sequent([LabelledFormula('w', preprocess('(A AND B)'))], []),
    [
        ChildSequent([LabelledFormula('w', preprocess('A')), LabelledFormula('w', preprocess('B'))], [], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
    ]
)

R_AND = Rule(
    'R∧',
    Sequent([], [LabelledFormula('w', preprocess('(A AND B)'))]),
    [
        ChildSequent([], [LabelledFormula('w', preprocess('A'))], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
        ChildSequent([], [LabelledFormula('w', preprocess('B'))], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA])
    ]
)

L_OR = Rule(
    'L∨',
    Sequent([LabelledFormula('w', preprocess('(A OR B)'))], []),
    [
        ChildSequent([LabelledFormula('w', preprocess('A'))], [], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
        ChildSequent([LabelledFormula('w', preprocess('B'))], [], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
    ]
)

R_OR = Rule(
    'R∨',
    Sequent([], [LabelledFormula('w', preprocess('(A OR B)'))]),
    [
        ChildSequent([], [LabelledFormula('w', preprocess('A')), LabelledFormula('w', preprocess('B'))], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
    ]
)

L_IMPLIES = Rule(
    'L→',
    Sequent([LabelledFormula('w', preprocess('(A IMPLIES B)'))], []),
    [
        ChildSequent([], [LabelledFormula('w', preprocess('A'))], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
        ChildSequent([LabelledFormula('w', preprocess('B'))], [], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
    ]
)
R_IMPLIES = Rule(
    'R→',
    Sequent([], [LabelledFormula('w', preprocess('(A IMPLIES B)'))]),
    [
        ChildSequent([LabelledFormula('w', preprocess('A'))], [LabelledFormula('w', preprocess('B'))], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA])
    ]
)

L_NOT = Rule(
    'L¬',
    Sequent([LabelledFormula('w', preprocess('(NOT A)'))], []),
    [
        ChildSequent([], [LabelledFormula('w', preprocess('A'))], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
    ]
)

R_NOT = Rule(
    'R¬',
    Sequent([], [LabelledFormula('w', preprocess('(NOT A)'))]),
    [
        ChildSequent([LabelledFormula('w', preprocess('A'))], [], [ExtraMultisetType.GAMMA], [ExtraMultisetType.DELTA]),
    ]
)

RULES = [
    INITIAL_SEQUENT_VARIABLE,
    INITIAL_SEQUENT_ATOM,
    L_BOT,
    L_AND,
    R_AND,
    L_OR,
    R_OR,
    L_IMPLIES,
    R_IMPLIES,
    L_NOT,
    R_NOT
]