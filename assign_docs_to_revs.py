import random
import math

def read_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def assign_documents(names, doc_ids):
    # Create a copy of doc_ids to avoid modifying the original
    available_docs = doc_ids.copy()
    assignments = {name: [] for name in names}
    # Track how many times each document has been assigned
    doc_assignment_count = {doc: 0 for doc in doc_ids}
    
    # Calculate target documents per person (rounded up)
    total_docs = len(doc_ids)
    num_names = len(names)
    docs_per_person = math.ceil(total_docs / num_names)
    
    # First pass: assign documents to balance the distribution
    for doc in doc_ids:
        if doc_assignment_count[doc] >= 2:  # Skip if already assigned twice
            continue
            
        # Find names that have fewer than the target number of documents
        available_names = [name for name in names 
                         if doc not in assignments[name] 
                         and len(assignments[name]) < docs_per_person]
        
        if not available_names:
            # If no names meet the criteria, use any name that hasn't been assigned this doc
            available_names = [name for name in names if doc not in assignments[name]]
        
        if not available_names:
            print(f"Warning: Could not find a valid assignment for document {doc}")
            continue
            
        # Choose the name with the fewest documents among available names
        name = min(available_names, key=lambda n: len(assignments[n]))
        assignments[name].append(doc)
        doc_assignment_count[doc] += 1
        if doc in available_docs:
            available_docs.remove(doc)
    
    # Second pass: assign remaining documents to different names
    for doc in doc_ids:
        if doc_assignment_count[doc] >= 2:  # Skip if already assigned twice
            continue
            
        # Get a random name that hasn't been assigned this document yet
        available_names = [name for name in names if doc not in assignments[name]]
        if not available_names:
            print(f"Warning: Could not find a valid assignment for document {doc}")
            continue
            
        # Choose the name with the fewest documents among available names
        name = min(available_names, key=lambda n: len(assignments[n]))
        assignments[name].append(doc)
        doc_assignment_count[doc] += 1
        if doc in available_docs:
            available_docs.remove(doc)
    
    # Verify all documents were assigned exactly twice
    for doc, count in doc_assignment_count.items():
        if count != 2:
            print(f"Warning: Document {doc} was assigned {count} times instead of 2")
    
    return assignments

def write_assignments(assignments, output_file):
    with open(output_file, 'w') as f:
        for name, docs in assignments.items():
            f.write(f"{name}: {', '.join(docs)} ({len(docs)} documents)\n")

def write_document_assignments(assignments, output_file):
    # Create a dictionary mapping documents to their assigned names
    doc_to_names = {}
    for name, docs in assignments.items():
        for doc in docs:
            if doc not in doc_to_names:
                doc_to_names[doc] = []
            doc_to_names[doc].append(name)
    
    # Sort documents alphabetically
    sorted_docs = sorted(doc_to_names.keys())
    
    # Write to file
    with open(output_file, 'w') as f:
        for doc in sorted_docs:
            names = doc_to_names[doc]
            f.write(f"{doc}: {', '.join(names)}\n")

def main():
    # Read input files
    names = read_file('a.txt')
    doc_ids = read_file('b.txt')
    
    # Randomly shuffle the document IDs
    random.shuffle(doc_ids)
    
    # Check if we have enough names for the assignments
    if len(names) < 2:
        print("Error: Need at least 2 names to make assignments")
        return
    
    # Make assignments
    assignments = assign_documents(names, doc_ids)
    
    # Write results to output files
    write_assignments(assignments, 'assignments.txt')
    write_document_assignments(assignments, 'document_assignments.txt')
    print("Assignments have been written to assignments.txt")
    print("Document assignments have been written to document_assignments.txt")
    
    # Print summary of document distribution
    print("\nDocument distribution summary:")
    for name, docs in assignments.items():
        print(f"{name}: {len(docs)} documents")

if __name__ == "__main__":
    main()
