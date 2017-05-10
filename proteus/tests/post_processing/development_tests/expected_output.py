import numpy as np

globalDOF2Element_test = [[0, 1], [0, 2, 3], [2], [1, 4, 5], 
                          [0, 1, 3, 4, 6, 7], [2, 3, 6], [5], [4, 5, 7], 
                          [6, 7], [0], [1], [0, 1], [2], [0, 3], [2, 3], 
                          [2], [1, 4], [5], [4, 5], [3, 6], [4, 7], [6, 7], 
                          [6], [5], [7]]

globalDOFGlobalElement2StarElement_test = [{0: 0, 1: 1}, {0: 0, 2: 1, 3: 2},
                                           {2: 0}, {1: 0, 4: 1, 5: 2}, 
                                           {0: 0, 1: 1, 3: 2, 4: 3, 6: 4, 7: 5}, 
                                           {2: 0, 3: 1, 6: 2}, {5: 0}, 
                                           {4: 0, 5: 1, 7: 2}, {6: 0, 7: 1}, 
                                           {0: 0}, {1: 0}, {0: 0, 1: 1}, 
                                           {2: 0}, {0: 0, 3: 1}, 
                                           {2: 0, 3: 1}, {2: 0}, 
                                           {1: 0, 4: 1}, {5: 0}, 
                                           {4: 0, 5: 1}, {3: 0, 6: 1}, 
                                           {4: 0, 7: 1}, {6: 0, 7: 1}, 
                                           {6: 0}, {5: 0}, {7: 0}]

dofStarElementsArray_cmp = np.array([[0, 0, 0, 0, 0, 0],
                                     [1, 0, 1, 0, 1, 0],
                                     [1, 0, 0, 0, 0, 0],
                                     [2, 2, 1, 0, 1, 1],
                                     [1, 0, 3, 0, 1, 0],
                                     [2, 0, 1, 0, 1, 0],
                                     [4, 0, 2, 0, 1, 0],
                                     [5, 2, 1, 0, 1, 1]])