"""
TODO: high level comment, author, and date
"""

import util

def main():

    opts = util.parse_args()
    train_partition = util.read_arff(opts.train_filename, True)
    test_partition  = util.read_arff(opts.test_filename, False)

    # TODO:create an instance of the DecisionTree class from the train_partition

    # TODO: print text representation of the DecisionTree

    # TODO: evaluate the decision tree on the test_partition

main()
