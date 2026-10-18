# LABORATORY MANUAL: ADDITIONAL EXERCISES (SINGLE NOTEBOOK)
# Target Folder: Lab5_Algorithms_BigO

import random
import time

LAST_NAME = "Tojot"
STUDENT_ID = "7965"
FAVORITE_ARTIST = "NFRealMusic"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(digit) for digit in STUDENT_ID)
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(char.upper()) - ord('A') + 1 for char in FAVORITE_ARTIST if char.isalpha())

print("="*70)
print("STUDENT-SPECIFIC PARAMETERS LOADED")
print(f"LAST_NAME: {LAST_NAME} (Length: {NAME_LENGTH})[cite: 3]")
print(f"STUDENT_ID: {STUDENT_ID} (Seed Digit: {SEED_DIGIT}, ID Sum: {ID_SUM})[cite: 3]")
print(f"FAVORITE_ARTIST: {FAVORITE_ARTIST} (Length: {ARTIST_LENGTH}, Alphabet Sum: {ARTIST_SUM})[cite: 3]")
print("="*70)

# 1. EMERGENCY DISPATCH RECORD SEARCH

print("\n[EXERCISE 1] Emergency Dispatch Record Search[cite: 3]")

original_records = sorted(random.sample(range(1000, 5000), 12))
rotation_point = SEED_DIGIT % len(original_records)
rotated_records = original_records[rotation_point:] + original_records[:rotation_point]
target_index = (ID_SUM + ARTIST_SUM) % len(original_records)
target_incident = original_records[target_index]

print(f"Original Records: {original_records}")
print(f"Rotated Records:  {rotated_records}")
print(f"Target Incident:  {target_incident}")

def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    comps = 0
    while left <= right:
        comps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comps
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1, comps

def linear_search(arr, target):
    comps = 0
    for i in range(len(arr)):
        comps += 1
        if arr[i] == target:
            return i, comps
    return -1, comps

pos_rot, comps_rot = search_rotated(rotated_records, target_incident)
pos_lin, comps_lin = linear_search(rotated_records, target_incident)

print(f"-> Rotated Binary Search: Position = {pos_rot}, Comparisons = {comps_rot}")
print(f"-> Linear Search:         Position = {pos_lin}, Comparisons = {comps_lin}")
print(f"-> Time Complexity:       Rotated O(log n) vs Linear O(n)")
print(f"-> Space Complexity:      O(1) for both algorithms")

# 2. UNIVERSITY ENROLLMENT RECORDS

print("\n" + "="*70)
print("[EXERCISE 2] University Enrollment Records[cite: 2]")

start_a = SEED_DIGIT * 100
dataset_a = sorted([start_a + (i * 5) for i in range((ID_SUM % 5) + 5)])

start_b = ARTIST_LENGTH * 100
dataset_b = sorted([start_b + (i * 4) for i in range(NAME_LENGTH + 5)])

print(f"Department A Dataset: {dataset_a}")
print(f"Department B Dataset: {dataset_b}")

def consolidate_datasets(arr1, arr2):
    consolidated = []
    i, j = 0, 0
    comparisons = 0
    while i < len(arr1) and j < len(arr2):
        comparisons += 1
        if arr1[i] < arr2[j]:
            consolidated.append(arr1[i])
            i += 1
        else:
            consolidated.append(arr2[j])
            j += 1
    consolidated.extend(arr1[i:])
    consolidated.extend(arr2[j:])
    return consolidated, comparisons

final_collection, total_comps = consolidate_datasets(dataset_a, dataset_b)

print(f"Consolidated Dataset:         {final_collection}")
print(f"Records Before Consolidation: {len(dataset_a) + len(dataset_b)}")
print(f"Records After Consolidation:  {len(final_collection)}")
print(f"Comparison Count:             {total_comps}")
print(f"Ordering Verified:            {final_collection == sorted(final_collection)}")
print(f"Time and Space Complexity:    Time O(n + m), Space O(n + m)")

# 3. E-COMMERCE ORDER PROCESSING (SECTION 3)

print("\n" + "="*70)
print("[EXERCISE 3] E-Commerce Order Processing[cite: 1, 2]")

dataset_size = 10 + NAME_LENGTH + (ID_SUM % 5)
random.seed(SEED_DIGIT)
base_orders = random.sample(range(100, 999), dataset_size)

# Create input conditions
conditions = {
    "Sorted": sorted(base_orders),
    "Reverse-Ordered": sorted(base_orders, reverse=True),
    "Random": base_orders.copy()
}
random.shuffle(conditions["Random"])

def bubble_sort(arr):
    data = arr.copy()
    comps, moves = 0, 0
    start = time.perf_counter()
    for i in range(len(data)):
        swapped = False
        for j in range(0, len(data) - i - 1):
            comps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                moves += 3
                swapped = True
        if not swapped:
            break
    return data, comps, moves, (time.perf_counter() - start) * 1000

def selection_sort(arr):
    data = arr.copy()
    comps, moves = 0, 0
    start = time.perf_counter()
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            comps += 1
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            moves += 3
    return data, comps, moves, (time.perf_counter() - start) * 1000

def insertion_sort(arr):
    data = arr.copy()
    comps, moves = 0, 0
    start = time.perf_counter()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if data[j] > key:
                data[j + 1] = data[j]
                moves += 1
                j -= 1
            else:
                break
        if j >= 0:
            comps += 1
        data[j + 1] = key
        moves += 1
    return data, comps, moves, (time.perf_counter() - start) * 1000

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

ecommerce_results = []

for cond_name, dataset in conditions.items():
    print(f"\n--- Input Condition: {cond_name} ---")
    for algo_name, algo_func in algorithms.items():
        sorted_data, comps, moves, ex_time = algo_func(dataset)
        is_verified = (sorted_data == sorted(dataset))
        ecommerce_results.append({
            "Condition": cond_name,
            "Algorithm": algo_name,
            "Comparisons": comps,
            "Movements": moves,
            "Time (ms)": f"{ex_time:.4f}",
            "Verified": is_verified
        })
        print(f"  [{algo_name}] Comps: {comps} | Moves: {moves} | Time: {ex_time:.4f}ms | Valid: {is_verified}")

# Final Summary Table Output
print("\n" + "="*70)
print("FINAL PERFORMANCE SUMMARY TABLE (E-COMMERCE)")
print("="*70)
print(f"{'Condition':<15} | {'Algorithm':<15} | {'Comps':<6} | {'Moves':<6} | {'Time (ms)':<10} | {'Valid'}")
print("-" * 75)
for r in ecommerce_results:
    print(f"{r['Condition']:<15} | {r['Algorithm']:<15} | {r['Comparisons']:<6} | {r['Movements']:<6} | {r['Time (ms)']:<10} | {r['Verified']}")
print("="*70)