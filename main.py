import sys
import traceback

def problematic_function(data):
    """
    This function is designed to cause a TypeError if 'data' is not a string.
    """
    print(f"Attempting to process data: {data}")
    # Intentionally cause a TypeError: can only concatenate str (not "int") to str
    # This line illustrates a common error that an AI explainer would target.
    result = "Processed: " + data
    return result

def ai_error_explainer(error_message):
    """
    Simulates an AI-powered error explainer.
    In a real scenario, this would use NLP/ML to parse the error message.
    Here, it provides a hardcoded explanation for a common TypeError based on its message.
    """
    # Check for a specific TypeError message pattern
    if "can only concatenate str (not " in error_message and "to str" in error_message:
        return (
            "\n--- AI Error Explainer ---\n"
            "**Error Type:** TypeError\n"
            "**Problem:** You tried to combine (concatenate) a string with a non-string type "
            "(like an integer, float, or list) using the `+` operator. Python requires both "
            "sides of the `+` for string concatenation to be strings.\n"
            "**Solution:** Convert the non-string variable to a string before concatenating it. "
            "For example, if `data` is an integer, use `str(data)`.\n"
            "**Example Fix:** `result = 'Processed: ' + str(data)`\n"
            "--- End AI Explainer ---\n"
        )
    # Add more conditions for other common errors if desired, e.g., IndexError
    elif "list index out of range" in error_message:
        return (
            "\n--- AI Error Explainer ---\n"
            "**Error Type:** IndexError\n"
            "**Problem:** You tried to access an element in a list or sequence using an index "
            "that is outside the valid range (0 to length-1).\n"
            "**Solution:** Check the length of your list/sequence and ensure your index is "
            "within the valid range.\n"
            "--- End AI Explainer ---\n"
        )
    else:
        # Fallback for errors not specifically handled by this simulated AI
        return (
            "\n--- AI Error Explainer ---\n"
            "**Problem:** This simulated AI explainer does not have a specific explanation "
            "for the error message: '" + error_message.split('\n')[0] + "'.\n"
            "**Suggestion:** A real AI would analyze this message further. For now, "
            "consult documentation or search online.\n"
            "--- End AI Explainer ---\n"
        )

if __name__ == "__main__":
    print("--- Simulating a common programming error ---")
    # This variable's type (integer) will cause a TypeError when concatenated with a string.
    # An AI explainer aims to simplify understanding errors like this.
    user_input_with_error = 123

    try:
        print(f"\nAttempting to run problematic_function with input: {user_input_with_error} (type: {type(user_input_with_error)})")
        processed_data = problematic_function(user_input_with_error)
        print(f"Successfully processed: {processed_data}")
    except Exception as e:
        # Catching the exception to simulate an AI analyzing the error message.
        print(f"\n!!! An error occurred: {e.__class__.__name__} - {e}")
        # The AI explainer takes the raw error message to provide a human-readable explanation.
        explanation = ai_error_explainer(str(e))
        print(explanation)

    print("\n" + "="*50 + "\n")
    print("--- Example with correct input ---")
    # This variable's type (string) will work correctly.
    user_input_correct = "world"
    try:
        print(f"\nAttempting to run problematic_function with input: {user_input_correct} (type: {type(user_input_correct)})")
        processed_data = problematic_function(user_input_correct)
        print(f"Successfully processed: {processed_data}")
    except Exception as e:
        print(f"\n!!! An error occurred with correct input: {e.__class__.__name__} - {e}")
        explanation = ai_error_explainer(str(e))
        print(explanation)
