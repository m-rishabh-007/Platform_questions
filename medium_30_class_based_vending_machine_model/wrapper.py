# ===== PLATFORM INJECTION POINT =====
# Contestant's Solution class will be injected here
# ===== END INJECTION POINT =====

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