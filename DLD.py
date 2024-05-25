from itertools import combinations

# Define functions for handling minterms and prime implicants

def generate_mints(input_str):
    
    ascii_codes = [ord(char) for char in input_str.upper()]  # Get ASCII codes of uppercase characters in the input string
    mints = set()
    for code in ascii_codes:
        for digit in str(code):
            mints.add(int(digit))  # Add individual digits of ASCII codes to the set of minterms
    return list(mints)

def binary_rep(mint, num_vars):
   
    return format(mint, f'0{num_vars}b')  # Format the minterm as a binary string with leading zeros

def combine_terms(term1, term2):
    
    diff = sum(1 for a, b in zip(term1, term2) if a != b)  # Count the number of differing bits
    if diff == 1:
        return ''.join('-' if a != b else a for a, b in zip(term1, term2))  # Combine the terms with '-' for differing bit
    return None

def find_prime_imps(mints, num_vars):
    
    terms = [binary_rep(mint, num_vars) for mint in mints]  # Convert minterms to binary representations
    prime_imps = set()
    while terms:
        new_terms = set()
        marked = set()
        for term1, term2 in combinations(terms, 2):  # Try combining all pairs of terms
            combined = combine_terms(term1, term2)
            if combined:
                new_terms.add(combined)
                marked.add(term1)
                marked.add(term2)
        prime_imps.update(term for term in terms if term not in marked)  # Add unmarked terms to prime implicants
        terms = list(new_terms)  # Update terms with new combined terms
    return list(prime_imps)

def find_ess_prime_imps(mints, prime_imps):
   
    coverage = {mint: [] for mint in mints}  # Initialize coverage dictionary
    for prime in prime_imps:
        for mint in mints:
            binary_mint = binary_rep(mint, len(prime))
            if all(p == '-' or p == m for p, m in zip(prime, binary_mint)):  # Check if prime implicant covers minterm
                coverage[mint].append(prime)
    ess_prime_imps = set()
    for mint, primes in coverage.items():
        if len(primes) == 1:  # If a minterm is covered by only one prime implicant, it's essential
            ess_prime_imps.add(primes[0])
    return list(ess_prime_imps)

def minimize_exp(mints, ess_prime_imps, num_vars, vars):
    
    minimized_terms = []
    for implicant in ess_prime_imps:
        term = ''.join(
            vars[i] + ("'" if bit == '0' else '')
            for i, bit in enumerate(implicant) if bit != '-'
        )
        minimized_terms.append(term)
    minimized_exp = " + ".join(minimized_terms)
    return minimized_exp

# Part (a)
name_a = "EKTA"
mints_a = generate_mints(name_a)
num_vars_a = 4
vars_a = "ABCD"
prime_imps_a = find_prime_imps(mints_a, num_vars_a)
ess_prime_imps_a = find_ess_prime_imps(mints_a, prime_imps_a)
minimized_exp_a = minimize_exp(mints_a, ess_prime_imps_a, num_vars_a, vars_a)

print("Part (a):")
print("Minterms:", mints_a)
print("Prime Implicants:", prime_imps_a)
print("Essential Prime Implicants:", ess_prime_imps_a)
print("Minimized SOP Expression:", minimized_exp_a)
print()

# Part (b)
mints_b = [0, 5, 7, 8, 9, 12, 13, 23, 24, 25, 28, 29, 37, 40, 42, 44, 46, 55, 56, 57, 60, 61]
num_vars_b = 6
vars_b = "ABCDEF"
prime_imps_b = find_prime_imps(mints_b, num_vars_b)
ess_prime_imps_b = find_ess_prime_imps(mints_b, prime_imps_b)
minimized_exp_b = minimize_exp(mints_b, ess_prime_imps_b, num_vars_b, vars_b)

print("Part (b):")
print("Minterms:", mints_b)
print("Prime Implicants:")
for imp in prime_imps_b:
    print(imp)
print("Essential Prime Implicants:")
for imp in ess_prime_imps_b:
    print(imp)
print("Minimized SOP Expression:", minimized_exp_b)

# Adding the 7th prime implicant to the minimized expression for part (b)
additional_prime_imp = find_prime_imps([7], num_vars_b)
ess_prime_imps_b += additional_prime_imp
minimized_exp_b_updated = minimize_exp(mints_b, ess_prime_imps_b, num_vars_b, vars_b)

print("\nPart (b) with 7th Prime Implicant Added:")
print("Updated Minimized SOP Expression:", minimized_exp_b_updated)
