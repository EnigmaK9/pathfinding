from pathlib import Path

def collect_to_txt(source_dir: str, output_filepath: str):
    """
    Finds .py and .md files (excluding __pycache__), reads their contents, 
    and writes them all into a single text file with headers for each file.
    """
    source_path = Path(source_dir)
    output_path = Path(output_filepath)
    
    target_extensions = {'.py', '.md'}
    collected_count = 0

    # Open the final text file in write mode
    # Using utf-8 encoding to prevent errors with special characters
    with open(output_path, 'w', encoding='utf-8') as outfile:
        
        for file_path in source_path.rglob('*'):
            
            # 1. Skip directories
            if not file_path.is_file():
                continue

            # 2. Exclude Python cache
            if '__pycache__' in file_path.parts:
                continue

            # 3. Process matching extensions
            if file_path.suffix in target_extensions:
                
                # Prevent the script from reading the output file if you happened 
                # to name it output.md or output.py and put it in the same directory
                if file_path.resolve() == output_path.resolve():
                    continue

                relative_path = file_path.relative_to(source_path)
                
                try:
                    # Read the individual file's content
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                    # Write a clear visual separator and the file path
                    outfile.write(f"{'='*60}\n")
                    outfile.write(f"File: {relative_path}\n")
                    outfile.write(f"{'='*60}\n\n")
                    
                    # Write the actual content followed by a couple of newlines
                    outfile.write(content)
                    outfile.write("\n\n")
                    
                    print(f"Added to text file: {relative_path}")
                    collected_count += 1
                    
                except UnicodeDecodeError:
                    print(f"Skipped {relative_path}: Not a readable text file (encoding issue).")
                except Exception as e:
                    print(f"Error reading {relative_path}: {e}")

    print(f"\nDone! Successfully combined {collected_count} files into '{output_filepath}'.")

if __name__ == "__main__":
    # "." means the directory you are currently running the script from
    SOURCE_DIRECTORY = "." 
    
    # The name of the single text file you want to generate
    OUTPUT_FILE = "collected_codebase.txt"

    # Run the script
    collect_to_txt(SOURCE_DIRECTORY, OUTPUT_FILE)
