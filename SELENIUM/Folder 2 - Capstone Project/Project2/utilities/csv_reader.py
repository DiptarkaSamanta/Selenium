import csv
import os

class CSVReader:
    @staticmethod
    def read_csv_data(file_path):
        """Reads CSV file and returns list of dictionaries containing row key-value pairs."""
        if not os.path.isabs(file_path):
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV test data file not found at: {file_path}")

        data_list = []
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(dict(row))
        return data_list

    @staticmethod
    def get_data_as_tuples(file_path, keys):
        """Reads CSV file and returns list of tuples matching specified keys."""
        rows = CSVReader.read_csv_data(file_path)
        tuple_list = []
        for row in rows:
            tuple_list.append(tuple(row[k] for k in keys))
        return tuple_list
