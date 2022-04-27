from base import Sequent

def contracted_view(sequent : Sequent, max_n : int):
    sequent = sequent.clone()

    for antecedent in sequent.antecedents.distinct_elements():
        if sequent.antecedents[antecedent] > max_n:
            sequent.antecedents[antecedent] = max_n

    for consequent in sequent.consequents.distinct_elements():
        if sequent.consequents[consequent] > max_n:
            sequent.consequents[consequent] = max_n

    return sequent