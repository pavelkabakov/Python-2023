import csv
import Note


class FileWriter:
    __filename = "Notes.csv"

    def file_write(note: Note, filename: str):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            row = note.get_id() + note.get_date() + note.get_head() + note.get_body()
            writer.writerow(row)

    def file_read(date: [], filename: str):
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], "-", row[1], "-", row[2], "-", row[3])
