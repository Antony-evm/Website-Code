import IPython.display
import sympy
import numpy as np


def make_boxed_tensor_latex(x, box_rows=True, index=0):
    ixs = "ijklmnopqrst"
    shape = x.shape
    # ensure has at least 2D
    if len(shape) == 1:
        x = x[None, :]

    rows, cols = x.shape[0:2]

    mat = []
    # always generate a matrix starting at the smallest index
    # e.g. a 2x2x3 tensor is a 2x2 matrix of 3 element arrays, not 2 rows of 2x3 matrices
    for row in range(rows):
        line = []
        for col in range(cols):
            if len(x.shape) == 2:
                line.append("\\quad \  \\llap{%d} \ \  \strut " % (x[row, col]))
            else:
                # insert a recursive matrix box
                line.append("%s" % (make_boxed_tensor_latex(x[row, col], box_rows=box_rows, index=index + 2)))
        # either box the whole row or just box entire matrices
        if box_rows:
            mat.append("\\fbox { $ " + " ".join(line) + " \strut $ } ")
        else:
            mat.append(" ".join(line))
    mat_code = "\\\\ \n".join(mat)
    return "  \\fbox{  $ \n " + mat_code + "  \strut $ }\ \ "


def show_boxed_tensor_latex(x, box_rows=True):
    # show the matrix in the notebook as a LaTeX equation
    IPython.display.display(IPython.display.Latex("\\[ " + make_boxed_tensor_latex(x, box_rows=box_rows) + " \\]"))


def print_matrix(name, matrix, prec=2):
    # print scalars
    if not hasattr(matrix, "__len__"):
        IPython.display.display(IPython.display.Latex("${0} = {1}$".format(name, matrix)))
        return

    if str(matrix.dtype).startswith("float"):
        matrix = np.around(matrix, prec)

    if len(matrix.shape) == 1:
        matrix = matrix[None, :]

    if sympy:
        IPython.display.display(IPython.display.Latex("${0} = {1}$".format(name, sympy.latex(sympy.Matrix(matrix)))))
    else:
        print(name, "\n", matrix)
