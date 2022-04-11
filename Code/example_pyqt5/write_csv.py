import csv
import datetime

header = ["Acitivity", "Time"]

activity_dict = {"Calculus 1": 7200,
                "Linear Algebra": 7100.5,
                "Machine Learning": 7172.73,
                "Finnish 1": 1850.2,
                "Finland Work": 1850.2,
                "Aplus Manual": 17075.178,
                "Programming Y2": 18000,
                "Database": 10000,
                "HEHE": 90566}

today = datetime.date.today()
file_path = "time-management-oop/Code/time_data/" + str(today) + ".csv"

print(file_path)
with open(file_path, "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    for key, value in activity_dict.items():
        writer.writerow([key, value])


