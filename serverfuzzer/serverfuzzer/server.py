"""A simple server that processes JSON files for customer orders."""

import json

# TODO: Confirm that you did not change any aspect of this implementation
# TODO: You can make this confirmation by adding a single-line comment
# that clearly states that you did not modify the provided implementation


def process_json(json_str: str) -> float:
    """Process a JSON string and return the highest total price among orders."""
    # load the JSON data by converting from a string to a dictionary
    data = json.loads(json_str)
    # calculate the total price for each order using the
    # price and quantity of each item in the order
    totals = {
        order["id"]: sum(
            item["quantity"] * item["price"] for item in order["items"]
        )
        for order in data
    }
    # return the highest total price
    return max(totals, key=totals.get)  # type: ignore
