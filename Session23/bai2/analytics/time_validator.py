from datetime import datetime


def parse_and_inspect_date(date_str):

    try:
        parsed_date = datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )

        return parsed_date

    except ValueError:

        print(
            f"[WARNING] "
            f"Định dạng ngày upload "
            f"'{date_str}' không tồn tại"
        )

        return None