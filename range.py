for i in range(10, 20, -2):  # Generates 10, 8, 6, 4, 2
    print(i)

print("--- PROBLEM: Nothing printed! ---")
print("Why? Start=10, End=20, Step=-2")
print("We're trying to go FROM 10 TO 20 but stepping BACKWARDS (-2)")
print("That's impossible! 10 -> 8 -> 6 -> 4... we're going away from 20!")

print("\n--- CORRECT WAYS TO USE RANGE ---")

print("\n1. Going UP with positive step:")
for i in range(10, 20, 2):  # 10 to 20, step +2
    print(i, end=" ")
print("(10 to 20, step +2)")

print("\n2. Going DOWN with negative step:")
for i in range(20, 10, -2):  # 20 to 10, step -2
    print(i, end=" ")
print("(20 to 10, step -2)")

print("\n3. What you probably wanted:")
for i in range(10, 21, 2):  # 10 to 20 (inclusive), step +2
    print(i, end=" ")
print("(10 to 20, step +2)")

print("\n" + "="*50)
print("RANGE RULES:")
print("="*50)
print("range(start, stop, step)")
print("- If step is POSITIVE: start must be < stop")
print("- If step is NEGATIVE: start must be > stop")
print("- If direction is wrong: empty sequence (nothing happens)")

print("\n--- EXAMPLES OF WRONG DIRECTIONS (empty results) ---")
print("range(10, 20, -1):", list(range(10, 20, -1)))  # Empty!
print("range(20, 10, 1):", list(range(20, 10, 1)))    # Empty!
print("range(5, 15, -3):", list(range(5, 15, -3)))    # Empty!

print("\n--- EXAMPLES OF CORRECT DIRECTIONS ---")
print("range(10, 20, 1):", list(range(10, 20, 1)))    # Works!
print("range(20, 10, -1):", list(range(20, 10, -1)))  # Works!
print("range(5, 15, 3):", list(range(5, 15, 3)))      # Works!

print("\n--- MEMORY TIP ---")
print("Think of it like walking:")
print("🚶‍♂️ To go from house 10 to house 20: take POSITIVE steps (+1, +2, +3...)")
print("🚶‍♂️ To go from house 20 to house 10: take NEGATIVE steps (-1, -2, -3...)")
print("🚫 You can't reach house 20 from house 10 by walking backwards!")

print("\n" + "="*60)
print("HOW RANGE CALCULATES - Step by Step")
print("="*60)

print("\nrange(10, 21, 2) step-by-step calculation:")
print("Start: 10, Stop: 21, Step: 2")
print("Range checks: 'Can I reach the next number before hitting stop?'")

current = 10
step = 2
stop = 21
count = 0

while current < stop:
    print(f"Step {count + 1}: current = {current} (< {stop}? Yes, include it)")
    current += step
    count += 1
    if current >= stop:
        print(f"Next would be: current = {current} (< {stop}? No, stop here)")
        break

print(f"\nResult: {list(range(10, 21, 2))}")

print("\n" + "="*60)
print("WHAT ABOUT THE 'REMAINDER'?")
print("="*60)

# Let's see what happens with different ranges
test_cases = [
    (10, 21, 2),  # Perfect fit
    (10, 22, 2),  # One extra
    (10, 20, 2),  # One short
    (0, 10, 3),   # With remainder
    (0, 11, 3),   # Different remainder
]

for start, stop, step in test_cases:
    result = list(range(start, stop, step))
    if result:
        last_value = result[-1]
        next_would_be = last_value + step
        distance_to_stop = stop - last_value
        
        print(f"\nrange({start}, {stop}, {step}) = {result}")
        print(f"Last value: {last_value}")
        print(f"Next would be: {next_would_be} (but {next_would_be} >= {stop}, so stopped)")
        print(f"Distance from last value to stop: {distance_to_stop}")

print("\n" + "="*60)
print("THE MATHEMATICAL FORMULA")
print("="*60)

print("Python uses this logic internally:")
print("For range(start, stop, step):")
print("1. Check if direction is correct")
print("2. Calculate: how many steps fit?")
print("   Formula: (stop - start + step - 1) // step")
print("3. Generate exactly that many values")

def explain_range_calculation(start, stop, step):
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return f"range({start}, {stop}, {step}) = [] (wrong direction)"
    
    # This is the actual formula Python uses internally
    count = max(0, (stop - start + step - 1) // step)
    
    print(f"\nrange({start}, {stop}, {step}):")
    print(f"  Formula: (stop - start + step - 1) // step")
    print(f"  = ({stop} - {start} + {step} - 1) // {step}")
    print(f"  = ({stop - start + step - 1}) // {step}")
    print(f"  = {count} values")
    
    # Generate the actual values
    values = [start + i * step for i in range(count)]
    print(f"  Values: {values}")
    print(f"  Last value: {values[-1] if values else 'None'}")
    if values:
        remainder = stop - (values[-1] + step)
        print(f"  Next would be: {values[-1] + step} (exceeds stop by {abs(remainder)})")
    
    return values

# Test the formula
test_cases = [
    (10, 21, 2),
    (0, 10, 3),
    (20, 10, -2),
    (5, 17, 4)
]

for start, stop, step in test_cases:
    explain_range_calculation(start, stop, step)