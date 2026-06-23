def calculate_average(scores):

    if not scores:
        return 0

    valid_scores = []

    for score in scores:

        if isinstance(
            score,
            (int, float)
        ):
            valid_scores.append(score)

    if not valid_scores:
        return 0

    average = (
        sum(valid_scores)
        / len(valid_scores)
    )

    return average


def classify_student(average):

    if average >= 8:
        return "Giỏi"

    elif average >= 6.5:
        return "Khá"

    elif average >= 5:
        return "Trung bình"

    return "Yếu"