import re
import datetime

def write_ids(file_name: str, ids: list[str]):
    with open(file_name, 'x') as w_file:
        for u_id in ids:
            w_file.write(f"{u_id}\n")

if __name__ == "__main__":
    with open("logs_comments.txt") as input_f:
        log_file_content = input_f.read()

        # Extract IDs after "Steam error" and "Done" messages, preserving order and making them unique
        error_ids = []
        done_ids = []

        error_set = set()
        done_set = set()

        for match in re.finditer(r"Steam error with (\d+)", log_file_content):
            error_id = match.group(1)
            if error_id not in error_set:
                error_ids.append(error_id)
                error_set.add(error_id)

        for match in re.finditer(r"Done with (\d+)", log_file_content):
            done_id = match.group(1)
            if done_id not in done_set:
                done_ids.append(done_id)
                done_set.add(done_id)

        time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
        write_ids(f"error_{time_now}_.txt", error_ids)
        write_ids(f"done_{time_now}_.txt", done_ids)
