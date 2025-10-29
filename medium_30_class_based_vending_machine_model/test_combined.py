class Product:
    def __init__(self, name, price):
        """
        Initialize a product with name and price.
        
        :type name: str
        :type price: int
        """
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        """
        Initialize an empty vending machine.
        """
        self.inventory = {}
    
    def restock(self, products):
        """
        Restock the vending machine with products.
        
        :type products: List[Tuple[str, int, int]]  # (name, price, quantity)
        :rtype: None
        """
        for name, price, quantity in products:
            if name in self.inventory:
                # Update existing product
                self.inventory[name]['quantity'] += quantity
            else:
                # Add new product
                self.inventory[name] = {
                    'product': Product(name, price),
                    'quantity': quantity
                }

class Solution:
    def purchase(self, inventory_data, purchase_requests):
        """
        Process purchase requests against vending machine inventory.
        
        :type inventory_data: List[Tuple[str, int, int]]  # (name, price, quantity)
        :type purchase_requests: List[Tuple[str, int]]  # (product_name, money_inserted)
        :rtype: List[Tuple[str, str, int]]  # (status, item_name, change)
        """
        # Initialize vending machine and restock
        machine = VendingMachine()
        machine.restock(inventory_data)
        
        results = []
        
        for product_name, money_inserted in purchase_requests:
            # Check if product exists
            if product_name not in machine.inventory:
                results.append(("PRODUCT_NOT_FOUND", "", money_inserted))
                continue
            
            # Check if product is available
            if machine.inventory[product_name]['quantity'] <= 0:
                results.append(("OUT_OF_STOCK", "", money_inserted))
                continue
            
            # Check if sufficient money provided
            product_price = machine.inventory[product_name]['product'].price
            if money_inserted < product_price:
                results.append(("INSUFFICIENT_FUNDS", "", money_inserted))
                continue
            
            # Process successful purchase
            change = money_inserted - product_price
            machine.inventory[product_name]['quantity'] -= 1
            results.append(("SUCCESS", product_name, change))
        
        return results

def execute_solution():
    # Read inventory data
    n = int(input().strip())
    inventory_data = []
    for _ in range(n):
        line = input().strip().split()
        name = line[0]
        price = int(line[1])
        quantity = int(line[2])
        inventory_data.append((name, price, quantity))
    
    # Read purchase requests
    m = int(input().strip())
    purchase_requests = []
    for _ in range(m):
        line = input().strip().split()
        product_name = line[0]
        money_inserted = int(line[1])
        purchase_requests.append((product_name, money_inserted))
    
    # Execute solution
    solution = Solution()
    results = solution.purchase(inventory_data, purchase_requests)
    
    # Output results
    for status, item_name, change in results:
        if status == "SUCCESS":
            print(f"{status} {item_name} {change}")
        else:
            print(f"{status} {change}")

if __name__ == "__main__":
    execute_solution()