import json


def parse_interface_status(filename):
    # Открываем JSON файл
    with open(filename, "r") as file:
        data = json.load(file)

    print("Interface Status")
    print("=" * 80)

    # Заголовки таблицы
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)

    # Проходим по массиву imdata
    for item in data["imdata"]:
        attributes = item["l1PhysIf"]["attributes"]

        dn = attributes.get("dn", "")
        descr = attributes.get("descr", "")
        speed = attributes.get("speed", "inherit")
        mtu = attributes.get("mtu", "")

        # Вывод строки таблицы
        print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")


if __name__ == "__main__":
    parse_interface_status("sample-data.json")