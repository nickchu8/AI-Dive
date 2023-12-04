
import pandas as pd

class Saver:
    def __init__(self, output_file, format="csv", save_every=None):
        self.output_file = output_file
        self.format = format
        self.save_every = save_every

    def save(self, results):
        match self.format:
            case "csv":
                self.save_csv(results)
            case _:
                raise ValueError(f"Unsupported format: {self.format}")
            
    def save_csv(self, results):
        print(f"Saving {len(results)} results to {self.output_file}")
        df = pd.DataFrame(results)
        df.to_csv(self.output_file, index=False)
    
