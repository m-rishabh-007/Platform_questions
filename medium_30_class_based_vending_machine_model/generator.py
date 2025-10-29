"""Problem-specific test case generator.

This script is called by `orchestrator.py` with JSON arguments that match
the `generation_logic` section of `config.json`. Implement the
`generate_case` function so that it produces _exactly one_ test case using
the provided rule arguments and prints it to STDOUT in the format expected
by the wrappers.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from typing import Any, Dict


def generate_case(rule_type: str, args: Dict[str, Any]) -> str:
    """Return the stdin payload for a single test case.

    Parameters
    ----------
    rule_type: str
        One of the keys defined in `config.json` (for example,
        \"boundary_values\", \"edge_cases\", \"random_valid\", \"stress_test\").
    args: Dict[str, Any]
        JSON-compatible data that describes how to build the test case.

    Returns
    -------
    str
        A newline-terminated string that will be written directly to STDOUT.
    """

    rng = random.Random(args.get("seed"))

    if rule_type == "boundary_values":
        # Minimum and maximum constraint test cases
        scenarios = [
            # Minimum case: 1 product, 1 request
            (1, 1, 100, 5, 1, 10, 150),
            # Maximum case: many products, many requests  
            (20, 25, 500, 50, 1, 50, 1000),
            # Edge pricing: low prices
            (3, 5, 50, 10, 1, 1, 100),
        ]
        scenario = rng.choice(scenarios)
        return generate_vending_test_case(*scenario)
    
    elif rule_type == "edge_cases":
        # Special edge cases: out of stock, insufficient funds, not found
        edge_types = [
            "out_of_stock",
            "insufficient_funds", 
            "product_not_found",
            "mixed_scenarios"
        ]
        edge_type = rng.choice(edge_types)
        
        if edge_type == "out_of_stock":
            # Products with 0 quantity
            num_products = rng.randint(2, 5)
            num_requests = rng.randint(3, 8)
            return generate_out_of_stock_case(num_products, num_requests, rng)
        elif edge_type == "insufficient_funds":
            # Requests with insufficient money
            num_products = rng.randint(2, 5) 
            num_requests = rng.randint(3, 8)
            return generate_insufficient_funds_case(num_products, num_requests, rng)
        elif edge_type == "product_not_found":
            # Requests for non-existent products
            num_products = rng.randint(2, 5)
            num_requests = rng.randint(3, 8) 
            return generate_not_found_case(num_products, num_requests, rng)
        else:  # mixed_scenarios
            # Mix of all edge cases
            num_products = rng.randint(3, 8)
            num_requests = rng.randint(5, 12)
            return generate_mixed_edge_case(num_products, num_requests, rng)
    
    elif rule_type == "random_valid":
        # Random valid test cases
        num_products = rng.randint(3, 10)
        num_requests = rng.randint(5, 15)
        max_price = 300
        max_quantity = 20
        max_money = 500
        return generate_vending_test_case(num_products, num_requests, max_price, max_quantity, 1, 20, max_money)
    
    elif rule_type == "stress_test":
        # Large test cases
        num_products = rng.randint(15, 20)
        num_requests = rng.randint(20, 30)
        max_price = 1000
        max_quantity = 50
        max_money = 1500
        return generate_vending_test_case(num_products, num_requests, max_price, max_quantity, 1, 50, max_money)

    raise ValueError(f"Unhandled rule_type: {rule_type}")


def generate_vending_test_case(num_products, num_requests, max_price, max_quantity, min_quantity, min_price, max_money):
    """Generate a vending machine test case with specified parameters."""
    rng = random.Random()
    
    # Generate unique product names
    product_names = []
    for i in range(num_products):
        product_names.append(f"Product_{chr(65+i)}")
    
    # Generate inventory data
    inventory_data = []
    for name in product_names:
        price = rng.randint(min_price, max_price)
        quantity = rng.randint(min_quantity, max_quantity)
        inventory_data.append((name, price, quantity))
    
    # Generate purchase requests
    purchase_requests = []
    for _ in range(num_requests):
        # 70% chance to request existing product, 30% chance for non-existing
        if rng.random() < 0.7 and product_names:
            product_name = rng.choice(product_names)
        else:
            product_name = f"NonExistent_{rng.randint(1, 100)}"
        
        money_inserted = rng.randint(1, max_money)
        purchase_requests.append((product_name, money_inserted))
    
    return format_test_case(inventory_data, purchase_requests)


def generate_out_of_stock_case(num_products, num_requests, rng):
    """Generate test case focused on out-of-stock scenarios."""
    product_names = [f"Product_{chr(65+i)}" for i in range(num_products)]
    
    # Mix of products with stock and without
    inventory_data = []
    for i, name in enumerate(product_names):
        price = rng.randint(20, 100)
        # Some products have 0 stock, others have 1-2 items
        quantity = 0 if i < num_products // 2 else rng.randint(1, 2)
        inventory_data.append((name, price, quantity))
    
    # Generate requests targeting out-of-stock products
    purchase_requests = []
    for _ in range(num_requests):
        product_name = rng.choice(product_names)
        money_inserted = rng.randint(50, 200)  # Sufficient money
        purchase_requests.append((product_name, money_inserted))
    
    return format_test_case(inventory_data, purchase_requests)


def generate_insufficient_funds_case(num_products, num_requests, rng):
    """Generate test case focused on insufficient funds scenarios."""
    product_names = [f"Product_{chr(65+i)}" for i in range(num_products)]
    
    inventory_data = []
    for name in product_names:
        price = rng.randint(50, 200)  # Higher prices
        quantity = rng.randint(2, 10)
        inventory_data.append((name, price, quantity))
    
    # Generate requests with insufficient money
    purchase_requests = []
    for _ in range(num_requests):
        product_name = rng.choice(product_names)
        # Find the price for this product
        product_price = next(price for n, price, _ in inventory_data if n == product_name)
        # 60% chance of insufficient funds
        if rng.random() < 0.6:
            money_inserted = rng.randint(1, product_price - 1)
        else:
            money_inserted = rng.randint(product_price, product_price + 100)
        purchase_requests.append((product_name, money_inserted))
    
    return format_test_case(inventory_data, purchase_requests)


def generate_not_found_case(num_products, num_requests, rng):
    """Generate test case focused on product not found scenarios."""
    product_names = [f"Product_{chr(65+i)}" for i in range(num_products)]
    
    inventory_data = []
    for name in product_names:
        price = rng.randint(20, 100)
        quantity = rng.randint(3, 10)
        inventory_data.append((name, price, quantity))
    
    # Generate requests with many non-existent products
    purchase_requests = []
    for _ in range(num_requests):
        # 70% chance for non-existent product
        if rng.random() < 0.7:
            product_name = f"NonExistent_{rng.randint(1, 100)}"
        else:
            product_name = rng.choice(product_names)
        money_inserted = rng.randint(20, 200)
        purchase_requests.append((product_name, money_inserted))
    
    return format_test_case(inventory_data, purchase_requests)


def generate_mixed_edge_case(num_products, num_requests, rng):
    """Generate test case with mixed edge scenarios."""
    product_names = [f"Product_{chr(65+i)}" for i in range(num_products)]
    
    inventory_data = []
    for i, name in enumerate(product_names):
        price = rng.randint(25, 150)
        # Mix quantities: some 0, some low, some normal
        if i < num_products // 3:
            quantity = 0  # Out of stock
        elif i < 2 * num_products // 3:
            quantity = rng.randint(1, 3)  # Low stock
        else:
            quantity = rng.randint(5, 15)  # Normal stock
        inventory_data.append((name, price, quantity))
    
    # Generate mixed requests
    purchase_requests = []
    for _ in range(num_requests):
        scenario = rng.choice(["existing", "non_existing", "existing"])
        if scenario == "non_existing":
            product_name = f"NonExistent_{rng.randint(1, 100)}"
            money_inserted = rng.randint(20, 200)
        else:
            product_name = rng.choice(product_names)
            product_price = next(price for n, price, _ in inventory_data if n == product_name)
            # Mix of sufficient and insufficient funds
            if rng.random() < 0.4:
                money_inserted = rng.randint(1, max(1, product_price - 1))  # Insufficient
            else:
                money_inserted = rng.randint(product_price, product_price + 100)  # Sufficient
        purchase_requests.append((product_name, money_inserted))
    
    return format_test_case(inventory_data, purchase_requests)


def format_test_case(inventory_data, purchase_requests):
    """Format the test case as input string."""
    lines = []
    
    # Inventory data
    lines.append(str(len(inventory_data)))
    for name, price, quantity in inventory_data:
        lines.append(f"{name} {price} {quantity}")
    
    # Purchase requests
    lines.append(str(len(purchase_requests)))
    for product_name, money_inserted in purchase_requests:
        lines.append(f"{product_name} {money_inserted}")
    
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Problem generator stub")
    parser.add_argument("rule_type", help="Name of the bucket being generated")
    parser.add_argument(
        "--args",
        type=json.loads,
        default="{}",
        help="JSON blob with configuration for this rule",
    )
    parser.add_argument(
        "--rng-seed",
        type=int,
        default=None,
        help="Optional seed override for deterministic debugging",
    )
    parsed = parser.parse_args(argv)
    if parsed.rng_seed is not None:
        parsed.args["seed"] = parsed.rng_seed
    return parsed


def main(argv: list[str]) -> int:
    namespace = parse_args(argv)

    try:
        payload = generate_case(namespace.rule_type, namespace.args)
    except Exception as exc:  # noqa: BLE001
        print(f"Generator error: {exc}", file=sys.stderr)
        return 1

    sys.stdout.write(payload)
    if not payload.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))