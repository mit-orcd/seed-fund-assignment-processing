# Document Assignment Program

This Python program randomly assigns document IDs to names, ensuring each document is assigned exactly twice to different names while maintaining a balanced distribution of documents across all names.

## Features

- Random assignment of documents to names
- Each document is assigned exactly twice
- Each document is assigned to different names
- Balanced distribution of documents across names
- Alphabetically sorted document-to-names mapping
- Input validation and error checking

## Requirements

- Python 3.x
- No external dependencies required

## Input Files

The program requires two input text files:

1. `a.txt`: Contains one name per line
   ```
   Alice
   Bob
   Carol
   David
   ```

2. `b.txt`: Contains one document ID per line
   ```
   DOC001
   DOC002
   DOC003
   DOC004
   ```

## Output Files

The program generates two output files:

1. `assignments.txt`: Lists each name and their assigned documents
   ```
   Alice: DOC001, DOC002, DOC003 (3 documents)
   Bob: DOC004, DOC005, DOC006 (3 documents)
   ```

2. `document_assignments.txt`: Alphabetically sorted list of documents and their assigned names
   ```
   DOC001: Alice, Carol
   DOC002: Bob, David
   ```

## Usage

1. Create the input files `a.txt` and `b.txt` with your names and document IDs
2. Run the program:
   ```bash
   python3 assign_docs.py
   ```
3. Check the output files for the assignments

## Example

Given these input files:

`a.txt`:
```
Alice
Bob
Carol
David
```

`b.txt`:
```
DOC001
DOC002
DOC003
DOC004
```

The program might generate:

`assignments.txt`:
```
Alice: DOC001, DOC003 (2 documents)
Bob: DOC002, DOC004 (2 documents)
Carol: DOC001, DOC002 (2 documents)
David: DOC003, DOC004 (2 documents)
```

`document_assignments.txt`:
```
DOC001: Alice, Carol
DOC002: Bob, Carol
DOC003: Alice, David
DOC004: Bob, David
```

## Notes

- The program requires at least 2 names to make valid assignments
- The number of documents per name will be balanced (within 1 document)
- Each document will be assigned exactly twice to different names
- The program includes error checking and will display warnings if assignments cannot be completed properly
