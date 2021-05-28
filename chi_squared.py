# Two simple functions. The first returns the expected values for a contingency table.
# The second computes a chi-squared statistic for a contingency table.
# By Ewen Bramble

def expected_value(rows):
    """Function takes rows of observed counts as list of lists, returns expected values
    in same format"""

    # Get list of row totals, up-down
    row_total = []
    for row in rows:
        row_total.append(sum(row))

    # Get list of column totals, left-right
    col_total = []
    num_rows = len(rows)
    num_col = len(rows[0])

    count = 0  # Column number for loop
    while count < num_col:
        total = 0  # Running column total
        for row in rows:
            total += row[count]
        col_total.append(total)
        count += 1

    sample_size = sum(row_total)

    exp_value_matrix = []
    for i in range(num_rows):  # row by row
        current_row = []  # list of expected values for current row
        for j in range(num_col):  # column by column
            current_row.append(row_total[i] * col_total[j] / sample_size)
        exp_value_matrix.append(current_row)

    return exp_value_matrix


def chi_squared(rows):
    """Function takes rows as list of lists, returns chi squared statistic"""

    exp_vals = expected_value(rows)

    num_rows = len(rows)
    num_col = len(rows[0])

    chi_sq = 0  # initialise chi squared total

    for i in range(num_rows):
        for j in range(num_col):
            chi_sq += (rows[i][j] - exp_vals[i][j]) ** 2 / exp_vals[i][j]

    return chi_sq