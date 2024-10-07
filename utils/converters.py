
class Converter:
    def __init__(self):
        pass

    @staticmethod
    def dict_factory(cursor, row):
        """Convert a database row to a dictionary."""
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @staticmethod
    def convert_to_string(data):
        if isinstance(data, dict):
            return ', '.join(f"{key}: {value}" for key, value in data.items())
        elif isinstance(data, list):
            if all(isinstance(item, dict) for item in data):
                return '; '.join(
                    [f"{{{', '.join([f'{key}: {value}' for key, value in item.items()])}}}" for item in data])
            else:
                return ', '.join(f"{Converter.convert_to_string(item)}" for item in data)
        else:
            return str(data)


def safe_assign(target, attr, value):
    if isinstance(value, tuple):
        value = value[0]
    setattr(target, attr, value)