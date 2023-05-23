import IPython.display
import numpy as np


def make_boxed_tensor_latex(x: np.ndarray, box_rows: bool = True, index: int = 0) -> str:
    """
    Creates a LaTeX representation of a boxed tensor.

    Args:
        x (np.ndarray): The tensor to represent.
        box_rows (bool, optional):
        Whether to box each row or the entire matrices.
        Defaults to True.
        index (int, optional):
        The index used for recursive matrix box generation.
        Defaults to 0.

    Returns:
        str: The LaTeX representation of the boxed tensor.
    """
    shape = x.shape
    # Ensure it has at least 2D
    if len(shape) == 1:
        x = x[None, :]

    rows, cols = x.shape[0:2]

    mat = []
    # Always generate a matrix starting at the smallest index
    # e.g. a 2x2x3 tensor is a 2x2 matrix of 3-element arrays,
    # not 2 rows of 2x3 matrices
    for row in range(rows):
        line = []
        for col in range(cols):
            if len(x.shape) == 2:
                line.append("\\quad\\hspace{0.5em}\\llap{%d}\\hspace{0.5em}\\strut" % (x[row, col]))
            else:
                # Insert a recursive matrix box
                line.append("%s" % (make_boxed_tensor_latex(x[row, col], box_rows=box_rows, index=index + 2)))
        # Either box the whole row or just box entire matrices
        if box_rows:
            mat.append("\\fbox{$" + " ".join(line) + " \\strut$}")
        else:
            mat.append(" ".join(line))
    mat_code = "\\\\\n".join(mat)
    return "\\fbox{$\n" + mat_code + "\\strut$}"


def show_boxed_tensor_latex(x: np.ndarray, box_rows: bool = True) -> None:
    """
    Displays a matrix as a LaTeX equation in the notebook.

    Args:
        x (ndarray): The matrix to display.
        box_rows (bool, optional):
        Whether to box the rows of the matrix. Defaults to True.
    """
    latex_equation = "\\[ " + make_boxed_tensor_latex(x, box_rows=box_rows) + " \\]"
    IPython.display.display(IPython.display.Latex(latex_equation))


def print_matrix(name: str, matrix: np.ndarray, prec: int = 2) -> None:
    """
    Prints a matrix or scalar as a LaTeX equation in the notebook.

    Args:
        name (str): The name of the matrix or scalar.
        matrix (np.ndarray): The matrix or scalar to print.
        prec (int, optional):
        The precision for rounding floating-point numbers.
        Defaults to 2.
    """
    # Print scalars
    if not hasattr(matrix, "__len__"):
        IPython.display.display(IPython.display.Latex("${0} = {1}$".format(name, matrix)))
        return

    if str(matrix.dtype).startswith("float"):
        matrix = np.around(matrix, prec)

    if len(matrix.shape) == 1:
        matrix = matrix[None, :]

    try:
        import sympy

        IPython.display.display(IPython.display.Latex("${0} = {1}$".format(name, sympy.latex(sympy.Matrix(matrix)))))
    except ImportError:
        # sympy not available, print the matrix directly
        print(name, "\n", matrix)
