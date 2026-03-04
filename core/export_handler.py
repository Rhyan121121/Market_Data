import subprocess
import os

def export_document(file_path, output_format="png", output_dir="data"):

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False

    try:

        print(f"Converting '{file_path}' to {output_format.upper()}...")


        command = [
            'libreoffice',
            '--headless',
            '--convert-to', output_format,
            '--outdir', output_dir,
            file_path
        ]


        subprocess.run(command, check=True)

        print(f"Success! The {output_format.upper()} file is ready in the '{output_dir}' folder.")
        return True

    except subprocess.CalledProcessError as e:

        print(f"Conversion failed. Error: {e}")
        return False