def solution(fees, records):
    answer = []
    cars = {}
    for record in records:
        time, car, order = record.split()

        hour, min = time.split(":")
        time = int(hour) * 60 + int(min)

        cars[car] = cars.get(car, []) + [[time, order]]

    for key, value in cars.items():
        if value[-1][1] == "IN":
            value.append([1439, "OUT"])
        total_time = 0
        for i in range(0, len(value), 2):
            total_time += value[i + 1][0] - value[i][0]

        price = fees[1]
        if total_time > fees[0]:
            total_time = ((total_time + 1) - fees[0]) // fees[2]
            price += total_time * fees[3]
        answer.append([price, key])
    answer.sort(key=lambda x: x[1])

    return [ans[0] for ans in answer]


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
