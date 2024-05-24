import csv


def simple_sort_based_join(product_filename, maker_filename, output_filename):
    """
    Executes a simple sort-based join between two datasets and writes the output to a CSV file.

    :param product_filename: Filename of the sorted product dataset.
    :param maker_filename: Filename of the sorted maker dataset.
    :param output_filename: Filename for the output joined dataset.
    """
    with open(product_filename) as fl0, open(maker_filename) as fl1, open(
        output_filename, "w", newline=""
    ) as result:
        read0 = csv.reader(fl0)
        read1 = csv.reader(fl1)
        buff0 = next(read0)
        buff1 = next(read1)
        write_fl = csv.writer(result)
        while (buff0 is not None) and (buff1 is not None):
            if buff0[0] == buff1[0]:
                buff2 = [buff0[0], buff0[1], buff1[1]]
                write_fl.writerow(buff2)
                buff0 = next(read0, None)
                buff1 = next(read1, None)
            elif buff0[0] < buff1[0]:
                buff0 = next(read0, None)
            else:
                buff1 = next(read1, None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print(
            "Usage: python ssb_join.py <product_file.csv> <maker_file.csv> <output_file.csv>"
        )
    else:
        simple_sort_based_join(sys.argv[1], sys.argv[2], sys.argv[3])
