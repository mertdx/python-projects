# %%
"""
--Excel File Comparator--

This module helps you to compare your excel files cell by cell
You need to put your excel files in the same directory with "excel_comparator.py"

author: @mert
"""

import sys
import pandas as pd
import numpy as np
import openpyxl


def import_files(file_1: str, file_2: str, sheet1, sheet2):
    """
    Imports excel files and converts them into dataframes.
    """
    df1 = pd.read_excel(
        file_1, sheet_name=sheet1, na_values=np.nan, header=None)

    df2 = pd.read_excel(
        file_2, sheet_name=sheet2,  na_values=np.nan, header=None)
    return df1, df2


def excel_diff(excel_file_1: str, excel_file_2: str, sheet1=0, sheet2=0):
    """
    Gets the dataframes from import_files function and compares them.
    Exports comparison result to a file named "result.xlsx" in working directory.
    """
    assert isinstance(excel_file_1, str)
    assert isinstance(excel_file_2, str)

    dataframes = import_files(excel_file_1, excel_file_2, sheet1, sheet2)
    df1 = dataframes[0]
    df2 = dataframes[1]

    df1_row, df1_col = df1.shape
    df2_row, df2_col = df2.shape

    df_result = pd.DataFrame(index=range(max(df1_row, df2_row)),
                             columns=range(max(df1_col, df2_col)))
    for row in range(max(df1_row, df2_row)):
        for column in range(max(df1_col, df2_col)):
            try:
                df1_val = df1.iloc[row, column]
            except:
                df1_val = np.nan
            try:
                df2_val = df2.iloc[row, column]
            except:
                df2_val = np.nan
            if df1_val == df2_val:
                df_result[column][row] = df1_val
            elif df1_val != df2_val:
                if df1_val is np.nan:
                    df1_val = ""
                if df2_val is np.nan:
                    df2_val = ""
                df_result[column][row] = f"{df1_val} / {df2_val}"

    df_result.to_excel("result.xlsx")


def main():
    """
    Terminal Operations
    """
    params = ["-file1", "-file2"]
    terminal_input = sys.argv

    if all(x in terminal_input for x in params):
        param1_index = terminal_input.index(params[0])
        param2_index = terminal_input.index(params[1])
        file1 = terminal_input[param1_index + 1]
        file2 = terminal_input[param2_index + 1]
        excel_diff(file1, file2)
    else:
        print(
            "Please make sure using both -file1 and -file2 tags with file names after them")


if __name__ == "__main__":
    main()

# %%
