# Function to create a sorted copy of a list without modifying the original
def make_sorted_copy(old_list):
    try:
        # Check input is a list of integers
        if not isinstance(old_list, list) or not all(isinstance(x, int) for x in old_list):
            raise ValueError

        # Create a copy to sort (original remains unchanged)
        unsorted = old_list[:]
        new_list = []

        # Implementing selection sort
        while unsorted:
            # Assume the first element is the smallest
            smallest = unsorted[0]
            for num in unsorted:
                if num < smallest:
                    smallest = num
            new_list.append(smallest)
            unsorted.remove(smallest)  # Remove from unsorted to avoid duplication

        return new_list

    except ValueError:
        print("Error: Input must be a list of integers.")
        return []

# Main program
if __name__ == "__main__":
    # Test case 1
    original_list = [7, 2, 9, 4, 1, 8, 5, 10, 3, 6]
    sorted_list = make_sorted_copy(original_list)

    print("Original:", original_list)
    print("Sorted:  ", sorted_list)

    # Test case 2 (optional additional test)
    another_list = [12, 3, 7, 5, 1, 9, 8, 2, 10, 6]
    print("\n--- Another Test ---")
    print("Original:", another_list)
    print("Sorted:  ", make_sorted_copy(another_list))
