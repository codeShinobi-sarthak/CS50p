from abc import ABC, abstractmethod

class DataExporter(ABC):

    @abstractmethod
    def export(self, data):
        pass


class ExportToTxt(DataExporter):

    def export(self, data):
        # with open("output.txt", "w") as file:
        #     file.write(data)

        print(f"Exporting to TXT: {data}")

class ExportTocsv(DataExporter):

    def export(self, data):
        print("Exporting to CSV:")
        print(",".join(data))


def run_export_pipeline(exporter, data):    
    exporter.export(data)


# --- Testing ---
some_data = ["product_id", "product_name", "price", "2025-08-15"]

# Create instances of our concrete exporters
txt_exporter = ExportToTxt()
json_exporter = ExportTocsv()

# Run the pipeline with different exporters
print("--- Using the TXT Exporter ---")
run_export_pipeline(txt_exporter, some_data)

print("\n" + "-"*20 + "\n")

print("--- Using the JSON Exporter ---")
run_export_pipeline(json_exporter, some_data)
