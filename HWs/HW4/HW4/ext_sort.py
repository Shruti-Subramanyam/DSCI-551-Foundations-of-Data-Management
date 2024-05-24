import csv
import os


def sort_and_write_chunk(chunk, run_id):
    """
    Sorts a chunk of data in-memory by the first column and writes it to a temporary file.

    :param chunk: A list of data rows to be sorted.
    :param run_id: Identifier for the run, used for naming the temporary file.
    """
    dir = "pass_0"
    os.makedirs(dir, exist_ok=True)
    location_file = os.path.join(dir, f"run_{run_id}.csv")
    chunk.sort(key=lambda x: x[0])
    with open(location_file, "w", newline="") as fl:
        file_write = csv.writer(fl)
        file_write.writerows(chunk)


def merge_runs(run_files, output_filename):
    """
    Merges sorted files (runs) into a single sorted output file.

    :param run_files: List of filenames representing sorted runs to be merged.
    :param output_filename: Filename for the merged, sorted output.
    """
    output_dir = os.path.dirname(output_filename)
    if output_dir != "":
        os.makedirs(output_dir, exist_ok=True)
    if len(run_files) == 1:
        with open(run_files[0]) as src_fl:
            with open(output_filename, "w") as dest_fl:
                for r in src_fl:
                    dest_fl.write(r)
        os.remove(run_files[0])
        return
    with open(run_files[0]) as fl0, open(run_files[1]) as fl1, open(
        output_filename, "w", newline=""
    ) as output:
        read0 = csv.reader(fl0)
        read1 = csv.reader(fl1)
        buff0 = next(read0)
        buff1 = next(read1)
        write_fl = csv.writer(output)
        while (buff0 is not None) and (buff1 is not None):
            if buff0[0] < buff1[0]:
                write_fl.writerow(buff0)
                buff0 = next(read0, None)
            else:
                write_fl.writerow(buff1)
                buff1 = next(read1, None)
        if buff0 is not None:
            write_fl.writerow(buff0)
            for bf0 in read0:
                write_fl.writerow(bf0)
        if buff1 is not None:
            write_fl.writerow(buff1)
            for bf1 in read1:
                write_fl.writerow(bf1)
    os.remove(run_files[0])
    os.remove(run_files[1])


def external_sort(input_filename, output_filename):
    """
    the external sort process: chunking, sorting, and merging.

    :param input_filename: Name of the file with data to sort.
    :param output_filename: Name of the file where sorted data will be written.
    """
    chunk_size = 2
    with open(input_filename) as fl:
        read_fl = csv.reader(fl)
        chunk = []
        cnt_r = 0
        for lines in read_fl:
            chunk.append(lines)
            if len(chunk) == chunk_size:
                sort_and_write_chunk(chunk, cnt_r)
                chunk = []
                cnt_r += 1
    if len(chunk) > 0:
        sort_and_write_chunk(chunk, cnt_r)
    else:
        cnt_r -= 1
    count_pas = 0
    while True:
        dr_pass = f"pass_{count_pas}/"
        new_dir = f"pass_{count_pas + 1}/"
        for run in range(0, cnt_r + 1, 2):
            rpath0 = dr_pass + f"run_{run}.csv"
            rpath1 = dr_pass + f"run_{run+1}.csv"
            if run + 1 > cnt_r:
                run_fl = [rpath0]
            else:
                run_fl = [rpath0, rpath1]
            if cnt_r <= 1:
                merge_runs(run_fl, output_filename)
                os.rmdir(dr_pass)
                return
            else:
                new_path = new_dir + f"run_{run // 2}.csv"
                merge_runs(run_fl, new_path)
        cnt_r = run // 2
        count_pas += 1
        os.rmdir(dr_pass)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 ext_sort.py input.csv output.csv")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        external_sort(input_filename, output_filename)
