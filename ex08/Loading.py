import time
import sys
import os


def ft_tqdm(lst: range) -> None:
    """
    Creates a progress bar similar to tqdm.

    Yields items from list while displaying:
    - Percentage completed
    - Progress bar with filled/unfilled portion
    - Current/total items
    - Elapsed time
    - Estimated time remaining
    - Speed (items per second)
    """
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        # take terminel widgth
        try:
            current_t_width = os.get_terminal_size().columns
        except OSError:
            current_t_width = 80
        # last locaton and elpsed time
        current = i + 1
        elapsed_time = time.time() - start_time
        # remaining time and speed measurement
        if elapsed_time > 0:
            speed = current / elapsed_time
            eta_seconds = (total - current) / speed
        else:
            speed = 0
            eta_seconds = 0
        # percentage calculation and output formatting
        percentage = int(current / total * 100)
        elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed_time))
        eta_str = time.strftime("%M:%S", time.gmtime(eta_seconds))
        # Calculate the bar width to accommodate the text.
        bar_width = current_t_width - 43
        if bar_width < 1:
            bar_width = 1
        # calculate the field of filled part
        filled_len = int(bar_width * current // total)
        bar = "=" * filled_len + ">" + " " * (bar_width - filled_len)

        output = f"\r{percentage:3}%|[{bar}]| {current}/{total} "
        output += f"[{elapsed_str}<{eta_str}, {speed:.2f}it/s]"
        # formatting the visiable output -\r, ->
        visible_output = output[1:]
        visible_output = visible_output.ljust(current_t_width)
        sys.stdout.write(f"\r{visible_output[:current_t_width]}")
        sys.stdout.flush()

        yield item
